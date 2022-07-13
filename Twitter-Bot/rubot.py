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
        

