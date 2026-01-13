from PIL import Image
from random import randint
import os
cwd = os.getcwd()
print(cwd)

input("Are you sure you want this?")
imgformat = os.listdir(cwd)
imgformat.remove("imagescaler.py")

print(imgformat)

for scaleimg_name in imgformat:

    id = randint(1, 213769)
    imgname = f"image67{id}.png"
    # Wczytaj obraz (dowolny format)
    img = Image.open(scaleimg_name)  # tutaj dowolny plik
    nowa_wys = 1080
    # Nowa wysokość
    w, h = img.size
    # Oblicz proporcjonalną wysokość
    nowa_szer = int(w / h * nowa_wys)

    # Zmień rozmiar
    img = img.resize((nowa_szer, nowa_wys))


    # Zapisz jako PNG (automatyczne konwertowanie)
    img.save(imgname, format="PNG")
