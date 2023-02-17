from django.shortcuts import render

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Peak
from .serializers import EmployeeSerializers
from django.http import Http404

# Create your views here.


class PeakList(APIView):
    def get(self, request):
        peaks = Peak.objects.all()
        serializer = EmployeeSerializers(peaks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class PeakDetail(APIView):
    def get_object(self, name):
        try:
            return Peak.objects.get(name=name)
        except Peak.DoesNotExist:
            raise Http404

    def get(self, request, name):
        employee = self.get_object(name)
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data)

    def put(self, request, name):
        peak = self.get_object(name)
        serializer = EmployeeSerializers(peak, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        peak = self.get_object(name)
        peak.delete()
        return Response(status.HTTP_204_NO_CONTENT)
