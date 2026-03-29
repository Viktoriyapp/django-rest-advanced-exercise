from asyncio import exceptions

from django.http.response import Http404
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    if isinstance(exc, Http404):
        # model_name = exc.__class__.__qualname__
        # <obj in mem> -> .qualname -> Manufacturer.DoesNotExist
        return Response({"detail": "Hey there " + exc.args[0].lower()}, status=HTTP_404_NOT_FOUND)

    if isinstance(exc, PermissionDenied):
        return Response({"detail": f"Access denied for this endpoint"}, status=HTTP_404_NOT_FOUND)

    return exception_handler(exc, context)