from django.test import TestCase
from .ciphers import caeser_encode

# Create your tests here.
class CiphersTest(TestCase):
    def test_caeser_encoding_1(self):
        plain_text = "hello"
        shift = 1
        expected = "ifmmp"
        output = caeser_encode(plain_text, shift)
        self.assertEqual(expected, output)

    def test_caeser_encoding_2(self):
        plain_text = "winter"
        shift = 3
        expected = "zlqwhu"
        output = caeser_encode(plain_text, shift)
        self.assertEqual(expected, output)

    def test_caeser_encoding_3(self):
        plain_text = 'xyz'
        shift = 3
        expected = 'abc' # should fail because of wrap-around
        output = caeser_encode(plain_text, shift)
        self.assertEqual(expected, output)