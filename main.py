
# coding: utf-8

# In[1]:

from optparse import OptionParser
import cv2
import numpy as np
import os


# In[6]:

def separate_img(img,n,hi,wi):
    h,w,ch = img.shape
    h0 = int(h * hi / n)
    h1 = int(h * (hi+1)/n)
    w0 = int(w * wi / n)
    w1 = int(w * (wi+1)/ n)
    img2 = img[h0:h1,w0:w1]
    return img2


# In[10]:

def separate_folder(folder, n):
    newfolder = folder + "2"
    os.makedirs(newfolder,exist_ok = True)
    files = os.listdir(folder)
    for file in files:
        print(file)
        fpath = os.path.join(folder, file)
        img = cv2.imread(fpath)
        for hi in range(n):
            for wi in range(n):
                img2 = separate_img(img, n, hi, wi)
                newfpath = os.path.join(newfolder, file.split(".")[0] + "_" + str(hi) + "_" + str(wi) + "." + file.split(".")[1])
                cv2.imwrite(newfpath, img2)


# In[12]:

def main():
    parser = OptionParser()
    parser.add_option(
        "-d","--dataset",
        help="folder directory of trimming",
        dest="root")
    parser.add_option(
        "-n","--number",
        type="int",
        help = "trimming number",
        dest="n"
        )
    (opt, args) = parser.parse_args()
    separate_folder(opt.root, opt.n)


if __name__ == '__main__':
    main()
