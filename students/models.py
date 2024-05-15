from django.db import models

# Modelo de dados do estudante
class Student(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_ingresso = models.DateField()