from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from api.serializers.serializers import UserSerializer

class RegisterView(APIView):

	serializer_class = UserSerializer

	def post(self, request, *args, **kwargs):

		data = request.POST

		print(kwargs)
		print(request.POST)
		username_val = data['username']
		password_val = data['password']

		email_val = None
		if 'email' in data:
			email_val = data['email']

		user = User()
		user.username = username_val
		user.set_password(password_val)
		if email_val!=None:
			user.email = email_val

		user.save()

		# self.response_list = self.serializer_class(users, many=True).data
		return Response("ok", status=200)



