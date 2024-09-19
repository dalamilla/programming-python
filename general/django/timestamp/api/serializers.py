from rest_framework import serializers


class DateSerializer(serializers.Serializer):
    unix = serializers.IntegerField()
    utc = serializers.CharField()


class DateSerializerException(serializers.Serializer):
    error = serializers.CharField()
