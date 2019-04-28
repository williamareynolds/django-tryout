# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from helpers import valid_string_failure_message, invalid_string_failure_message
from ..fields import QUALITATIVE_VALUE_VALIDATOR
from ..fields import COMBINED_QUALITATIVE_VALUE_VALIDATOR


class QualitativeFieldTest(TestCase):
    """This class will test the custom field functions and validation."""

    def test_qualitative_validation_regex(self):
        regex = QUALITATIVE_VALUE_VALIDATOR.regex

        valid_strings_to_test = ['+', '-', '?']
        for string in valid_strings_to_test:
            self.assertRegex(
                string,
                regex,
                valid_string_failure_message(string, regex)
            )

        invalid_strings_to_test = ['+-', '', '?+', '0', 'positive']
        for string in invalid_strings_to_test:
            self.assertNotRegex(
                string,
                regex,
                invalid_string_failure_message(string, regex)
            )

    def test_combined_qualitative_validation_regex(self):
        regex = COMBINED_QUALITATIVE_VALUE_VALIDATOR.regex

        valid_strings_to_test = ['-.-', '-.?', '-.+',
                                 '?.-', '?.?', '?.+',
                                 '+.-', '+.?', '+.+']
        for string in valid_strings_to_test:
            self.assertRegex(
                string,
                regex,
                valid_string_failure_message(string, regex)
            )

        invalid_strings_to_test = ['-', '+', '?', '-.', '.+', '?-', '+,-']
        for string in invalid_strings_to_test:
            self.assertNotRegex(
                string,
                regex,
                invalid_string_failure_message(string, regex)
            )
