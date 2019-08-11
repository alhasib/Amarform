from rest_framework import serializers

from .models import Amarform

# model serializer for AmarForm model class

class AmarformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amarform
        fields = '__all__'
