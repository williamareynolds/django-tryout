from django.core.validators import RegexValidator
from django.db import models


QUALITATIVE_VALUES = (
    ('+', 'Positive'),
    ('-', 'Negative'),
    ('?', 'Indeterminate'),
)

COMBINED_QUALITATIVE_VALUES = (
    ('-.-', 'Serum Negative, Blood Negative'),
    ('-.?', 'Serum Negative, Blood Indeterminate'),
    ('-.+', 'Serum Negative, Blood Positive'),
    ('?.-', 'Serum Indeterminate, Blood Negative'),
    ('?.?', 'Serum Indeterminate, Blood Indeterminate'),
    ('?.+', 'Serum Indeterminate, Blood Positive'),
    ('+.-', 'Serum Positive, Blood Negative'),
    ('+.?', 'Serum Positive, Blood Indeterminate'),
    ('+.+', 'Serum Positive, Blood Positive'),
)

QUALITATIVE_VALUE_VALIDATOR = RegexValidator(
    regex=r'^(\+|\?|\-)$',
    message='Qualitative values must be null (unspecified), + (positive), '
            '- (negative), or ? (indeterminate)',
    code='invalid_qualitative_value'
)

COMBINED_QUALITATIVE_VALUE_VALIDATOR = RegexValidator(
    regex=r'^(\+|\?|\-)\.(\+|\?|\-)$',
    message='Combined qualitative values must be a combination of two '
            'qualitative values separated by a single "." (period). '
            'See the lfa.3 description at '
            'https://data.cdc.gov/Global-Health/Tests-for-antibodies-to-'
            'trachoma-PGP3-antigen/pwgb-7r9t',
    code='invalid_combined_qualitative_value'

)


def qualitative_field():
    """
    Create a qualitative result field
    :return:
    :rtype: models.CharField
    """
    return models.CharField(max_length=1,
                            choices=QUALITATIVE_VALUES,
                            null=True,
                            validators=[QUALITATIVE_VALUE_VALIDATOR])


def combined_qualitative_field():
    """
    Create a combined qualitative field
    :return:
    :rtype: models.CharField
    """
    return models.CharField(max_length=3,
                            choices=COMBINED_QUALITATIVE_VALUES,
                            validators=[
                                COMBINED_QUALITATIVE_VALUE_VALIDATOR
                            ],
                            null=True)
