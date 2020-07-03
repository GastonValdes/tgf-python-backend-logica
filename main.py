import requests
from flask import Flask, jsonify 
from flask_cors import CORS

app = Flask(__name__)

#cors = CORS(app, resources={r"/calculos": {"origins": "http://localhost:port"}})
CORS(app)
@app.route('/calculos', methods=["GET"])
def executeCalc():

    urlSensores = 'http://localhost:3010/sensores'
    urlUmbrales = 'http://localhost:3010/umbrales'
    urlActuadores = 'http://localhost:3010/actuadores'
    
    sens_temp_int = '5ef7e82b6bfea84aac9e00de'
    sens_temp_ext = '5ef1550af54594ffd00719bb'
    sens_ilum_int = '5ef15566f54594ffd00719bd'
    sens_ilum_ext = '5ef1554ef54594ffd00719bc'
    sens_pres_int = '5ef8dfc46bfea84aac9e00df'

    umbr_ilum = '5ef75fc1c7cdc90b341294e7'
    umbr_temp = '5ee3345d57073346e027f608'

    act_temp = '5ee337e5d5618d47e86355e4'
    act_pers = '5ef91feaf6aa3a589cf22a47'
    act_vent = '5ef92105f6aa3a589cf22a48'
    act_ilum = '5ef9217cf6aa3a589cf22a49'
   
   ###############################################################
   ###  Este bloque trae el sensor de Temperatura Interior     ###
    rSensor_temp_int = requests.get(urlSensores + '/' + sens_temp_int )  # Armo la llamada a la API para el sensor de temp interior
    if rSensor_temp_int.status_code == 200: # Chequeo si el resultado de la API fue correcto
        rSensor_temp_int_json = rSensor_temp_int.json() # paso el resultado a JSON
        rSensor_temp_int_Medicion = rSensor_temp_int_json['medicion'] #Obtengo el valor de la propiedad Medicion 
        print('medicion Sensor Temperatura Interior')
        print(rSensor_temp_int_Medicion)
    ################################################################
    

    ###############################################################
    ###   Este bloque trae el sensor de Temperatura Exterior    ###    
    rSensor_temp_ext = requests.get(urlSensores + '/' + sens_temp_ext )  # Armo la llamada a la API para el sensor de temp exterior
    if rSensor_temp_ext.status_code == 200: # Chequeo si el resultado de la API fue correcto
        rSensor_temp_ext_json = rSensor_temp_ext.json() # paso el resultado a JSON
        rSensor_temp_ext_Medicion = rSensor_temp_ext_json['medicion'] #Obtengo el valor de la propiedad Medicion 
        print('medicion Sensor Temperatura Exterior')
        print(rSensor_temp_ext_Medicion)
    ###############################################################

    ###############################################################
    ###  Este bloque trae el sensor de Iluminacion Interior     ###
    rSensor_ilum_int = requests.get(urlSensores + '/' + sens_ilum_int )  # Armo la llamada a la API para el sensor de iluminacion interior
    if rSensor_ilum_int.status_code == 200: # Chequeo si el resultado de la API fue correcto
        rSensor_ilum_int_json = rSensor_ilum_int.json() # paso el resultado a JSON
        rSensor_ilum_int_Medicion = rSensor_ilum_int_json['medicion'] #Obtengo el valor de la propiedad Medicion 
        print('medicion Sensor Iluminacion Interior')
        print(rSensor_ilum_int_Medicion)
    ################################################################

    ###############################################################
    ###  Este bloque trae el sensor de Iluminacion Exterior     ###
    rSensor_ilum_ext = requests.get(urlSensores + '/' + sens_ilum_ext )  # Armo la llamada a la API para el sensor de iluminacion Exterior
    if rSensor_ilum_ext.status_code == 200: # Chequeo si el resultado de la API fue correcto
        rSensor_ilum_ext_json = rSensor_ilum_ext.json() # paso el resultado a JSON
        rSensor_ilum_ext_Medicion = rSensor_ilum_ext_json['medicion'] #Obtengo el valor de la propiedad Medicion 
        print('medicion Sensor Iluminacion Exterior')
        print(rSensor_ilum_ext_Medicion)
    ################################################################    
    
    ###############################################################
    ###  Este bloque trae el sensor de Presencia Interior     ###
    rSensor_pres_int = requests.get(urlSensores + '/' + sens_pres_int )  # Armo la llamada a la API para el sensor de Presencia
    if rSensor_pres_int.status_code == 200: # Chequeo si el resultado de la API fue correcto
        rSensor_pres_int_json = rSensor_pres_int.json() # paso el resultado a JSON
        rSensor_pres_int_Medicion = rSensor_pres_int_json['medicion'] #Obtengo el valor de la propiedad Medicion 
        print('medicion Sensor Presencia Interior')
        print(rSensor_pres_int_Medicion)
    ################################################################    

    #################################################################
    ####  Este Bloque trae todos los umbrales de configuracion   ####
    #responseUmbrales = requests.get(urlUmbrales)
    #responseUmbrales_json = responseUmbrales.json()
    #if responseUmbrales.status_code == 200:
    #    print('Aca empieza la segunda API--->')
    #   print(responseUmbrales_json)
    
    ###############################################################
    ###       Este bloque trae el umbral de Temperatura         ###
    print (urlUmbrales + '/' + umbr_temp)
    rUmbral_temp = requests.get(urlUmbrales + '/' + umbr_temp)  # Armo la llamada a la API para el sensor de temp interior
    if rUmbral_temp.status_code == 200: # Chequeo si el resultado de la API fue correcto
        rUmbral_temp_json = rUmbral_temp.json() # paso el resultado a JSON
        rUmbral_Temp_Medicion = rUmbral_temp_json['valor'] #Obtengo el valor de la propiedad Medicion 
        print('valor Umbral de Temperatura')
        print(rUmbral_Temp_Medicion)
    ################################################################
    
    ###############################################################
    ###       Este bloque trae el umbral de Temperatura         ###
    print (urlUmbrales + '/' + umbr_ilum)
    rUmbral_ilum = requests.get(urlUmbrales + '/' + umbr_ilum)  # Armo la llamada a la API para el sensor de temp interior
    if rUmbral_temp.status_code == 200: # Chequeo si el resultado de la API fue correcto
        rUmbral_ilum_json = rUmbral_ilum.json() # paso el resultado a JSON
        rUmbral_ilum_Medicion = rUmbral_ilum_json['valor'] #Obtengo el valor de la propiedad Medicion 
        print('valor Umbral de Iluminacion')
        print(rUmbral_ilum_Medicion)
    ################################################################

    ###################################################################
    ###   Aca hay que meter la logica o la llamada a un servicio de ###
    ###   computacion cognitiva para que devuelva los resultados    ###
    if rUmbral_ilum_Medicion > rSensor_ilum_int_Medicion:
        act_ilum_calc = rUmbral_ilum_Medicion
        print('hay que subir la luz')


    ###############################################################
    ###  Este bloque actualiza el actuador de Luz         ###
        payload_act_ilum = {'id' : act_ilum, 'identificador': 'Actuador_Ilum_001', 'dir_ip': '192.169.10.123', 'dir_mac': '69-4F-7A-AA-C3-77', 'tipo': 'Iluminacion', 'subtipo': 'Interior', 'habilitado': 'true', 'operacion' : act_ilum_calc}
        rAct_ilum = requests.patch(urlActuadores, json=payload_act_ilum)  # Armo la llamada a la API para el sensor de temp interior
        print(urlActuadores)
        print(rAct_ilum)
        print(rAct_ilum.content)
        if rAct_ilum.status_code == 200: # Chequeo si el resultado de la API fue correcto
            print('post correcto')
            print(act_ilum_calc)
    ################################################################





    #####################################################
    ###         Genero la respuesta de la API         ###      
    return {'Respuesta': 'ok'},200
    

if __name__ == '__main__':
    app.run(debug=True)


    
    #medicion = responseSensores_json['medicion']