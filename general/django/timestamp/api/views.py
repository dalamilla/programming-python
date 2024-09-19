from datetime import datetime, timezone

from rest_framework.response import Response
from rest_framework import views
from .serializers import DateSerializer, DateSerializerException
from .utils import parsing_date


class DateView(views.APIView):
    def get(self, request, input_date=None):

        if input_date is None:
            time_date = datetime.now(timezone.utc)
        elif input_date.isnumeric():
            time_date = datetime.fromtimestamp(int(input_date) / 1000, tz=timezone.utc)
        else:
            try:
                time_date = parsing_date(input_date)
            except ValueError:
                data = {"error": "Invalid Date"}
                return Response(DateSerializerException(data).data, 400)

        unix = int(time_date.timestamp() * 1000)
        utc = time_date.strftime("%a, %d %b %Y %H:%M:%S GMT")

        data = {"unix": unix, "utc": utc}

        return Response(DateSerializer(data).data)
