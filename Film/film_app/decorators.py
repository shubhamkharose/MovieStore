from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        FilmName = args[0].request.data.get("FilmName", "")
        if not FilmName:
            return Response(
                data={
                    "message": "FilmName is required to add a Movie"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated
