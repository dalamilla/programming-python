from rest_framework import serializers
from .models import Url


class UrlShortenerSerializer(serializers.Serializer):
    url = serializers.CharField(source="original_url")
    short_url = serializers.CharField(required=False, source="id")

    def create(self, validated_data):
        return Url.objects.create(**validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["original_url"] = representation.pop("url")
        return representation


class UrlShortenerSerializerException(serializers.Serializer):
    error = serializers.CharField()
