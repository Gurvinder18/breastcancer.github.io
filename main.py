import cv2
import io
from flask import Flask, request, jsonify
import base64
from fastai.vision import *
import PIL.Image as Image

app = Flask("__name__")
learn = load_learner('/Users/gurvi/Desktop/pythonProject1', 'tanay.h5')
@app.route('/')
def func():
    return "Use / predict"

@app.route('/predict', methods=['POST'])
def home():
    encodedimage = request.form.get('encoded_image')
    b = base64.b64decode(encodedimage)
    img = Image.open(io.BytesIO(b))
    img.save('mamogram.png')
    p = cv2.imread('mamogram.png')
    image = open_image('mamogram.png')
    result = learn.predict(image)
    print(result)

    return jsonify({'result':str(result)})


if __name__ == "__main__":
    app.run(debug=True)
