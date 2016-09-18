from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

"""
This module contains the API Implementation
"""

class MessageList(APIView):

	def get(self, request, format = None):
		messages = Message.objects.all()
		serializer = MessageSerializer(messages, many=True)
		responseData = {"messages": serializer.data}
		return Response(responseData,status=200)


	def post(self, request, format = None):
		serializer = MessageSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			responseData = {"message": serializer.data}
			return Response(responseData, status=200)
		return Response(serializer.errors, status=400)

	def get_object(self, pk, format = None):
		try:
			return Message.objects.get(pk=pk)
		except Message.DoesNotExist:
			raise Http404

	@csrf_exempt
	def delete(self, request, ss, format = None):
		print "insdie deletess-{}".format(ss)
		message1 = self.get_object(ss)
		message1.delete()
		responseData = {"success": "true"}
		return Response(responseData,status=200)

	


