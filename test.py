import base64
from fastai.vision import *
import PIL.Image as Image
import cv2

learn = load_learner('/Users/gurvi/Desktop/pythonProject1', 'tanay.h5')
with open('non-IDC.png', 'rb') as Imagefile:
    byteform = base64.b64encode(Imagefile.read())
print(byteform)
b = base64.b64decode(byteform)
img = Image.open(io.BytesIO(b))
img.save('mamogram.png')
p = cv2.imread('mamogram.png')
image = open_image('mamogram.png')
result = learn.predict(image)
print(result)
