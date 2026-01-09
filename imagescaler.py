from PIL import Image
from random import randint
import os
cwd = os.getcwd
print(cwd)
id = randint(1, 213769)
imgformat = input("what is the file name: ")
scaleimg_name = f"{imgformat}"

print(imgformat)

imgname = f"image{id}.png"
# Wczytaj obraz (dowolny format)
img = Image.open(scaleimg_name)  # tutaj dowolny plik
nowa_wys = 400
# Nowa wysokość
w, h = img.size
# Oblicz proporcjonalną wysokość
nowa_szer = int(w / h * nowa_wys)

# Zmień rozmiar
img = img.resize((nowa_szer, nowa_wys))


# Zapisz jako PNG (automatyczne konwertowanie)
img.save(imgname, format="PNG")
