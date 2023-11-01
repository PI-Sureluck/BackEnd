from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from ..models import *


class WebScraping:
    def webscraping(self):
        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get("https://pt.egamersworld.com/bets")

        driver.find_element('xpath', '/html/body/main/div[1]/div[3]')

        games = driver.find_element('xpath', '/html/body/main/div[1]/div[3]').find_elements('class name',
                                                                                            'item_item__e0cZG')
        for game in games:
            divs = game.find_elements('tag name', 'div')

            namesite = divs[0].find_element('tag name', 'a').find_element('tag name', 'img').get_attribute('title')
            timeA = divs[1].text
            oddA = divs[2].text
            oddB = divs[3].text
            timeB = divs[4].text

            nameevent = f"{timeA}vs{timeB}"
            site, created = Site.objects.get_or_create(name=namesite,defaults={'link': 'None', 'logo': 'None', 'xpath': 'None'})
            event, created = Event.objects.get_or_create(name=nameevent, date="2023-11-01", teamA=timeA, teamB=timeB)
            oddA, created = Odds.objects.update_or_create(site=site,event=event,team=timeA,defaults={'odd': oddA})
            oddB, created = Odds.objects.update_or_create(site=site,event=event,team=timeB,defaults={'odd': oddB})
        driver.close()
        return 0