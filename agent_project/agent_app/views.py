import openai
import os
from django.conf import settings
from rest_framework import viewsets
from .models import Document
from .serializers import DocumentSerializer

openai.api_key = 'OPENAI_API_KEY'

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        document = serializer.save()
        try:
            with document.file.open() as file:
                text = file.read()
        except UnicodeDecodeError:
            with document.file.open() as file:
                text = file.read().decode('utf-8', errors='ignore')
        
        # Summarize text
        summary_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize this text: {text}"}
            ],
            max_tokens=100
        )
        summary = summary_response['choices'][0]['message']['content'].strip()

        # Extract key points
        extraction_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Extract key points from this text: {text}"}
            ],
            max_tokens=100
        )
        extraction = extraction_response['choices'][0]['message']['content'].strip()

        # Generate thesis
        thesis_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Generate a thesis for this text: {text}"}
            ],
            max_tokens=100
        )
        thesis = thesis_response['choices'][0]['message']['content'].strip()

        document.summary = summary
        document.extraction = extraction
        document.thesis = thesis
        document.save()
