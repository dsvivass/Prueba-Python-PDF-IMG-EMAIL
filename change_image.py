
#!/usr/bin/env python3

from PIL import Image
import os

os.chdir('./supplier-data/images/')
lista_imgs = os.listdir()

for img in lista_imgs:
    if img != '.DS_Store' and os.path.splitext(img)[1] == '.tiff':
        name, _ = os.path.splitext(img) # Separa el nombre de la extension
        imagen = Image.open(img)
        imagen.convert('RGB').resize((600, 400)).save('{}.jpeg'.format(name))


