""" from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def members(request):
    return HttpResponse("Hello world!") """

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SymptomSerializer
from .predict import predict_illness
# Import your prediction function here

class PredictIllness(APIView):
    def post(self, request):
        try:
            serializer = SymptomSerializer(data=request.data)
            if serializer.is_valid():
                symptoms = serializer.validated_data
                prediction = predict_illness(symptoms)
                return Response({"prediction": prediction}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
