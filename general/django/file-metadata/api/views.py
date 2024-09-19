from rest_framework.response import Response
from .serializers import FileMetadataAnalyseSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        file = request.FILES["upfile"]
        name = file.name
        size = file.size
        type = file.content_type

        data = {"name": name, "size": size, "type": type}
        return Response(FileMetadataAnalyseSerializer(data).data)
