import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import User


# Create your views here.

class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        print(jd)
        User.objects.create(name=jd['name'], email=jd['email'], password=jd['password'])
        data = {'status': 200, 'message': 'Usuario cadastrado com sucesso'}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        user = list(User.objects.filter(id=id).values())
        username = jd['name']
        if (len(user) > 0):
            useredit = User.objects.get(id=id)
            if (jd['name'] != ""):
                useredit.name = jd['name']
            if (jd['email'] != ""):
                useredit.email = jd['email']
            if (jd['password'] != ""):
                useredit.password = jd['password']
            useredit.save()
            data = {'status': 200, 'message': 'Usuario ' + username + ' editado com sucesso'}
        else:
            data = {'status': 404, 'message': 'não foi possivel encontrar o usuario'}

        return JsonResponse(data)

    def delete(self, request, id):
        user = list(User.objects.filter(id=id).values())
        if (len(user) > 0):
            User.objects.filter(id=id).delete()
            data = {'status': 200, 'message': 'Usuario deletado com sucesso'}
        else:
            data = {'status': 404, 'message': 'não foi possivel encontrar o usuario'}

        return JsonResponse(data)
