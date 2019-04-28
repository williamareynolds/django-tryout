# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
from fields import qualitative_field, combined_qualitative_field


class Sample(models.Model):
    """
    Trachoma PGP3 Antigen test sample
    Each record is the result set of various IF/IC/Genetic assays used to detect
    the presence of the Trachoma PGP3 Antigen. Refer to
    https://data.cdc.gov/Global-Health/Tests-for-antibodies-to-trachoma-PGP3-antigen/pwgb-7r9t
    for more detail and field descriptions. Please note that age has been
    excluded from this data set.
    """
    SEXES = (
        (1, 'Male'),
        (2, 'Female'),
    )

    SEX_VALIDATOR = RegexValidator(
        regex=r'^(1|2)$',
        message='Sex should be 1 (male), 2 (female), or null (not specified).',
        code='invalid_sex'
    )

    AGE_CATEGORY_VALIDATOR = RegexValidator(
        regex=r'^(\(|\[)\d{1,3},\d{1,3}(\)|\])$',
        message='age_f must be null or provided in interval notation. See '
                'http://www.sosmath.com/algebra/inequalities/ineq02/ineq02.html'
                ' for more information.',
        code='invalid_age_category'
    )

    sex = models.PositiveSmallIntegerField(choices=SEXES,
                                           null=True,
                                           validators=[SEX_VALIDATOR])
    age = models.PositiveSmallIntegerField(null=True)
    age_f = models.CharField(max_length=9,
                             null=True,
                             verbose_name='age category',
                             validators=[AGE_CATEGORY_VALIDATOR])
    luminex_mfi = models.IntegerField()
    luminex = qualitative_field()
    luminex_dx = qualitative_field()
    elisa_od = models.DecimalField(max_digits=4, decimal_places=3)
    elisa = qualitative_field()
    elisa_dx = qualitative_field()
    elisa_dx_mt = qualitative_field()
    elisa_pre_od = models.DecimalField(max_digits=4, decimal_places=3)
    elisa_pre = qualitative_field()
    elisa_pre_dx = qualitative_field()
    elisa_pre_dx_mt = qualitative_field()
    lfa_serum = qualitative_field()
    lfa_blood = qualitative_field()
    lfa_3 = combined_qualitative_field()
    lfa_serum_2 = qualitative_field()
    lfa_blood_2 = qualitative_field()
    lfa_2 = combined_qualitative_field()
