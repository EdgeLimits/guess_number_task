from rest_framework import serializers


class GuessSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=["start","<",">","="])
    