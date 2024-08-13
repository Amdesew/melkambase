from rest_framework import serializers
from melkamapp.models import orders, samples, car_spare_part

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = "__all__"

class SamplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = samples
        fields = "__all__"

class CraSparePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = car_spare_part
        fields = "__all__"