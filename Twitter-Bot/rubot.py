import os
from weakref import ref
import tweepy
from datetime import datetime
import email
import smtplib
import time
import dotenv
import requests
from bs4 import BeautifulSoup, Tag

# --------------------------------------------------------------
# APPLYING DOTENV
# --------------------------------------------------------------
dotenv.load_dotenv(dotenv.find_dotenv())


# --------------------------------------------------------------
# STARTING UP TWEEPY
# --------------------------------------------------------------
api_key = os.getenv("api_key")
api_key_secret = os.getenv("api_key_secret")
acess_token = os.getenv("acess_token")
acess_token_secret = os.getenv("acess_token_secret")

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(acess_token, acess_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# --------------------------------------------------------------
# STARTING UP EMAIL ALERT SYSTEM
# --------------------------------------------------------------

SENDER = os.getenv("email_sender")
RECEIVER = os.getenv("email_reciever")
APP_PASSWORD = os.getenv("app_password")
SUBJECT = "RuBot alert"
BODY = "<h3>Alerta de erro RuBot</h3><br>Esta foi a mensagem de erro encontrada:<br>"

def send_email(error_text):
    msg = email.message.Message()
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
    msg['To'] = RECEIVER
    password = APP_PASSWORD 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(BODY + error_text)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print(f'Email enviado para {RECEIVER}')

# --------------------------------------------------------------
# Collecting and treating Menu information
# --------------------------------------------------------------

class meal(object):
    Salada = []
    Prato = []
    Opcao = []
    Acompanhamento = []
    Guarnicao = []
    Sobremesa = []


def get_Meal(meal_num):

    content = requests.get('https://ru.ufes.br/cardapio').text
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('p')
    refeicao = meal()

    try:

        if(meal_num == 1):
            # treating the possibility that the site doesnt have such informaton
            if(len(tags) < 9):
                return None

            i = 0

            while "Salada" not in tags[i].text:
                i += 1
            i += 1

            # SALAD OPTIONS
            refeicao.Salada = tags[i].text
            i += 1
            while "Prato Principal" not in tags[i].text:
                refeicao.Salada = refeicao.Salada + "\n"+tags[i].text
                i += 1

            # MAIN DISH
            i += 1
            refeicao.Prato = tags[i].text
            i += 1
            while "Opção" not in tags[i].text:
                refeicao.Prato = refeicao.Prato + "\n"+tags[i].text
                i += 1

            # VEGETARIAN OPTION
            i += 1
            refeicao.Opcao = tags[i].text
            i += 1
            while "Acompanhamento" not in tags[i].text:
                refeicao.Opcao = refeicao.Opcao + "\n"+tags[i].text
                i += 1

            # SIDE DISH
            i += 1
            refeicao.Acompanhamento = tags[i].text
            i += 1
            while "Guarnição" not in tags[i].text:
                refeicao.Opcao = refeicao.Opcao + "\n"+tags[i].text
                i += 1

            i = i+1
            refeicao.Guarnicao = tags[i].text
            i += 1
            while "Sobremesa" not in tags[i].text:
                refeicao.Guarnicao = refeicao.Guarnicao + "\n"+tags[i].text
                i += 1

            i += 1
            refeicao.Sobremesa = tags[i].text
            i += 1
            while "*" not in tags[i].text:
                refeicao.Sobremesa = refeicao.Sobremesa + "\n"+tags[i].text
                i += 1

            return refeicao

        if (meal_num == 2):
            # treating the possibility that the site doesnt have such informaton
            if(len(tags) < 20):
                return None

            i = 0
            while "Salada" not in tags[i].text:
                i += 1
            i += 1

            while "Salada" not in tags[i].text:
                i += 1
            i += 1

            # SALAD OPTIONS
            refeicao.Salada = tags[i].text
            i += 1
            while "Prato Principal" not in tags[i].text:
                refeicao.Salada = refeicao.Salada + "\n"+tags[i].text
                i += 1

            # MAIN DISH
            i += 1
            refeicao.Prato = tags[i].text
            i += 1
            while "Opção" not in tags[i].text:
                refeicao.Prato = refeicao.Prato + "\n"+tags[i].text
                i += 1

            # VEGETARIAN OPTION
            i += 1
            refeicao.Opcao = tags[i].text
            i += 1
            while "Acompanhamento" not in tags[i].text:
                refeicao.Opcao = refeicao.Opcao + "\n"+tags[i].text
                i += 1

            # SIDE DISH
            i += 1
            refeicao.Acompanhamento = tags[i].text
            i += 1
            while "Guarnição" not in tags[i].text:
                refeicao.Opcao = refeicao.Opcao + "\n"+tags[i].text
                i += 1

            i = i+1
            refeicao.Guarnicao = tags[i].text
            i += 1
            while "Sobremesa" not in tags[i].text:
                refeicao.Guarnicao = refeicao.Guarnicao + "\n"+tags[i].text
                i += 1

            i += 1
            refeicao.Sobremesa = tags[i].text
            i += 1
            while "*" not in tags[i].text:
                refeicao.Sobremesa = refeicao.Sobremesa + "\n"+tags[i].text
                i += 1

            return refeicao

    except Exception as error:
        send_email(error)
        return None




def tweet_meal(refeicao, num_refeicao):
    if(num_refeicao == 1):
        if(len(refeicao.Acompanhamento+refeicao.Guarnicao+refeicao.Opcao+refeicao.Prato+refeicao.Salada+refeicao.Sobremesa) > 156):
            tweet1 = "O almoço de hoje é:\n\nPara salada🥗:\n" + refeicao.Salada + "\n\nPrato principal🍽️:\n" + refeicao.Prato + "\n\nOpção🍽️:\n" + refeicao.Opcao + "\n1/2\n"
            tweet2 = "Acompanhamento🥣:\n" + refeicao.Acompanhamento + "\n\nGuarnição🌿:\n" + refeicao.Guarnicao + "\n\nSobremesa🍎:\n" + refeicao.Sobremesa + "\n2/2"
            api.update_status(tweet2)
            api.update_status(tweet1)
            #print(tweet1)
            #print(tweet2)
            print("Almoço tweetado com sucesso!\n")
        else:
            tweet = "O almoço de hoje é:\n\nPara salada🥗:\n" + refeicao.Salada + "\n\nPrato principal🍽️:\n" + refeicao.Prato + "\n\nOpção🍽️:\n" + refeicao.Opcao + "\n\nAcompanhamento🥣:\n" + refeicao.Acompanhamento + "\n\nGuarnição🌿:\n" + refeicao.Guarnicao + "\n\nSobremesa🍎:\n" + refeicao.Sobremesa
            api.update_status(tweet)
            #print(tweet)
            print("Almoço tweetado com sucesso!\n")
        time.sleep(120)
    elif(num_refeicao==2):
        if(len(refeicao.Acompanhamento+refeicao.Guarnicao+refeicao.Opcao+refeicao.Prato+refeicao.Salada+refeicao.Sobremesa)>157):
            tweet1 = "A janta de hoje é:\n\nPara salada🥗:\n" + refeicao.Salada + "\n\nPrato principal🍽️:\n" + refeicao.Prato + "\n\nOpção🍽️:\n" + refeicao.Opcao + "\n1/2"
            tweet2 = "Acompanhamento🥣:\n" + refeicao.Acompanhamento + "\n\nGuarnição🌿:\n" + refeicao.Guarnicao + "\n\nSobremesa🍎:\n" + refeicao.Sobremesa + "\n2/2"
            api.update_status(tweet2)
            api.update_status(tweet1)
            #print(tweet1)
            #print(tweet2)
            print("Janta tweetada com sucesso!\n")
        else:
            tweet = "A janta de hoje é:\n\nPara salada🥗:\n" + refeicao.Salada + "\n\nPrato principal🍽️:\n" + refeicao.Prato + "\n\nOpção🍽️:\n" + refeicao.Opcao + "\n\nAcompanhamento🥣:\n" + refeicao.Acompanhamento + "\n\nGuarnição🌿:\n" + refeicao.Guarnicao+"\n\nSobremesa🍎:\n" + refeicao.Sobremesa
            api.update_status(tweet)
            #print(tweet)
            print("Janta tweetada com sucesso!\n")
        time.sleep(120)


                

def main():

    if((datetime.now().time().hour==12)and(datetime.now().time().minute==00)):
        refeicao= meal()
        refeicao = get_Meal(1)
        if(refeicao):
            tweet_meal(refeicao, 1)
        else:
            print("Nao encontrei, esperando uma horinha")
            time.sleep(3600)
            refeicao = get_Meal(1)
            if(refeicao):
                api.update_status("Desculpa pela demora pessoal! Aqui está o almoço de agora!")
                #print("Desculpa pela demora pessoal! Aqui está o almoço de agora!")
                tweet_meal(refeicao, 1)
            else:
                api.update_status("Não encontrei o almoço no site hoje pessoal :(")
                print("ERROR: Lunch not found")

    if((datetime.now().time().hour==19)and(datetime.now().time().minute==00)):
        refeicao= meal()
        refeicao = get_Meal(2)
        if(refeicao):
            tweet_meal(refeicao, 2)
        else:
            print("Nao encontrei, esperando uma horinha")
            time.sleep(3600)
            refeicao = get_Meal(2)
            if(refeicao):
                api.update_status("Desculpa pela demora pessoal! Aqui está a janta de agora!")
                #print("Desculpa pela demora pessoal! Aqui está a janta de agora!")
                tweet_meal(refeicao, 2)
            else:
                api.update_status("Não encontrei a janta no site hoje pessoal :(")
                print("ERROR: Dinner not found")

    return 0


if __name__ == "__main__":
    while True:
        
        # Weekend check
        if(datetime.today().weekday()==5 or datetime.today().weekday()==6):
            print("Indo dormir para o final de semana, até lá!")
            time.sleep(28800)
            print("Acordei!")
        else:
            main()
            time.sleep(30)