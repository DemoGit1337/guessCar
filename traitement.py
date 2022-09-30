import numpy as np
from PIL import Image


def traitement_images(nom_fichier):
    img = Image.open(nom_fichier) 
    img = img.resize((224, 224)) 

    r, g, b = img.split() 
    img = Image.merge("RGB", (b, g, r)) 

    img = np.asarray(img, dtype = float) 

    
    for i in range(224):
        for j in range(224):
            img[i,j] = (img[i,j,0] - 103.939, img[i,j,1] - 116.779, img[i,j,2] - 123.68)

    
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    return(img)

