import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Site


# Create your views here.

class SiteView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            site = list(Site.objects.filter(id=id).values())
            if (len(site) > 0):
                data = {'status': 200, 'message': 'Site encontrado', 'site': site}
            else:
                data = {'status': 404, 'message': 'não foi possivel encontrar o site'}
        else:
            sites = list(Site.objects.values('id', 'name', 'link', 'logo', 'xpath'))
            if (len(sites) > 0):
                data = {'status': 200, 'message': 'Sites encontrados', 'sites': sites}
            else:
                data = {'status': 404, 'message': 'não foi possivel encontrar nenhum site'}
        return JsonResponse(data)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        print(jd)
        Site.objects.create(name=jd['name'], link=jd['link'], logo=jd['logo'],xpath=jd['xpath'])
        data = {'status': 200, 'message': 'Site cadastrado com sucesso'}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        site = list(Site.objects.filter(id=id).values())
        sitename = jd['name']
        if (len(site) > 0):
            siteedit = Site.objects.get(id=id)
            if (jd['name'] != ""):
                siteedit.name = jd['name']
            if (jd['link'] != ""):
                siteedit.link = jd['link']
            if (jd['logo'] != ""):
                siteedit.logo = jd['logo']
            if (jd['xpath'] != ""):
                siteedit.xpath = jd['xpath']
            siteedit.save()
            data = {'status': 200, 'message': 'Site ' + sitename + ' editado com sucesso'}
        else:
            data = {'status': 404, 'message': 'não foi possivel encontrar o site'}

        return JsonResponse(data)

    def delete(self, request, id):
        site = list(Site.objects.filter(id=id).values())
        if (len(site) > 0):
            Site.objects.filter(id=id).delete()
            data = {'status': 200, 'message': 'Site deletado com sucesso'}
        else:
            data = {'status': 404, 'message': 'não foi possivel encontrar o site'}

        return JsonResponse(data)

