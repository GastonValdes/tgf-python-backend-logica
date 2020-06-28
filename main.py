import requests
from flask import Flask, jsonify 

app = Flask(__name__)

@app.route('/calculos', methods=["GET"])
def executeCalc():

    urlSensores = 'http://localhost:3010/sensores'
    urlUmbrales = 'http://localhost:3010/umbrales'
    
    #responseSensores = requests.get(urlSensores)
    responseSensores = requests.get('http://localhost:3010/sensores/5ef1550af54594ffd00719bb')
    responseSensores_json = responseSensores.json
    if responseSensores.status_code == 200:
        print(responseSensores.content)
    
    responseUmbrales = requests.get(urlUmbrales)
    responseUmbrales_json = responseUmbrales.json
    if responseUmbrales.status_code == 200:
        print(responseUmbrales.content)
    
    return {'Respuesta': 'ok'},200
    

if __name__ == '__main__':
    app.run(debug=True)


    
    #medicion = responseSensores_json['medicion']