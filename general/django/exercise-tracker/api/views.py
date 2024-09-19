from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, FormParser

from .serializers import (
    UserSerializer,
    ErrorSerializerException,
    ExerciseSerializer,
    LogsSerializer,
)
from .models import User


@api_view(["GET", "POST"])
@parser_classes([JSONParser, FormParser])
def users(request):
    if request.method == "GET":
        data = User.objects.all()
        return Response(UserSerializer(data, many=True).data)
    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        data = {"error": "invalid username"}
        return Response(ErrorSerializerException(data, many=True).data, status=404)


@api_view(["POST"])
@parser_classes([JSONParser, FormParser])
def exercises(request, username_id=None):
    try:
        user = User.objects.get(pk=username_id)
    except User.DoesNotExist:
        data = {"error": "user not found"}
        return Response(ErrorSerializerException(data).data, status=404)
    serializer = ExerciseSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(username_id=user)
        return Response(serializer.data, status=200)
    data = {"error": "invalid exercise info"}
    return Response(ErrorSerializerException(data).data, status=404)


@api_view(["GET"])
@parser_classes([JSONParser, FormParser])
def logs(request, username_id=None):
    try:
        user = User.objects.get(pk=username_id)
    except User.DoesNotExist:
        data = {"error": "username not found"}
        return Response(ErrorSerializerException(data, many=True).data, status=404)
    context = {
        "from": request.query_params.get("from"),
        "to": request.query_params.get("to"),
        "limit": request.query_params.get("limit"),
    }
    return Response(LogsSerializer(user, context=context).data)
