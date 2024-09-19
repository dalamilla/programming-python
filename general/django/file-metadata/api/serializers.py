from rest_framework import serializers


class FileMetadataAnalyseSerializer(serializers.Serializer):
    name = serializers.CharField()
    size = serializers.CharField()
    type = serializers.CharField()
