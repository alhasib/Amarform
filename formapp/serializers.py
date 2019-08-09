from rest_framework import serializers

from .models import Amarform


class AmarformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amarform
        fields = '__all__'