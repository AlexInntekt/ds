from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from django.contrib.auth.models import User

from .serializers.serializers import UserSerializer

@permission_classes([IsAuthenticated])
class UsersView(APIView):

	serializer_class = UserSerializer

	def get(self, request, *args, **kwargs):
		users = User.objects.all()
		self.response_list = self.serializer_class(users, many=True).data
		return Response(self.response_list, status=200)



