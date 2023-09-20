import json

from django.utils.dateparse import parse_date
from rest_framework import viewsets

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import *


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
        Site.objects.create(name=jd['name'], link=jd['link'], logo=jd['logo'], xpath=jd['xpath'])
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


class EventView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            event = list(Event.objects.filter(id=id).values())
            if (len(event) > 0):
                data = {'status': 200, 'message': 'Event encontrado', 'event': event}
            else:
                data = {'status': 404, 'message': 'não foi possivel encontrar o event'}
        else:
            events = list(Event.objects.values())
            if (len(events) > 0):
                data = {'status': 200, 'message': 'Events encontrados', 'events': events}
            else:
                data = {'status': 404, 'message': 'não foi possivel encontrar nenhum event'}
        return JsonResponse(data)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        print(jd)
        data_evento_str = jd['date']
        data_evento = parse_date(data_evento_str)
        Event.objects.create(name=jd['name'], date=data_evento, teamA=jd['teamA'], teamB=jd['teamB'])
        data = {'status': 200, 'message': 'Evento criado com sucesso'}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        event = list(Event.objects.filter(id=id).values())
        eventname = jd['name']
        print("entrou no certo" + eventname)
        if (len(event) > 0):
            eventedit = Event.objects.get(id=id)
            if (jd['name'] != ""):
                eventedit.name = jd['name']
            if (jd['teamA'] != ""):
                eventedit.teamA = jd['teamA']
            if (jd['teamB'] != ""):
                eventedit.teamB = jd['teamB']
            if (jd['date'] != ""):
                eventedit.date = parse_date(jd['date'])
            eventedit.save()
            data = {'status': 200, 'message': 'Evento ' + eventname + ' editado com sucesso'}
        else:
            data = {'status': 404, 'message': 'não foi possivel encontrar o evento'}

        return JsonResponse(data)

    def delete(self, request, id):
        evento = list(Event.objects.filter(id=id).values())
        if (len(evento) > 0):
            Event.objects.filter(id=id).delete()
            data = {'status': 200, 'message': 'Evento deletado com sucesso'}
        else:
            data = {'status': 404, 'message': 'não foi possivel encontrar o evento'}

        return JsonResponse(data)

class OddsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            odd = list(Odds.objects.filter(id=id).values())
            if (len(odd) > 0):
                data = {'status': 200, 'message': 'Odds encontrado', 'odd': odd}
            else:
                data = {'status': 404, 'message': 'não foi possivel encontrar o odd'}
        else:
            odds = list(Odds.objects.values())
            if (len(odds) > 0):
                data = {'status': 200, 'message': 'Odds encontrados', 'odds': odds}
            else:
                data = {'status': 404, 'message': 'não foi possivel encontrar nenhuma odd'}
        return JsonResponse(data)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        print(jd)
        site = Site.objects.get(id=jd["site"])
        evento = Event.objects.get(id=jd["event"])
        Odds.objects.create(odd=jd['odd'], site=site, event=evento)
        data = {'status': 200, 'message': 'Odd criado com sucesso'}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        odds = list(Odds.objects.filter(id=id).values())

        if (len(odds) > 0):
            oddsedit = Odds.objects.get(id=id)
            if (jd['odd'] != ""):
                oddsedit.odd = jd['odd']
            if (jd['site'] != ""):
                site = Site.objects.get(id=jd["site"])
                oddsedit.site = site
            if (jd['event'] != ""):
                evento = Event.objects.get(id=jd["event"])
                oddsedit.event = evento

            oddsedit.save()
            data = {'status': 200, 'message': 'Odds editada com sucesso'}
        else:
            data = {'status': 404, 'message': 'não foi possivel encontrar a odd'}

        return JsonResponse(data)

    def delete(self, request, id):
        odd = list(Odds.objects.filter(id=id).values())
        if (len(odd) > 0):
            Odds.objects.filter(id=id).delete()
            data = {'status': 200, 'message': 'Odds deletado com sucesso'}
        else:
            data = {'status': 404, 'message': 'não foi possivel encontrar a odd'}

        return JsonResponse(data)