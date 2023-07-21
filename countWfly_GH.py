# -*- coding: utf-8 -*-
"""
Created on Jan 22 17:56:23 2022

@author: juanmir
"""
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import sys

# Get the path to the input image from command-line arguments
input_image_path = sys.argv[1]
output_image_path = sys.argv[2]

# import the image
img = plt.imread(input_image_path)
img_copy = img.copy().astype("float")
img_copy.shape

# set parameters
boxHalfRef = 18
percentile = 0.15
percentileBlue = 0.01

# fly's centroid coordinates: 512,1432
matref = img_copy[512-boxHalfRef:512+boxHalfRef, 1432-boxHalfRef:1432+boxHalfRef, 0:3]# using quantiles

# compute percentiles
Qrefred =  np.quantile(matref[:,:,0], percentile)
Qrefgreen = np.quantile(matref[:,:,1], percentile)
Qrefblue = np.quantile(matref[:,:,2], percentileBlue) # lower because of shadow

#### using percentiles
buffer = 18
boxHalfWindowforNA = boxHalfRef+buffer
whiteflyAmount = 0
for i in np.arange(boxHalfRef, img_copy.shape[0] - boxHalfRef):
    print(i)
    for j in np.arange(boxHalfRef, img_copy.shape[1] - boxHalfRef):

        testedDist = img_copy[i-boxHalfRef:i+boxHalfRef, j-boxHalfRef:j+boxHalfRef, 0:3]

        if np.argwhere(np.isnan(img_copy[i-boxHalfWindowforNA:i+boxHalfWindowforNA, j-boxHalfWindowforNA:j+boxHalfWindowforNA, 0])).shape[0] == 0:  # jump a window having a fly (i.e., there are many NAs)
            if ((np.quantile(testedDist[:,:,0], percentile+0.35) >= Qrefred) and (np.quantile(testedDist[:,:,1], percentile+0.35) >= Qrefgreen) and (np.quantile(testedDist[:,:,2], percentileBlue+0.95) >= Qrefblue)):
                img_copy[i-boxHalfRef:i+boxHalfRef, j-boxHalfRef:j+boxHalfRef, 0:3] = np.nan
                whiteflyAmount = whiteflyAmount + 1
                print(whiteflyAmount, "flies")
                continue
        else:
            continue

print(whiteflyAmount, "flies in total")
# save as an image
a = np.array(img_copy, dtype=np.uint8)
img = Image.fromarray(a, 'RGB')
img.save(output_image_path)
