import os
import openai
from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer

openai.api_key = os.getenv("OPENAI_API_KEY")

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        document = serializer.save()
        with document.file.open('r') as file:
            text = file.read()
        
        # Summarize text
        summary_response = openai.Completion.create(
            engine="davinci-codex",
            prompt=f"Summarize this text: {text}",
            max_tokens=100
        )
        summary = summary_response.choices[0].text.strip()

        # Extract key points
        extraction_response = openai.Completion.create(
            engine="davinci-codex",
            prompt=f"Extract key points from this text: {text}",
            max_tokens=100
        )
        extraction = extraction_response.choices[0].text.strip()

        # Generate thesis
        thesis_response = openai.Completion.create(
            engine="davinci-codex",
            prompt=f"Generate a thesis for this text: {text}",
            max_tokens=100
        )
        thesis = thesis_response.choices[0].text.strip()

        document.summary = summary
        document.extraction = extraction
        document.thesis = thesis
        document.save()

