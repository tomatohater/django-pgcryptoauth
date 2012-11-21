import base64

from django.db import connection
from django.contrib.auth.hashers import (BasePasswordHasher, mask_hash)
from django.utils.datastructures import SortedDict
from django.utils.crypto import constant_time_compare
from django.utils.translation import ugettext_noop as _


class PgCryptoPasswordHasher(BasePasswordHasher):
    """
    Password hasher which is intended to provide password continuity from the
    legacy pgcrypto-encoded password (not recommended)

    pgcrypto$hash

    Configured to use the crypt() method from the pgcrypto Postgres extension.
    NOTE: Postgres and pgcrypto are required.
    """
    algorithm = 'pgcrypto'

    def salt(self):
        """
        Generates a salt via pgcrypto.gen_salt('md5').
        """
        cursor = connection.cursor()
        cursor.execute("SELECT gen_salt('md5')")
        return cursor.fetchall()[0][0]

    def encode(self, password, salt=None):
        assert password
        if not salt:
            salt = self.salt()

        cursor = connection.cursor()
        cursor.execute("SELECT crypt('%s', '%s')" % (password, salt))
        hash = cursor.fetchall()[0][0]
        return "%s$%s" % (self.algorithm, hash)

    def verify(self, password, encoded):
        algorithm, hash = encoded.split('$', 1)
        assert algorithm == self.algorithm
        encoded_2 = self.encode(password, hash)
        return constant_time_compare(encoded, encoded_2)

    def safe_summary(self, encoded):
        algorithm, hash = encoded.split('$', 1)
        assert algorithm == self.algorithm
        return SortedDict([
            (_('algorithm'), algorithm),
            (_('hash'), mask_hash(hash)),
        ])
