from api.models import CustomAuthToken, Trip
from api.serializers import TripSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class GetCreateTripApiView(generics.ListCreateAPIView):
    authentication_classes = [CustomAuthToken]
    permission_classes = [IsAuthenticated]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
