# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-28 00:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female')], null=True, validators=[django.core.validators.RegexValidator(code='invalid_sex', message='Sex should be 1 (male), 2 (female), or null (not specified).', regex='^(1|2)$')])),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('age_f', models.CharField(max_length=9, null=True, validators=[django.core.validators.RegexValidator(code='invalid_age_category', message='age_f must be null or provided in interval notation. See http://www.sosmath.com/algebra/inequalities/ineq02/ineq02.html for more information.', regex='^(\\(|\\[)\\d{1,3},\\d{1,3}(\\)|\\])$')], verbose_name='age category')),
                ('luminex_mfi', models.IntegerField()),
                ('luminex', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('luminex_dx', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('elisa_od', models.DecimalField(decimal_places=3, max_digits=4)),
                ('elisa', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('elisa_dx', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('elisa_dx_mt', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('elisa_pre_od', models.DecimalField(decimal_places=3, max_digits=4)),
                ('elisa_pre', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('elisa_pre_dx', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('elisa_pre_dx_mt', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('lfa_serum', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('lfa_blood', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('lfa_3', models.CharField(choices=[(b'-.-', b'Serum Negative, Blood Negative'), (b'-.?', b'Serum Negative, Blood Indeterminate'), (b'-.+', b'Serum Negative, Blood Positive'), (b'?.-', b'Serum Indeterminate, Blood Negative'), (b'?.?', b'Serum Indeterminate, Blood Indeterminate'), (b'?.+', b'Serum Indeterminate, Blood Positive'), (b'+.-', b'Serum Positive, Blood Negative'), (b'+.?', b'Serum Positive, Blood Indeterminate'), (b'+.+', b'Serum Positive, Blood Positive')], max_length=3, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_combined_qualitative_value', message=b'Combinde qualitative values must be a combination of two qualitative values separated by a single "." (period). See the lfa.3 description at https://data.cdc.gov/Global-Health/Tests-for-antibodies-to-trachoma-PGP3-antigen/pwgb-7r9t', regex=b'^(\\+|\\?|\\-)\\.(\\+|\\?|\\-)$')])),
                ('lfa_serum_2', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('lfa_blood_2', models.CharField(choices=[(b'+', b'Positive'), (b'-', b'Negative'), (b'?', b'Indeterminate')], max_length=1, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_qualitative_value', message=b'Qualitative values must be null (unspecified), + (positive), - (negative), or ? (indeterminate)', regex=b'^(\\+|\\?|\\-)$')])),
                ('lfa_2', models.CharField(choices=[(b'-.-', b'Serum Negative, Blood Negative'), (b'-.?', b'Serum Negative, Blood Indeterminate'), (b'-.+', b'Serum Negative, Blood Positive'), (b'?.-', b'Serum Indeterminate, Blood Negative'), (b'?.?', b'Serum Indeterminate, Blood Indeterminate'), (b'?.+', b'Serum Indeterminate, Blood Positive'), (b'+.-', b'Serum Positive, Blood Negative'), (b'+.?', b'Serum Positive, Blood Indeterminate'), (b'+.+', b'Serum Positive, Blood Positive')], max_length=3, null=True, validators=[django.core.validators.RegexValidator(code=b'invalid_combined_qualitative_value', message=b'Combinde qualitative values must be a combination of two qualitative values separated by a single "." (period). See the lfa.3 description at https://data.cdc.gov/Global-Health/Tests-for-antibodies-to-trachoma-PGP3-antigen/pwgb-7r9t', regex=b'^(\\+|\\?|\\-)\\.(\\+|\\?|\\-)$')])),
            ],
        ),
    ]
