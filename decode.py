import PIL.Image as Image #pip install pillow
import io
import base64
from byte_array import byte_data

b = base64.b64decode(byte_data)
#print(b)
img = Image.open(io.BytesIO(b))
img.show()