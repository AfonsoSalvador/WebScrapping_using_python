import os
from weakref import ref 
import tweepy
from datetime import datetime
import time
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

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(acess_token, acess_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


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
        if(len(tags)<3):
            return None

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
        if(len(tags)<20):
            return None

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



def main():


    if((datetime.now().time().hour==13)and(datetime.now().time().minute==5)):
        refeicao= meal()
        refeicao = get_Meal(1)
        if(refeicao):
            if(len(refeicao.Acompanhamento+refeicao.Guarnicao+refeicao.Opcao+refeicao.Prato+refeicao.Salada+refeicao.Sobremesa)>160):
                tweet1 = "O almoço de hoje é:\n\nPara salada🥗:\n" + refeicao.Salada + "\n\nPrato principal🍽️:\n" + refeicao.Prato + "\n\n Opção🍽️:\n" + refeicao.Opcao + "\n1/2"
                tweet2 = "Acompanhamento🥣:\n" + refeicao.Acompanhamento + "\n\nGuarnição🌿:\n" + refeicao.Guarnicao,"\n\nSobremesa🍎:\n" + refeicao.Sobremesa + "\n2/2"
                api.update_status(tweet1)
                api.update_status(tweet2)
            else:
                tweet = "O almoço de hoje é:\n\nPara salada🥗:\n" + refeicao.Salada + "\n\nPrato principal🍽️:\n" + refeicao.Prato + "\n\n Opção🍽️:\n" + refeicao.Opcao + "\n\nAcompanhamento🥣:\n" + refeicao.Acompanhamento + "\n\nGuarnição🌿:\n" + refeicao.Guarnicao,"\n\nSobremesa🍎:\n" + refeicao.Sobremesa
                api.update_status(tweet)
            time.sleep(120)

    if((datetime.now().time().hour==15)and(datetime.now().time().minute==00)):
        refeicao= meal()
        refeicao = get_Meal(2)
        if(refeicao):
            if(len(refeicao.Acompanhamento+refeicao.Guarnicao+refeicao.Opcao+refeicao.Prato+refeicao.Salada+refeicao.Sobremesa)>161):
                tweet1 = "A janta de hoje é:\n\nPara salada🥗:\n" + refeicao.Salada + "\n\nPrato principal🍽️:\n" + refeicao.Prato + "\n\n Opção🍽️:\n" + refeicao.Opcao + "\n1/2"
                tweet2 = "Acompanhamento🥣:\n" + refeicao.Acompanhamento + "\n\nGuarnição🌿:\n" + refeicao.Guarnicao,"\n\nSobremesa🍎:\n" + refeicao.Sobremesa + "\n2/2"
                api.update_status(tweet1)
                api.update_status(tweet2)
            else:
                tweet = "A janta de hoje é:\n\nPara salada🥗:\n" + refeicao.Salada + "\n\nPrato principal🍽️:\n" + refeicao.Prato + "\n\n Opção🍽️:\n" + refeicao.Opcao + "\n\nAcompanhamento🥣:\n" + refeicao.Acompanhamento + "\n\nGuarnição🌿:\n" + refeicao.Guarnicao,"\n\nSobremesa🍎:\n" + refeicao.Sobremesa
                api.update_status(tweet)
            time.sleep(120)
        

    return 0


if __name__ == "__main__":
    while True:
        main()
        time.sleep(30)

        #Weekend check
        if(datetime.today().weekday()==5):
            time.sleep(172800)