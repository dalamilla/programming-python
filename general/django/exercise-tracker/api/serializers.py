from rest_framework import serializers
from datetime import date
from .models import User, Exercise


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["id"] = str(representation["id"])
        representation["_id"] = representation.pop("id")
        return representation


class ExerciseSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="username_id.username", read_only=True)
    _id = serializers.CharField(source="username_id.id", read_only=True)
    date = serializers.DateField(
        default=date.today(),
        format="%a %b %d %Y",
        input_formats=["%Y-%m-%d", "%a %b %d %Y"],
    )

    class Meta:
        model = Exercise
        fields = ["description", "duration", "date", "username", "_id"]

    def create(self, validated_data):
        return Exercise.objects.create(**validated_data)


class ExerciseBaseSerializer(serializers.ModelSerializer):
    date = serializers.DateField(
        format="%a %b %d %Y",
    )

    class Meta:
        model = Exercise
        fields = ["description", "duration", "date"]


class LogsSerializer(serializers.ModelSerializer):
    log = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "log", "count"]

    def get_log(self, obj):

        from_date = self.context.get("from")
        to_date = self.context.get("to")
        limit = self.context.get("limit")

        if limit is not None:
            limit = int(limit)

        if from_date is None and to_date is None:
            exercise = Exercise.objects.filter(username_id=obj.id)[:limit]
        elif from_date is None:
            exercise = Exercise.objects.filter(username_id=obj.id).filter(
                date__lte=to_date
            )[:limit]
        elif to_date is None:
            exercise = Exercise.objects.filter(username_id=obj.id).filter(
                date__gte=from_date
            )[:limit]
        else:
            exercise = Exercise.objects.filter(username_id=obj.id).filter(
                date__range=[from_date, to_date]
            )[:limit]
        serializer = ExerciseBaseSerializer(exercise, many=True, read_only=True)
        return serializer.data

    def get_count(self, obj):
        count = len(self.get_log(obj))
        return count

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["id"] = str(representation["id"])
        representation["_id"] = representation.pop("id")
        return representation


class ErrorSerializerException(serializers.Serializer):
    error = serializers.CharField()
