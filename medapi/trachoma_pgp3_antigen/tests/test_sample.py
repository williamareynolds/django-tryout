from decimal import Decimal
from django.test import TestCase
from helpers import valid_string_failure_message, invalid_string_failure_message
from ..models import Sample


class SampleTest(TestCase):
    """This class will test the basic functionality of the Sample model."""

    def setUp(self):
        Sample.objects.create(
            sex=1,
            age=7,
            age_f='(0,10]',
            luminex_mfi=24000,
            luminex='+',
            luminex_dx='-',
            elisa_od=4.242,
            elisa='?',
            elisa_dx='+',
            elisa_dx_mt='-',
            elisa_pre_od=1.329,
            elisa_pre='+',
            elisa_pre_dx='+',
            elisa_pre_dx_mt='?',
            lfa_serum='-',
            lfa_blood='+',
            lfa_3='-.+',
            lfa_serum_2='-',
            lfa_blood_2='?',
            lfa_2='-.?'
        )

    def test_sample_contains_desired_properties(self):
        sample = Sample.objects.first()
        self.assertEqual(sample.sex, 1)
        self.assertEqual(sample.age, 7)
        self.assertEqual(sample.age_f, '(0,10]')
        self.assertEqual(sample.luminex_mfi, 24000)
        self.assertEqual(sample.luminex, '+')
        self.assertEqual(sample.luminex_dx, '-')
        self.assertEqual(sample.elisa_od, Decimal('4.242'))
        self.assertEqual(sample.elisa, '?')
        self.assertEqual(sample.elisa_dx, '+')
        self.assertEqual(sample.elisa_dx_mt, '-')
        self.assertEqual(sample.elisa_pre_od, Decimal('1.329',))
        self.assertEqual(sample.elisa_pre, '+')
        self.assertEqual(sample.elisa_pre_dx, '+')
        self.assertEqual(sample.elisa_pre_dx_mt, '?')
        self.assertEqual(sample.lfa_serum, '-')
        self.assertEqual(sample.lfa_blood, '+')
        self.assertEqual(sample.lfa_3, '-.+')
        self.assertEqual(sample.lfa_serum_2, '-')
        self.assertEqual(sample.lfa_blood_2, '?')
        self.assertEqual(sample.lfa_2, '-.?')

    def test_sample_age_category_validator(self):
        sample = Sample()
        regex = sample.AGE_CATEGORY_VALIDATOR.regex

        valid_strings = ['[10,20)', '(4,120)', '[0,100]']
        for string in valid_strings:
            self.assertRegex(
                string,
                regex,
                valid_string_failure_message(string, regex)
            )

        invalid_strings = ['{10,20]', '(1,1}', '50,21', '(1000,23)', '[-1,4)']
        for string in invalid_strings:
            self.assertNotRegex(
                string,
                regex,
                invalid_string_failure_message(string, regex)
            )

