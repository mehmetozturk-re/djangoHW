"""This file contains serializers for models."""
from rest_framework import serializers
from base.models import Airline, Aircraft
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# MODEL SERIALIZER


class AircraftSerializer(serializers.ModelSerializer):
    """Aircraft model serializer."""

    class Meta:
        """Meta."""

        model = Aircraft
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'manufacturer_serial_number': {'required': False},
            'type': {'required': False},
            'model': {'required': False},
            'number_of_engines': {'required': False},
            'operator_airline': {'required': False},
        }


class AirlineSerializer(serializers.ModelSerializer):
    """Airline model serializer."""

    aircraft_set = AircraftSerializer(many=True, read_only=True)

    class Meta:
        """Meta."""

        model = Airline
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': False},
            'callsign': {'required': False},
            'founded_year': {'required': False},
            'base_airport': {'required': False},
        }


class UserTokenSerializer(TokenObtainPairSerializer):
    """Auth token serializer."""

    @classmethod
    def get_token(cls, user):
        """Return user token."""
        token = super().get_token(user)

        token['username'] = user.username

        return token

# STANDART SERIALIZER
# Class Based yapilmadan once yazdigim serializer.


class AirlineStandartSerializer(serializers.Serializer):
    """Airline serializer for function based views."""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    callsign = serializers.CharField(required=False)
    founded_year = serializers.IntegerField(required=False)
    base_airport = serializers.CharField(required=False)

    def create(self, validated_data):
        """CRUD - Create method."""
        return Airline.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """CRUD - Update method."""
        instance.name = validated_data.get('name', instance.name)
        instance.callsign = validated_data.get('callsign', instance.callsign)
        instance.founded_year = validated_data.get('founded_year',
                                                   instance.founded_year)
        instance.base_airport = validated_data.get('base_airport',
                                                   instance.base_airport)
        instance.save()
        return instance
