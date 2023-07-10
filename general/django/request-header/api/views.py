from rest_framework.response import Response
from rest_framework import views
from .serializers import WhoamiSerializer


class WhoamiView(views.APIView):
    def get(self, request):
        data = {
            "ipaddress": request.META.get("REMOTE_ADDR"),
            "language": request.headers["Accept-Language"],
            "software": request.headers["User-Agent"],
        }
        return Response(WhoamiSerializer(data).data)
