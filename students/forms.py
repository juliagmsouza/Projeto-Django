from django import forms
from .models import Student

# Formulário com dados de entrada para registro de um estudante
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['nome', 'curso', 'matricula', 'data_nascimento', 'email', 'telefone', 'data_ingresso']
