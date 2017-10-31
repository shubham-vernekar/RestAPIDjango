from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from . import permissions
from . import serializers
from . import models

# Create your views here.

class HelloApiView(APIView):
	""" Test API View """

	serializer_class = serializers.HelloSerializer

	def get(self,request,format=None):
		""" Returns a list of APIView features. """
		an_apiview = [
			'Uses HTTP methods as function (get, post, patch, put, delete)',
			'It is similar to a tradition Django view',
			'Gives you the most control over your logic',
			"Is mapped manually to URL's"
		]

		return Response({'message':'Hello','APIView':an_apiview})


	def post(self,request):
		""" Create a hello Message """	
		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = "hello {0}".format(name)
			return Response({'Message':message})
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, pk=None):
		""" Handles updating an object. """
		return Response ({"method":"put"})

	def patch(self, request, pk=None):
		""" Updates only fields provided in the request """
		return Response ({"method":"patch"})

	def delete(self, request, pk=None):
		""" Deletes an object. """
		return Response ({"method":"delete"})


class HelloViewSet(viewsets.ViewSet):
	""" Test API Viewset """

	serializer_class = serializers.HelloSerializer


	def list(self,request):
		""" Returns a hello message """

		a_viewset= [
			'Uses actions (list, create, retreve, update, partial_update)',
			'Automatically maps to URLs using Routers',
			'Provides more functionality with less code.',
		]

		return Response({'message':'Hello','a_viewset':a_viewset})
 

	def create(self,request):
		""" Create a new hello message """

		serializer = serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			message = "hello {0}".format(name)
			return Response({'Message':message})
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		""" handles getting an object by its id."""
		return Response ({"http_method":"Retreive"})

	def update(self, request, pk=None):
		""" handles updating an object by its id."""
		return Response ({"http_method":"Update"})

	def partial_update(self, request, pk=None):
		""" handles updating part of an object by its id."""
		return Response ({"http_method":"Patch"})

	def destroy(self, request, pk=None):
		""" Deletes an object. """
		return Response ({"http_method":"delete"})


class UserProfileViewSet(viewsets.ModelViewSet):
	""" Handles creating and updating profiles """
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes=(TokenAuthentication,)
	permission_classes=(permissions.UpdateOwnProfile,)


