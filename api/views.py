from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from controls.models import Control
from domo.serializers import ControlSerializer
from domo.scripts import light0

class ControlDetail(APIView):
    """
    Retrieve, update or delete a control instance.
    """

    def get_object(self, pk):
        try:
            return Control.objects.get(pk=pk)
        except Control.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        control = self.get_object(pk)
        serializer = ControlSerializer(control)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        control = self.get_object(pk)
        serializer = ControlSerializer(control, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if control.state:
                light0.turn_on()
            else:
                light0.turn_off()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        control = self.get_object(pk)
        control.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
