from rest_framework import serializers
from Moneyfi.models import MoneyfiModel

class MfSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyfiModel
        fields = '__all__'
