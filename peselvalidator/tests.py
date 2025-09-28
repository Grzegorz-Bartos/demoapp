from django.test import TestCase

from .utils import validate_pesel


class PeselTests(TestCase):
    def test_valid_example(self):
        # przykładowy poprawny PESEL: 44051401359 (15-05-1944, M)
        info = validate_pesel("44051401359")
        self.assertTrue(info.valid)
        self.assertEqual(info.gender, "M")

    def test_bad_checksum(self):
        info = validate_pesel("44051401358")
        self.assertFalse(info.valid)
