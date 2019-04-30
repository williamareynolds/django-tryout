from rest_framework import serializers
from models import Sample


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = (
            'id',
            'sex',
            'age',
            'age_f',
            'luminex_mfi',
            'luminex',
            'luminex_dx',
            'elisa_od',
            'elisa',
            'elisa_dx',
            'elisa_dx_mt',
            'elisa_pre_od',
            'elisa_pre',
            'elisa_pre_dx',
            'elisa_pre_dx_mt',
            'lfa_serum',
            'lfa_blood',
            'lfa_3',
            'lfa_serum_2',
            'lfa_blood_2',
            'lfa_2',
        )
