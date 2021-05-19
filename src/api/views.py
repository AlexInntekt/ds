from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response



class UsersView(APIView):

    def get(self, request, *args, **kwargs):

      # file_serializer = BinaryCompanySerializer(data=request.data)

      # validate serializer and then return SUCCES or FAILURE
      # if file_serializer.is_valid():
      #     file_serializer.save()
      #     return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      # else:
      #     return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      return Response("Werks", status=200)


