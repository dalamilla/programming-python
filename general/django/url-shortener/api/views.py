from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser
from rest_framework import views
from .serializers import UrlShortenerSerializer, UrlShortenerSerializerException
from .utils import check_domain, check_url
from .models import Url


class UrlShortenerView(views.APIView):
    parser_classes = [JSONParser, FormParser]

    def get(self, request, short_url=None):
        if short_url.isdigit():
            try:
                url = Url.objects.get(pk=short_url).original_url
                return redirect(url)
            except Url.DoesNotExist:
                data = {"error": "No short URL found for the given input"}
                return Response(UrlShortenerSerializerException(data).data)
        elif isinstance(short_url, str):
            data = {"error": "Wrong format"}
            return Response(UrlShortenerSerializerException(data).data)

    def post(self, request):
        serializer = UrlShortenerSerializer(data=request.data)
        if serializer.is_valid():
            if not check_url(serializer.validated_data.get("original_url")):
                data = {"error": "Invalid url"}
                return Response(UrlShortenerSerializerException(data).data)
            elif not check_domain(serializer.validated_data.get("original_url")):
                data = {"error": "Invalid Hostname"}
                return Response(UrlShortenerSerializerException(data).data)
            serializer.save()
            return Response(serializer.data, status=200)
        data = {"error": "Invalid url"}
        return Response(UrlShortenerSerializerException(data).data)
