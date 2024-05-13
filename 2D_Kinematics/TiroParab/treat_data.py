import json
import re

with open('C:\\Users\\adrio\\OneDrive\\Escritorio\\ITESM\\Sexto Semestre\\Servicio Becario - Cyberlearning\\CyberLearning2\\TiroParab\\TIRO_PARABOLICO_1.json', 'r') as f:
  data = json.load(f)


response = data["mapping"]["ad856dba-11e5-4155-b01d-8cb5f2a9ea28"]["message"]["content"]["parts"]
response_txt = str(response[0])

preguntas_respuestas = response_txt.split("\n\n")



for i, pregunta_respuesta in enumerate(preguntas_respuestas, start=1):
    #print(f"Pregunta {i}:")
    preguntas_respuestas[i-1] = preguntas_respuestas[i-1].encode('latin1').decode('utf-8')
    pregunta_respuesta_deco = pregunta_respuesta.encode('latin1').decode('utf-8')
    #print(pregunta_respuesta_deco)
    #print()


lineas_totales = []
preguntas = []
opciones = []
respuestas_correctas = []


for i in range(1, len(preguntas_respuestas)):
  lineas_totales.append(preguntas_respuestas[i].split('\n'))


for i in range(1, len(lineas_totales)+1):

  preguntas.append(lineas_totales[i-1][0])
  opciones.append(lineas_totales[i-1][1:-1])
  respuestas_correctas.append(lineas_totales[i-1][-1])


for i in range(0, len(preguntas)):
   indice_pregunta = preguntas[i].index(' ') + 1
   preguntas[i] = preguntas[i][indice_pregunta:]




