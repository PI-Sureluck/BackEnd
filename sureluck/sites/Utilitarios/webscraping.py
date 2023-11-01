from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class WebScraping:
    def webscraping(self):
        service = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=service)

# Crie uma instância da classe WebScraping
scraper = WebScraping()

# Chame o método webscraping
scraper.webscraping()

print("teste")