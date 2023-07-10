from rest_framework import serializers


class WhoamiSerializer(serializers.Serializer):
    ipaddress = serializers.CharField()
    language = serializers.CharField()
    software = serializers.CharField()
