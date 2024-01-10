from os import listdir
from os.path import isfile, join
import numpy as np
import cv2 as cv

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
        
    v = mx*100
    return h, s, v

# Kelas Matang
mypath="resize/matang"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
img = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  img[n] = cv.imread( join(mypath,onlyfiles[n]) )
  
  B1, G1, R1 = img[n][200,300]
  h1, s1, v1 = rgb_to_hsv(B1, G1, R1)
  
  B2, G2, R2 = img[n][300,200]
  h2, s2, v2 = rgb_to_hsv(B2, G2, R2)
  
  # input rgb value ke csv
  file = open("data_kersen.csv","a")
  file.write(str(h1) + "," + str(s1) + "," + str(v1) + "," + str(h2) + "," + str(s2) + "," + str(v2) +",Matang"+ "\n")
  file.close() 


# Kelas Mentah
mypath="resize/mentah"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
img = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  img[n] = cv.imread( join(mypath,onlyfiles[n]) )
  
  B1, G1, R1 = img[n][200,300]
  h1, s1, v1 = rgb_to_hsv(B1, G1, R1)
  
  B2, G2, R2 = img[n][300,200]
  h2, s2, v2 = rgb_to_hsv(B2, G2, R2)
  
  # input rgb value ke csv
  file = open("data_kersen.csv","a")
  file.write(str(h1) + "," + str(s1) + "," + str(v1) + "," + str(h2) + "," + str(s2) + "," + str(v2) +",Mentah"+ "\n")
  file.close() 

cv.waitKey(0)
cv.destroyAllWindows()
