---
layer: post
title: "Read file from Zip"
description: ""
category: machine-learning
---


This script show you how to read Image file from Zip folder



```Python
import zipfile
from PIL import Image
import numpy as np
from matplotlib.pyplot import imshow
from scipy.misc import imread
%matplotlib inline

path1 = '/media/lhlong/01D309ADC81A8610/lhlong/ML/work/self/data/CelebA/Img/img_align_celeba.zip'
with zipfile.ZipFile(path1) as zippedImgs:
    for i in range(len(zippedImgs.namelist())):
        print("iter", i, " ")
        file_in_zip = zippedImgs.namelist()[i]
        if (".jpg" in file_in_zip or ".JPG" in file_in_zip): 
            print("Found image: ", file_in_zip.split('/')[1])
            with zippedImgs.open(file_in_zip) as file:
                img = Image.open(file)
                print(img.size, img.mode, len(img.getdata()))
                imshow(img)
            break
        else:
            print("")
```