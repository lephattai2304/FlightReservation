from rest_framework import serializers
from .models import Flight, Passenger, Reservation
import re


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
    def validate_flightNumber(self, flightNumber):
        if(re.match("^[a-zA-Z0-9]*$",flightNumber)== None):
            raise serializers.ValidationError("Invalid flightNumber. You make sure it is alpha or numberic!")
        return flightNumber
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    # flight = FlightSerializer(read_only = True)
    # passenger = PassengerSerializer(read_only = True)

    # flight = FlightSerializer()
    # passenger = PassengerSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'