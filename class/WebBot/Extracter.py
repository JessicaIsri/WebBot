import re
import os

directory = 'E:\\FATEC\\PI\\Files\\frags'
path = os.listdir(directory)
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
                cep = line[674:682]
                cnpj = line[3:18]
                cidade = line[688:738]
                if cidade == 'SAO JOSE DOS CAMPOS':
                    pass
                # print(cnpj, cep)
            except:
                print("Não possui o dado requirido")






