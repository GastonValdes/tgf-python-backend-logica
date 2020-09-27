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
   

######################################################################################################
############         En este bloque voy a intentar traer todos los sensores        ###################
#    rSensores = requests.get(urlSensores )  # Armo la llamada a la API para de sensores
#    if rSensores.status_code == 200: # Chequeo si el resultado de la API fue correcto
#        rSensores_json = rSensores.json() # paso el resultado a JSON
#        rSensores_Names = rSensores_json['identificador'] #Obtengo la lista de nombres de sensores 
#        print('lista completa de sensores')
#        print(rSensores_json)
#        print('lista de nombres de los sensores')
#        print(rSensores_Names)
#######################################################################################################



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
    #####################################################################

    #####################################################################
    ###  Este bloque trae el valor actual del actuador de Temperatura ###
    print (urlActuadores + '/' + act_temp)
    rAct_temp = requests.get(urlActuadores + '/' + act_temp)  # Armo la llamada a la API para el Actuador de Temperatura interior
    if rAct_temp.status_code == 200: # Chequeo si el resultado de la API fue correcto
        rAct_temp_json = rAct_temp.json() # paso el resultado a JSON
        rAct_temp_Medicion = rAct_temp_json['operacion'] #Obtengo el valor de la propiedad Operacion 
        print('valor Actuador de Temperatura')
        print(rAct_temp_Medicion)
        act_temp_calc = rAct_temp_Medicion
    ################################################################

    #####################################################################
    ###  Este bloque trae el valor actual del actuador de Iluminacion ###
    print (urlActuadores + '/' + act_ilum)
    rAct_ilum = requests.get(urlActuadores + '/' + act_ilum)  # Armo la llamada a la API para el Actuador de Iluminacion interior
    if rAct_ilum.status_code == 200: # Chequeo si el resultado de la API fue correcto
        rAct_ilum_json = rAct_ilum.json() # paso el resultado a JSON
        rAct_ilum_Medicion = rAct_ilum_json['operacion'] #Obtengo el valor de la propiedad Operacion 
        print('valor Actuador de Iluminacion')
        print(rAct_ilum_Medicion)
        act_ilum_calc = rAct_ilum_Medicion
    ################################################################

    #####################################################################
    ###  Este bloque trae el valor actual del actuador de Apertura de ventanas ###
    print (urlActuadores + '/' + act_vent)
    rAct_vent = requests.get(urlActuadores + '/' + act_vent)  # Armo la llamada a la API para el Actuador de Apertura de ventanas
    if rAct_vent.status_code == 200: # Chequeo si el resultado de la API fue correcto
        rAct_vent_json = rAct_vent.json() # paso el resultado a JSON
        rAct_vent_Medicion = rAct_vent_json['operacion'] #Obtengo el valor de la propiedad Operacion 
        print('valor Actuador de Apertura de Ventanas')
        print(rAct_vent_Medicion)
        act_vent_calc = rAct_vent_Medicion
    ################################################################

    #####################################################################
    ###  Este bloque trae el valor actual del actuador de Apertura de Persianas ###
    print (urlActuadores + '/' + act_pers)
    rAct_pers = requests.get(urlActuadores + '/' + act_pers)  # Armo la llamada a la API para el Actuador de APertura de Persianas
    if rAct_pers.status_code == 200: # Chequeo si el resultado de la API fue correcto
        rAct_pers_json = rAct_pers.json() # paso el resultado a JSON
        rAct_pers_Medicion = rAct_pers_json['operacion'] #Obtengo el valor de la propiedad Operacion 
        print('valor Actuador de Apertura de Persianas')
        print(rAct_pers_Medicion)
        act_pers_calc = rAct_pers_Medicion
    ################################################################

    ###################################################################
    ###   Aca hay que meter la logica o la llamada a un servicio de ###
    ###   computacion cognitiva para que devuelva los resultados    ###
    ### Verifico si el usuario esta presente, con presencia > o igual a 50
    if  rSensor_pres_int_Medicion < 50:
        act_ilum_calc = 0
        act_temp_calc = 0
        act_vent_calc = "Cerrada"
        act_pers_calc = "Cerrada"
        print ('el usuario no esta presente Apago todo')

    else:
        print ('Me dio = o mayor a 50')
        print ('Temperatura interior: ')
        print (rSensor_temp_int_Medicion)
        print ('Temperatura configurada: ')
        print (rUmbral_Temp_Medicion)
        ####### Temperatura interior es mayor a la deseada #######       
        if rSensor_temp_int_Medicion > rUmbral_Temp_Medicion:
            print ('Temp interior > a la deseada ')
            ##### Temperatura interior mayor a Temperatura Exterior
            if rSensor_temp_int_Medicion > rSensor_temp_ext_Medicion:
                print ('estado de persiana:')
                print (rAct_pers_Medicion)
                #### si la persiana esta abierta
                if rAct_pers_Medicion == "Abierta":
                    act_pers_calc = "Cerrada"
                    ### si la ventana esta abierta
                    if rAct_temp_Medicion == "Abierta":
                        act_vent_calc = "Cerrada"
                        act_temp_calc = rUmbral_Temp_Medicion - rSensor_temp_int_Medicion
                        act_ilum = rSensor_ilum_int_Medicion - rUmbral_ilum_Medicion
                    else:
                        act_vent_calc = "Abierta"
                #### Si la persiana esta cerrada
                else:
                    act_pers_calc = "Abierta"

            ##### Temperatura interior menor o igual a Temperatura exterior 
            if rSensor_temp_int_Medicion <= rSensor_temp_ext_Medicion:
                print ('Temperatura Interior <= exterior => Cierro Ventana')
                act_vent_calc = "Cerrada"
                act_temp_calc = rSensor_temp_int_Medicion - rUmbral_Temp_Medicion
                print ('corregir temperatura')
                print (act_temp_calc)

        ####### Temperatura interior es menor a la deseada #######  
        elif rSensor_temp_int_Medicion < rUmbral_Temp_Medicion:
            print ('Temp interior < a la deseada ')
            ##### Temperatura interior menor a Temperatura Exterior
            if rSensor_temp_int_Medicion < rSensor_temp_ext_Medicion:
                ### si la ventana esta abierta
                if rAct_temp_Medicion == "Abierta":
                    ### cierro la ventana
                    act_vent_calc = "Cerrada"
                ### si la ventana esta cerrada
                else:
                    #### si la persiana esta abierta
                    if rAct_pers_Medicion == "Abierta":
                        act_pers_calc = "Cerrada"
                    #### si la persiana esta cerrada
                    else:
                        act_temp_calc = rUmbral_Temp_Medicion - rSensor_temp_int_Medicion
                        act_ilum = rSensor_ilum_int_Medicion - rUmbral_ilum_Medicion
                

    #rUmbral_ilum_Medicion > rSensor_ilum_int_Medicion:
    #    act_ilum_calc = rUmbral_ilum_Medicion
    #    print('hay que subir la luz')


    ###############################################################
    ###  Este bloque actualiza el actuador de Luz         ###
    payload_act_ilum = {'id' : act_ilum, 'identificador': 'Actuador_Ilum_001', 'dir_ip': '192.169.10.123', 'dir_mac': '69-4F-7A-AA-C3-77', 'tipo': 'Correccion', 'subtipo': 'Iluminacion', 'habilitado': 'true', 'operacion' : act_ilum_calc}
    rAct_ilum = requests.patch(urlActuadores, json=payload_act_ilum)  # Armo la llamada a la API para el sensor de temp interior
    print(urlActuadores)
    print(rAct_ilum)
    print(rAct_ilum.content)
    if rAct_ilum.status_code == 200: # Chequeo si el resultado de la API fue correcto
        print('post correcto')
        print(act_ilum_calc)
    ################################################################

    ###############################################################
    ###  Este bloque actualiza el actuador de temperatura         ###
    payload_act_temp = {'id' : act_temp, 'identificador': 'Actuador_Temp_001', 'dir_ip': '192.169.10.111', 'dir_mac': 'AA-15-5D-82-4C-52', 'tipo': 'Correccion', 'subtipo': 'Temperatura', 'habilitado': 'true', 'operacion' : act_temp_calc}
    rAct_temp = requests.patch(urlActuadores, json=payload_act_temp)  # Armo la llamada a la API para el sensor de temp interior
    print(urlActuadores)
    print(rAct_temp)
    print(rAct_temp.content)
    if rAct_ilum.status_code == 200: # Chequeo si el resultado de la API fue correcto
        print('post correcto')
        print(act_temp_calc)
    ################################################################


    ###############################################################
    ###  Este bloque actualiza el actuador de ventana         ###
    payload_act_ventana = {'id' : act_vent, 'identificador': 'Actuador_Aper_002', 'dir_ip': '192.169.10.114', 'dir_mac': '6B-1E-5D-82-4B-F3', 'tipo': 'Apertura', 'subtipo': 'Ventana', 'habilitado': 'true', 'operacion' : act_vent_calc}
    rAct_vent = requests.patch(urlActuadores, json=payload_act_ventana)  # Armo la llamada a la API para el sensor de temp interior
    print(urlActuadores)
    print(rAct_vent)
    print(rAct_vent.content)
    if rAct_vent.status_code == 200: # Chequeo si el resultado de la API fue correcto
        print('post correcto')
        print(act_vent_calc)
    ################################################################

    ###############################################################
    ###  Este bloque actualiza el actuador de persiana          ###
    payload_act_persiana = {'id' : act_pers, 'identificador': 'Actuador_Aper_001', 'dir_ip': '192.169.10.115', 'dir_mac': 'AA-15-5D-82-4C-52', 'tipo': 'Apertura', 'subtipo': 'Persiana', 'habilitado': 'true', 'operacion' : act_pers_calc}
    rAct_pers = requests.patch(urlActuadores, json=payload_act_persiana)  # Armo la llamada a la API para el sensor de temp interior
    print(urlActuadores)
    print(rAct_pers)
    print(rAct_pers.content)
    if rAct_pers.status_code == 200: # Chequeo si el resultado de la API fue correcto
        print('post correcto')
        print(act_pers_calc)
    ################################################################

    #####################################################
    ###         Genero la respuesta de la API         ###      
    return {'Respuesta': 'ok'},200
    

if __name__ == '__main__':
    app.run(debug=True)


    
    #medicion = responseSensores_json['medicion']