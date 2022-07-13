from asyncio.windows_events import NULL
import os 
import tweepy
import time
import random
import dotenv
import requests
from bs4 import BeautifulSoup

#--------------------------------------------------------------
# APPLYING DOTENV
#--------------------------------------------------------------
dotenv.load_dotenv(dotenv.find_dotenv())


#--------------------------------------------------------------
# STARTING UP TWEEPY
#--------------------------------------------------------------
api_key = os.getenv("api_key")
api_key_secret = os.getenv("api_key_secret")
acess_token = os.getenv("acess_token")
acess_token_secret = os.getenv("acess_token_secret")

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
auth.set_access_token(acess_token, acess_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify=True)


#--------------------------------------------------------------
# Collecting and treating Menu information
#--------------------------------------------------------------

class meal(object):
    Salada = []
    Prato = []
    Opcao = []
    Acompanhamento = []
    Guarnicao = []
    Sobremesa = []

def get_Meal(meal_num):

    content = requests.get('https://ru.ufes.br/cardapio').text
    soup = BeautifulSoup(content,'lxml')
    tags = soup.find_all('p')
    refeicao = meal()

    if(meal_num==1):
        #trating the possibility that the site doesnt have such informaton
        if(len(tags)>3):
            return NULL

        i=0

        while tags[i].text != "Salada":
            i +=1
        i +=1

        #SALAD OPTIONS
        refeicao.Salada = tags[i].text
        i +=1
        while tags[i].text != "Prato Principal":
            refeicao.Salada = refeicao.Salada + "\n"+tags[i].text
            i +=1

        #MAIN DISH
        i +=1
        refeicao.Prato = tags[i].text

        #VEGETARIAN OPTION
        i +=2
        refeicao.Opcao = tags[i].text

        
        i=i+2
        refeicao.Acompanhamento = tags[i].text

        i=i+2
        refeicao.Guarnicao= tags[i].text

        i=i+2
        refeicao.Sobremesa = tags[i].text
        i +=1
        while tags[i].text != "*cardápio sujeito a alterações":
            refeicao.Sobremesa = refeicao.Sobremesa + "\n"+tags[i].text
            i +=1

        return refeicao
    
    if (meal_num==2):
        #trating the possibility that the site doesnt have such informaton
        if(len(tags)>20):
            return NULL

        i=0
        while tags[i].text != "Salada":
            i +=1
        i +=1

        while tags[i].text != "Salada":
            i +=1
        i +=1

        #SALAD OPTIONS
        refeicao.Salada = tags[i].text
        i +=1
        while tags[i].text != "Prato Principal":
            refeicao.Salada = refeicao.Salada + "\n"+tags[i].text
            i +=1

        #MAIN DISH
        i +=1
        refeicao.Prato = tags[i].text

        #VEGETARIAN OPTION
        i +=2
        refeicao.Opcao = tags[i].text

        i=i+2
        refeicao.Acompanhamento = tags[i].text

        i=i+2
        refeicao.Guarnicao= tags[i].text

        i=i+2
        refeicao.Sobremesa = tags[i].text
        i +=1
        while tags[i].text != "*cardápio sujeito a alterações":
            refeicao.Sobremesa = refeicao.Sobremesa + "\n"+tags[i].text
            i +=1

        return refeicao



