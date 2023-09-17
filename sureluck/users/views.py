from django.http import JsonResponse
from django.views import View
from .models import User
# Create your views here.

class UserView(View):

    def get(self,request):
        users= list(User.objects.values('id','name','email'))
        if(len(users)>0):
            data = {'status':200, 'message':'Usuarios encontrados','users':users}
        else:
            data = {'status':200, 'message':'não foi possivel encontrar nenhum usuario', 'users':users}
        return JsonResponse(data)
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass
