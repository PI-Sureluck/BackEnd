import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .models import User
from .serializers import UserSerializer
import jwt, datetime

# Create your views here.


class Register(APIView):
    def get(self, request, id=0):
        if (id > 0):
            user = list(User.objects.filter(id=id).values())
            if (len(user) > 0):
                data = {'status': 200, 'message': 'Usuario encontrado', 'user': user}
            else:
                data = {'status': 404, 'message': 'não foi possivel encontrar o usuario'}
        else:
            users = list(User.objects.values('id', 'name', 'email'))
            if (len(users) > 0):
                data = {'status': 200, 'message': 'Usuarios encontrados', 'users': users}
            else:
                data = {'status': 404, 'message': 'não foi possivel encontrar nenhum usuario', 'users': users}
        return JsonResponse(data)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        user = list(User.objects.filter(id=id).values())
        if (len(user) > 0):
            User.objects.filter(id=id).delete()
            data = {'status': 200, 'message': 'Usuario deletado com sucesso'}
        else:
            data = {'status': 404, 'message': 'não foi possivel encontrar o usuario'}

        return JsonResponse(data)

class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Algo deu errado')

        if not user.check_password(password):
            raise AuthenticationFailed('Algo deu errado')

        payload = {
            'id' : user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response =Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'jwt': token
        }
        return response


class UserView(APIView):

    def get(self,request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Algo deu errado')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Algo deu errado')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {
            'message' : 'success'
        }
        return response



