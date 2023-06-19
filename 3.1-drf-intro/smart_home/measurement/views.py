from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView
from measurement.models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class AddTemp(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
