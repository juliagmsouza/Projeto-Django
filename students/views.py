from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Classe para lidar com requisição de listagem de estudantes e cadastro de estudantes
class StudentCreateAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()

        # Aplica filtros de nome, curso e data de nascimento, se fornecidos
        nome = self.request.query_params.get('nome', None)
        curso = self.request.query_params.get('curso', None)
        data_nascimento = self.request.query_params.get('data_nascimento', None)

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if curso:
            queryset = queryset.filter(curso__icontains=curso)
        if data_nascimento:
            queryset = queryset.filter(data_nascimento=data_nascimento)

        return queryset

# Classe para lidar com atualização, detalhamento e remoção de estudantes
class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Classe para lidar com o cadastro de novos usuários no sistema
class CreateUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Verifica se recebeu username e senha
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=400)

        # Verifica se o user name já foi utilizado
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already taken'}, status=400)

        # Cria usuário
        user = User.objects.create_user(username=username, password=password)

        return Response({}, status=201)