from django.urls import path

from measurement.views import SensorView, SensorUpdate, AddTemp

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', AddTemp.as_view()),
]
