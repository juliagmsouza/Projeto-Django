from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from .models import Student
from rest_framework.test import APIClient

class StudentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.student = Student.objects.create(
            nome='João da Silva',
            curso='Engenharia',
            matricula='12345',
            data_nascimento='1990-01-01',
            email='joao@example.com',
            telefone='123456789',
            data_ingresso='2020-01-01'
        )

    def test_student_list_view(self):
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.student.nome)

    def test_student_detail_view(self):
        response = self.client.get(reverse('student-detail', args=[self.student.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.student.nome)

    def test_student_create_view(self):
        new_student_data = {
            'nome': 'Maria da Silva',
            'curso': 'Administração',
            'matricula': '54321',
            'data_nascimento': '1995-05-05',
            'email': 'maria@example.com',
            'telefone': '987654321',
            'data_ingresso': '2021-02-01'
        }
        response = self.client.post(reverse('student-create'), new_student_data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Student.objects.filter(nome=new_student_data['nome']).exists())

    def test_student_update_view(self):
        updated_data = {
            'nome': 'João Carlos da Silva',
            'curso': 'Medicina',
            'matricula': '54321',
            'data_nascimento': '1995-05-05',
            'email': 'joao_carlos@example.com',
            'telefone': '987654321',
            'data_ingresso': '2021-02-01'
        }
        response = self.client.put(reverse('student-detail', args=[self.student.id]), updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Student.objects.filter(nome=updated_data['nome']).exists())

    def test_student_delete_view(self):
        response = self.client.delete(reverse('student-detail', args=[self.student.id]))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())