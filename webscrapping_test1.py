from random import gauss
from bs4 import BeautifulSoup
import requests

content = requests.get('https://ru.ufes.br/cardapio').text

soup = BeautifulSoup(content, 'lxml')
tags = soup.find_all('p')

SaladaA = []
PratoPA = []
OpcaoA = []
AcompanhamentoA = []
GuarnicaoA = []
SobremesaA = []

SaladaJ = []
PratoPJ = []
OpcaoJ = []
AcompanhamentoJ = []
GuarnicaoJ = []
SobremesaJ = []

i=4

SaladaA = tags[3].text
while tags[i].text != "Prato Principal":
    SaladaA = SaladaA + "\n "+tags[i].text
    i = i+1

i=i+1
PratoPA = tags[i].text
i=i+2
OpcaoA = tags[i].text
i=i+2
AcompanhamentoA = tags[i].text
i=i+2
GuarnicaoA = tags[i].text
i=i+2
SobremesaA = tags[i].text


#Inicia leitura da Janta
i = i+5
SaladaJ = tags[18].text
while tags[i].text != "Prato Principal":
    SaladaJ = SaladaJ + "\n "+tags[i].text
    i = i+1

i=i+1
PratoPJ = tags[i].text
i=i+2
OpcaoJ = tags[i].text
i=i+2
AcompanhamentoJ = tags[i].text
i=i+2
GuarnicaoJ = tags[i].text
i=i+2
SobremesaJ = tags[i].text

print("Os pratos do almoço de hoje são:\n\nPara salada:\n",SaladaA,"\n\nPrato principal:\n",PratoPA, "\n\n Opção:\n",
OpcaoA,"\n\nAcompanhamento:\n",AcompanhamentoA,"\n\nGaurnição:\n",GuarnicaoA,"\n\nSobremesa:\n",SobremesaA)


print("\n\n\nOs pratos da Janta de hoje são:\n\nPara salada:\n",SaladaJ,"\n\nPrato principal:\n",PratoPJ, "\n\n Opção:\n",
OpcaoJ,"\n\nAcompanhamento:\n",AcompanhamentoJ,"\n\nGaurnição:\n",GuarnicaoJ,"\n\nSobremesa:\n",SobremesaJ)