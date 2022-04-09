import os, shutil, datetime
from time import strftime

#origin = "D:/Publica/"

#dest = "D:/Publica2/"


#Teste
origin = "C:/Users/igor.correa/Desktop/Publica/"
dest = "C:/Users/igor.correa/Desktop/Publica2/"
time = datetime.datetime.now()
time = strftime("%I-%M-%S")
#FimTeste

folderList=[
    "TI",
    "Controladoria",
    "RH",
    "Financeiro",
    "Contabilidade",
    "Faturamento",
    "Compras",
    "Fiscal",
    "Porto",
]

def run():
    bkp()
    clear(origin)
    makeDir()

    #Teste
    with open(f"{origin}{time}.txt",'w') as teste:
        teste.write("teste")
    #FimTeste

def clear(dir):

    for the_file in os.listdir(dir):

        file_path = os.path.join(dir, the_file)

        try:
            if os.path.isfile(file_path):
                os.remove(file_path)

            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        except Exception as e:
            print(e)

def makeDir():
    for folder in folderList:
        try:
            os.mkdir(f"{origin}{folder}")
        except Exception as e:
            print(e)

def bkp():
    clear(dest)
    for the_file in os.listdir(origin):

        file_path_origin = os.path.join(origin, the_file)
        file_path_dest = os.path.join(dest, the_file)

        try:
            if os.path.isfile(file_path_origin):
                shutil.copy(file_path_origin, dest)

            elif os.path.isdir(file_path_origin):
                shutil.copytree(file_path_origin, file_path_dest)

        except Exception as e:
            print(e)

run()