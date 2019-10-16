from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from datetime import datetime
from .serializers import FlightSerializer, BookingSerializer 



class FlightListView(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer



class BookingListView(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer