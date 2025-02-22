from rest_framework import serializers

class SymptomSerializer(serializers.Serializer):
    symptom1 = serializers.CharField(max_length=100)
    symptom2 = serializers.CharField(max_length=100)
    symptom3 = serializers.CharField(max_length=100)
    symptom4 = serializers.CharField(max_length=100)
    # Add more symptoms as needed