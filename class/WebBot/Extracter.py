import re
import os
import json
from DataBase import *

directory = 'E:\\FATEC\\PI\\Files\\frags'
path = os.listdir(directory)
db = DataBase
for files in path:
    print(files)
    file = open(directory+'\\'+files)
    for line in file:
        text = line.split(' ')
        c = line
        pos = text[0].find('F')
        # print(pos)
        if pos == 1:
            try:
                #obtem o valor da cidade
                cidade = line[688:738]

                #especifica por dados provinientes de são jose
                if cidade == 'SAO JOSE DOS CAMPOS':
                    cep = line[674:682]
                    cnpj = line[3:18]
                    #cria o json a ser inserido
                    empresa = {'cnpj': cnpj, 'cep': cep, 'cidade': cidade}

                    #insere o json no banco
                    db.insertOne(empresa)
            except:
                print("Não possui o dado requirido")






