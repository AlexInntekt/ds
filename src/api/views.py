from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from django.contrib.auth.models import User

from .serializers.serializers import UserSerializer

import random
import datetime


@permission_classes([IsAuthenticated])
class UsersView(APIView):

	serializer_class = UserSerializer

	def get(self, request, *args, **kwargs):
		users = User.objects.all()
		self.response_list = self.serializer_class(users, many=True).data
		return Response(self.response_list, status=200)



class SensorView(APIView):

	def get_data(self):
		data = {}

		air_quality_choices = ['Good', 'Excelent', 'Bad', 'Medium']

		data['temperature'] = str(random.randint(10,28))
		data['humidity'] = str(random.randint(60,85))
		data['air_quality'] = random.choice(air_quality_choices)
		data['timestamp'] = str(datetime.datetime.now())
		data['power_consumption'] = str(random.randint(20, 5000))

		return data

	def get(self, request, *args, **kwargs):
		data = self.get_data()
		data['sensor ID'] = kwargs
		return Response(data, status=200)
