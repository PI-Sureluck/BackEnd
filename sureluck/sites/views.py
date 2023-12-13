import json

from django.utils import timezone
from django.utils.dateparse import parse_date
from rest_framework import viewsets
from .Utilitarios.Calculadora import Calculadora
from .Utilitarios.webscraping import WebScraping
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
        Odds.objects.create(odd=jd['odd'], site=site, event=evento, team=jd['team'])
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
            if (jd['event'] != ""):
                evento = Event.objects.get(id=jd["team"])
                oddsedit.team = evento

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


class SureBetsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            try:
                surebet = SureBets.objects.get(id=id)
                Porcent = Calculadora.verificarValorApostar(self, surebet.oddA.odd, surebet.oddB.odd)
                surebet_info = {
                    'Id': surebet.id,
                    'TimeA': {
                        "Time": surebet.oddA.team,
                        "Odd": surebet.oddA.odd,
                        "Site": {
                            "Name": surebet.oddA.site.name,
                            "Link": surebet.oddA.site.link
                        },
                        "Event": {
                            "Name": surebet.oddA.event.name,
                            "Date": surebet.oddA.event.date
                        },
                        "Porcent": Porcent[0]
                    },
                    'TimeB': {
                        "Time": surebet.oddB.team,
                        "Odd": surebet.oddB.odd,
                        "Site": {
                            "Name": surebet.oddB.site.name,
                            "Link": surebet.oddB.site.link
                        },
                        "Event": {
                            "Name": surebet.oddB.event.name,
                            "Date": surebet.oddB.event.date
                        },
                        "Porcent": Porcent[1]
                    }
                }
                data = {'status': 200, 'message': 'SureBet encontrado', 'surebet': surebet_info}
            except SureBets.DoesNotExist:
                data = {'status': 404, 'message': 'Não foi possível encontrar a SureBet com o ID fornecido'}
        else:
            surebets = SureBets.objects.all().order_by('-created_at')
            surebet_info_list = []

            now = timezone.now()
            limite_tempo = now - timezone.timedelta(minutes=5)
            print(limite_tempo)
            SureBets.objects.filter(created_at__lt=limite_tempo).delete()

            for surebet in surebets:
                Porcent = Calculadora.verificarValorApostar(self, surebet.oddA.odd, surebet.oddB.odd)
                surebet_info = {
                    'Id': surebet.id,
                    'TimeA': {
                        "Time": surebet.oddA.team,
                        "Odd": surebet.oddA.odd,
                        "Site": {
                            "Name": surebet.oddA.site.name,
                            "Link": surebet.oddA.site.link
                        },
                        "Event": {
                            "Name": surebet.oddA.event.name,
                            "Date": surebet.oddA.event.date
                        },
                        "Porcent": Porcent[0]
                    },
                    'TimeB': {
                        "Time": surebet.oddB.team,
                        "Odd": surebet.oddB.odd,
                        "Site": {
                            "Name": surebet.oddB.site.name,
                            "Link": surebet.oddB.site.link
                        },
                        "Event": {
                            "Name": surebet.oddB.event.name,
                            "Date": surebet.oddB.event.date
                        },
                        "Porcent": Porcent[1]
                    }
                }
                surebet_info_list.append(surebet_info)

            if len(surebet_info_list) > 0:
                data = {'status': 200, 'message': 'SureBets encontrados', 'surebets': surebet_info_list}
            else:
                data = {'status': 404, 'message': 'Não foi possível encontrar nenhuma SureBet'}

        return JsonResponse(data)

    def post(self, request):
        # Lê o JSON do corpo da requisição
        jd = json.loads(request.body)
        print(jd)
        sites = []
        events = []
        for item in jd["site"]:
            print(item)
            sites.append(Site.objects.get(id=item))

        for item in jd["event"]:
            print(item)
            events.append(Event.objects.get(id=item))
        sure_bet = SureBets.objects.create(
            teamA=jd['teamA'],
            teamB=jd['teamB'],
            oddA=jd['oddA'],
            oddB=jd['oddB'],
            profit=jd['profit']
        )
        sure_bet.site.set(sites)
        sure_bet.event.set(events)

        data = {'status': 200, 'message': 'Surebets criado com sucesso'}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        odds = list(Odds.objects.filter(id=id).values())

        if (len(odds) > 0):
            surebetsedit = SureBets.objects.get(id=id)

            profit = jd['profit']
            if (jd['teamA'] != ""):
                surebetsedit.teamA = jd['teamA']
            if (jd['teamB'] != ""):
                surebetsedit.teamB = jd['teamB']
            if (jd['oddA'] != ""):
                surebetsedit.oddA = jd['oddA']
            if (jd['oddB'] != ""):
                surebetsedit.oddB = jd['oddB']
            if (jd['profit'] != ""):
                surebetsedit.profit = jd['profit']

            surebetsedit.save()
            data = {'status': 200, 'message': 'SureBets editada com sucesso'}
        else:
            data = {'status': 404, 'message': 'não foi possivel encontrar a Surebets'}

        return JsonResponse(data)

    def delete(self, request, id):
        odd = list(SureBets.objects.filter(id=id).values())
        if (len(odd) > 0):
            SureBets.objects.filter(id=id).delete()
            data = {'status': 200, 'message': 'Surebets deletado com sucesso'}
        else:
            data = {'status': 404, 'message': 'não foi possivel encontrar a Surebets'}

        return JsonResponse(data)


class ScrepView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        events = Event.objects.all()  # Recupera todos os eventos
        event_data = []  # Lista para armazenar os dados dos eventos e suas odds

        for event in events:
            odds_do_event = Odds.objects.filter(event=event)
            event_odds = {
                "event_name": event.name,
                "teamA": [],
                "teamB": [],
                "surebets": []
            }

            for odds in odds_do_event:
                if event.teamA == odds.team:
                    event_odds["teamA"].append({
                        'team': odds.team,
                        'odd': odds.odd,
                        'site': odds.site.name
                    })
                else:
                    event_odds["teamB"].append({
                        'team': odds.team,
                        'odd': odds.odd,
                        'site': odds.site.name
                    })

            for teamA in event_odds["teamA"]:
                for teamB in event_odds["teamB"]:
                    is_surebet = Calculadora.verificarSureBets(0, teamA['odd'], teamB['odd'])
                    if is_surebet == 1:
                        event_odds["surebets"].append({
                            'teamA': teamA['team'],
                            'teamB': teamB['team'],
                            'odd_teamA': teamA['odd'],
                            'odd_teamB': teamB['odd']
                        })
                        oddA = Odds.objects.get(odd=teamA['odd'], team=teamA['team'], site__name=teamA['site'],
                                                event=event)
                        oddB = Odds.objects.get(odd=teamB['odd'], team=teamB['team'], site__name=teamB['site'],
                                                event=event)
                        # Crie uma instância do modelo SureBets e associe as instâncias de Odds
                        SureBets.objects.create(
                            teamA=oddA.team,
                            teamB=oddB.team,
                            oddA=oddA,
                            oddB=oddB,
                            profit=0
                        )



        return JsonResponse({'status': 200})


class ScrapView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        WebScraping.webscraping(0)
        response = ScrepView.as_view()(request)
        return JsonResponse({'status': 200})