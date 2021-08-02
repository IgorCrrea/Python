# from bing_image_downloader import downloader
import time
import webbrowser
import pyautogui as pg
import random
import mensagens
import phone_no


def sendmsg():
    for numero in phone_no.num:
        mensagem = "".join(random.choice(mensagens.mensagemlist))
        print(mensagem)

        webbrowser.open('https://web.whatsapp.com/send?phone=' + numero + '&text=' + mensagem)
        time.sleep(18)
        width, height = pg.size()
        pg.click(width / 2, height / 2)
        pg.press('enter')
        time.sleep(5)
        pg.hotkey("ctrl", "w")

def sendgroup():
    mensagem = "".join(random.choice(mensagens.mensagemlist))
    print(mensagem)

    webbrowser.open('https://web.whatsapp.com/accept?code=FmtrKkHDL5a546lzwyxijE')
    time.sleep(18)
    width, height = pg.size()
    pg.click(width / 2, height / 2)
    pg.typewrite(f"{mensagem} \n")
    time.sleep(5)
    pg.hotkey("ctrl", "w")



sendmsg()
sendgroup()
