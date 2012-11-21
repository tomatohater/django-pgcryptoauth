from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import connection, transaction
from django.test import TestCase

from pgcryptoauth.hashers import PgCryptoPasswordHasher


class PgCryptoAuthTests(TestCase):
    hasher = PgCryptoPasswordHasher()
    username = u'kingbuzzo'
    password = u'sY0CVj0L56'
    pghash = u'$1$3yGxidZQ$q1ntm5wERWVI2Xq4UbRx8.'
    encoded = u'pgcrypto$%s' % pghash

    def setUp(self):
        cursor = connection.cursor()
        cursor.execute("CREATE EXTENSION pgcrypto")
        transaction.commit_unless_managed()
        
        self.user = User.objects.create_user(username=self.username)
        self.user.password = self.encoded
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_encode(self):
        """
        Test encoder with good password.
        """
        encoded = self.hasher.encode(self.password, self.pghash)
        self.assertEqual(encoded, self.encoded)

    def test_bad_encode(self):
        """
        Test encoder with bad password.
        """
        encoded = self.hasher.encode('bad password', self.pghash)
        self.assertNotEqual(encoded, self.encoded)

    def test_verify(self):
        """
        Test verifier.
        """
        self.assertTrue(self.hasher.verify(self.password, self.encoded))

    def test_authenticate(self):
        """
        Test authentication.
        """
        user = authenticate(username=self.username, password=self.password)
        self.assertTrue(isinstance(user, User))

    def test_bad_authenticate(self):
        """
        Test authentication with bad password.
        """
        user = authenticate(username=self.username, password='bad password')
        self.assertFalse(isinstance(user, User))