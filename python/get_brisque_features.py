from utils import compute_image_mscn_transform, extract_subband_feats

import numpy as np
import cv2
import glob

# Matlab Interpolation Implementation in Python
from imresize import imresize



def brisque(image):
    y_mscn = compute_image_mscn_transform(image)
    half_scale = imresize(image, scalar_scale = 0.5, method = 'bicubic')
    y_half_mscn = compute_image_mscn_transform(half_scale)
    feats_full = extract_subband_feats(y_mscn)
    feats_half = extract_subband_feats(y_half_mscn)
    return np.concatenate((feats_full, feats_half))
    
    
files = sorted(glob.glob("../test_images/*.png"))
for file in files:
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype(np.float64)
    feats = brisque(img)
    print("Brisque Featues computed for :",file)
    np.set_printoptions(precision=4)
    print(feats)

