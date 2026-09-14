import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir('chemin vers le repertoire qui contient les images')

fd = open('img_xxxx.dat', 'rb') # xxxx = numéro de l'image à afficher
b = fd.read()
fd.close()

img=np.empty((320,240), dtype=np.uint8)

for n in range(len(b)):
    img[n%320,n//320]=b[n]

plt.xticks([])
plt.yticks([])
plt.imshow(img, cmap='gray')
