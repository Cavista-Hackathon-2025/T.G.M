from django.urls import path
from .views import PredictIllness

urlpatterns = [
    path('api/predict/', PredictIllness.as_view(), name='predict_illness'),
]
