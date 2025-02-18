from django.shortcuts import render
from rest_framework import generics
from .models import Hero, About, Resume, Skills, Projects, Message
from .serializers import HeroSerializer, AboutSerializer, ResumeSerializer, SkillsSerializer, ProjectsSerializer, MessageSerializer
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import os

# Create your views here.

class HeroList(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class AboutList(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ResumeList(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class SkillsList(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class ProjectsList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class SendMessage(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.save()
            
            try:
                # Send email
                subject = f"New Message from {message.name}"
                body = f"""
                Name: {message.name}
                Email: {message.email}
                Message: {message.message}
                """
                send_mail(
                    subject,
                    body,
                    os.getenv('EMAIL'),  # From email
                    [os.getenv('EMAIL')],  # To email
                    fail_silently=False,
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                # Save the message even if email fails
                message.save()
                return Response(
                    {'error': 'Failed to send email but message saved'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
