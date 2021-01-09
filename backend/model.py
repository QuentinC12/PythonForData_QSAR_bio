from flask import Flask, request, jsonify
import pickle
import numpy as np
import json
app = Flask(__name__)
model = pickle.load(open('../modelFinal.pkl', 'rb'))

@app.route('/')
def hello_world():
    return 'Bienvenue sur mon API, essayez le Endpoints /predict en méthode POST aves les données d\'une mollécule chimique'


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    X = np.array([v for k, v in data.items()])
    prediction = model.predict([X])
    print(prediction[0])
    if prediction[0] == 0:
        reponse = 'NRB'
    else:
        reponse = 'RB'
    return reponse

if __name__ == "__main__":
    app.run(debug=True)


