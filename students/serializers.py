# students/serializers.py
from rest_framework import serializers
from .models import Student

# Serializer do modelo Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'nome', 'curso', 'matricula', 'data_nascimento', 'email', 'telefone', 'data_ingresso']
