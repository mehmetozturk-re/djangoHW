"""This file contains views for requests."""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from .models import Airline, Aircraft
from .serializers import AirlineSerializer
from .serializers import AircraftSerializer
from .serializers import UserTokenSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

# CLASS VIEWS

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class UserObtainTokenAPIView(TokenObtainPairView):
    """Auth view."""

    serializer = UserTokenSerializer


class AircraftCreateAPIView(APIView):
    """Aircraft Create view."""

    def get(self, request):
        """Return get all aircrafts response."""
        aircraft = Aircraft.objects
        serializer = AircraftSerializer(aircraft, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Return Create response."""
        serializer = AircraftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AircraftGetDeleteUpdateByIdAPIView(APIView):
    """Aircraft Update-Delete-Read view."""

    def get_object(self, id):
        """Return object by id."""
        aircraft = get_object_or_404(Aircraft, pk=id)
        return aircraft

    def get(self, request, id):
        """Return get object by id response."""
        aircraft = self.get_object(id=id)
        serializer = AircraftSerializer(aircraft)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        """Return Update response."""
        aircraft = self.get_object(id=id)
        serializer = AircraftSerializer(aircraft, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id):
        """Return Delete response."""
        aircraft = self.get_object(id=id)
        aircraft.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AirlineGetListCreateAPIView(APIView):
    """Aircline Create view."""

    def get(self, request):
        """Return get all airlines response."""
        airlines = Airline.objects
        serializer = AirlineSerializer(airlines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Return Create response."""
        serializer = AirlineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AirlineGetDeleteUpdateByIdAPIView(APIView):
    """Airline Update-Delete-Read view."""

    def get_object(self, id):
        """Return object by id."""
        airline = get_object_or_404(Airline, pk=id)
        return airline

    def get(self, request, id):
        """Return get object by id response."""
        airline = self.get_object(id=id)
        serializer = AirlineSerializer(airline)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        """Return Update response."""
        airline = self.get_object(id=id)
        serializer = AirlineSerializer(airline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id):
        """Return Delete response."""
        airline = self.get_object(id=id)
        airline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# FUNCTION BASED VIEWS


@csrf_exempt
@api_view(['POST', 'GET'])
def airline_get_list_create(request):
    """Return Create response."""
    if request.method == 'GET':
        airlines = Airline.objects
        serializer = AirlineSerializer(airlines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AirlineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'POST'])
def airline_get_delete_update_by_id(request, id):
    """Return Create response."""
    try:
        airline = Airline.objects.get(pk=id)
    except Airline.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AirlineSerializer(airline)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = AirlineSerializer(airline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        airline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
