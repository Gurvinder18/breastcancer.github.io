from flask import Flask, request, jsonify

app = Flask("__name__")
@app.route('/')
def func():
    return "Use / predict"

@app.route('/predict', methods=['POST'])
def home():
    encodedimage = request.form.get('encoded_image')

    return jsonify({'result': 'BENIGN'})


if __name__ == "__main__":
    app.run(debug=True)
