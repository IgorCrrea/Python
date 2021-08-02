from bing_image_downloader import downloader
from what_Image_by_pywhatkit import sendwhats_image
import random
import mensagens
import phone_no

limite = 20  # Quantidade de imagens a serem baixadas.

def baixarfotos():
    # Baixa imagens do Bing
    downloader.download(query="GoodMorning .jpg", limit=limite, output_dir='dataset',
                        force_replace=True, timeout=60)
    
def send_Img():
    
    for numero in phone_no.num:
        img = random.randrange(1, limite + 1)
        mensagem = "".join(random.choice(mensagens.mensagemlist))
        url = f"D:\Estudos\Programação\wpp_img\dataset\Img\Image_{img}.jpg"
        print(mensagem)
        sendwhats_image(numero, url, mensagem, 7, True, 3)

baixarfotos()
#send_Img()




