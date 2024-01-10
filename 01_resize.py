from os import listdir
from os.path import isfile, join
import numpy
import cv2 as cv

# kelas matang
mypath="png/matang"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = cv.imread( join(mypath,onlyfiles[n]) )
  down_width = 500
  down_height = 500
  down_points = (down_width, down_height)
  images[n] = cv.resize(images[n], down_points, interpolation= cv.INTER_LINEAR)
  cv.imwrite(f'resize/matang/matang_{n+1}.png',images[n])
  
# kelas mentah
mypath="png/mentah"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = cv.imread( join(mypath,onlyfiles[n]) )
  down_width = 500
  down_height = 500
  down_points = (down_width, down_height)
  images[n] = cv.resize(images[n], down_points, interpolation= cv.INTER_LINEAR)
  cv.imwrite(f'resize/mentah/mentah_{n+1}.png',images[n])

cv.waitKey(0)
cv.destroyAllWindows()
