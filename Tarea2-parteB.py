#función que genera la id del registro record
id=0
def generar_id():
    global id
    id = id +1
    return id

dict_filmografia = {}
#iniciamos los valores de "dict_filmografia"
lista_name = []
lista_director = []
lista_actors = []
lista_release = []
lista_country = []
lista_duration = []
lista_rating = []
lista_file = []
#Leemmos el fichero y almacenamos la información en "dict_filmografia"
try:
    fichero = open("C:\\Users\\marta\\nuevo repositorio\\filmografia.csv","r")
except:
    print("Error archivo")
else:
    
    lista_de_lineas = fichero.readlines()
    #guardamos en la variable "cantidad_de_lineas" las lineas totales del fichero
    cantidad_de_lineas = len(lista_de_lineas)
    lista_de_claves = lista_de_lineas[0].split(",")
    #recorremos las lineas del fichero saltandonos la primera linea
    for linea in lista_de_lineas[1:]:
        lista_de_palabras = linea.split(",")
        lista_name.append(lista_de_palabras[0])
        lista_director.append(lista_de_palabras[1])
        lista_actors.append(lista_de_palabras[2])
        lista_release.append(lista_de_palabras[3])
        lista_country.append(lista_de_palabras[4])
        lista_duration.append(lista_de_palabras[5])
        lista_rating.append(lista_de_palabras[6])
        lista_file.append(lista_de_palabras[7])
    dict_filmografia[lista_de_claves[0]]=lista_name
    dict_filmografia[lista_de_claves[1]]=lista_director
    dict_filmografia[lista_de_claves[2]]=lista_actors
    dict_filmografia[lista_de_claves[3]]=lista_release
    dict_filmografia[lista_de_claves[4]]=lista_country
    dict_filmografia[lista_de_claves[5]]=lista_duration
    dict_filmografia[lista_de_claves[6]]=lista_rating
    dict_filmografia[lista_de_claves[7]]=lista_file
finally:
    fichero.close()
#creamos el texto que va a reemplazar al csv
contador = 0
texto_xml=""
while contador!=cantidad_de_lineas-1:
    texto_xml= texto_xml + f'<record id="{generar_id()}" model="videoclub.peliculas">\n'
    texto_xml= texto_xml + f'<field name="name">{dict_filmografia[lista_de_claves[0]][contador]}</field>\n'
    texto_xml= texto_xml + f'<field name="director" ref="{dict_filmografia[lista_de_claves[1]][contador]}" />\n'
    texto_xml= texto_xml + f'<field name="actors" eval="[(6,0,[ref(‘{dict_filmografia[lista_de_claves[2]][contador]}’)])]" />'
    texto_xml= texto_xml + f'<field name="release">{dict_filmografia[lista_de_claves[3]][contador]}</field>\n'
    texto_xml= texto_xml + f'<field name="country">{dict_filmografia[lista_de_claves[4]][contador]}</field>\n'
    texto_xml= texto_xml + f' <field name="duration">{dict_filmografia[lista_de_claves[5]][contador]}</field>\n'
    texto_xml= texto_xml + f' <field name="rating">{dict_filmografia[lista_de_claves[6]][contador]}</field>\n'
    texto_xml= texto_xml + f' <field file="{dict_filmografia[lista_de_claves[7]][contador]}" name="cover" type="base64" />\n'
    texto_xml= texto_xml + f' </record>\n'
    contador = contador + 1
print(texto_xml)
#escribimos el texto en el fichero xml
try:
    fichero = open("C:\\Users\\marta\\nuevo repositorio\\filmografia_odoo.xml","w")
    fichero.write(texto_xml)
except:
    print("Error archivo")
    
finally:
    fichero.close()