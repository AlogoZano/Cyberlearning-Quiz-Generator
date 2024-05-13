import json
import re


with open('C:\\Users\\adrio\\OneDrive\\Escritorio\\ITESM\\Sexto Semestre\\Servicio Becario - Cyberlearning\\CyberLearning2\\MovCirc\\MOV_CIRCULAR_1.json', 'r') as f1:
  first10 = json.load(f1)

with open('C:\\Users\\adrio\\OneDrive\\Escritorio\\ITESM\\Sexto Semestre\\Servicio Becario - Cyberlearning\\CyberLearning2\\MovCirc\\MOV_CIRCULAR_2.json', 'r') as f2:
  last10 = json.load(f2)


response1 = first10["mapping"]["5c711869-94d5-4b15-8a6b-ef4554c010b0"]["message"]["content"]["parts"]
response2 = last10["mapping"]["6d09a103-718c-4d3b-a49c-f63f3834743b"]["message"]["content"]["parts"]

response1_txt = str(response1[0])
response2_txt = str(response2[0])

comp_response = response1_txt + response2_txt

preguntas_respuestas = comp_response.split("\n\n")

for i, pregunta_respuesta in enumerate(preguntas_respuestas, start=1):
    #print(f"Pregunta {i}:")
    preguntas_respuestas[i-1] = preguntas_respuestas[i-1].encode('latin1').decode('utf-8')
    pregunta_respuesta_deco = pregunta_respuesta.encode('latin1').decode('utf-8')
    #print(pregunta_respuesta)
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

print(preguntas)


