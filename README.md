# Conector utilizado en Austral

## ¿Que contiene?
El desarrollo esta compuesto en 2 partes:
+ Conector con Markey
+ Conector Fake Entry


## Conector Markey
Se encuentra dentro de la carpeta **app/conector**

Dentro hay varios archivos que voy a explicar el propósito de c/u

### config.py
Este archivo contiene la clase **Settings** que básicamente es un enum con varias constantes que sirven para la configuración de la conexión con la API de Markey (URL, token y api_key)

Cabe aclarar que acá dentro también se encuentra definido el **CUTOMERTYPE** el cual se extrae de la instancia del cliente en Debmedia, en el apartado de tipos de clientes. En este caso el tipo de cliente **cliente** tiene el id 829.
![image](https://github.com/user-attachments/assets/e4a130fc-a88a-4a6f-a5d8-3b5004ada989)

### DataValidator.py
Este archivo contiene la clase **DataValidator** la cual se encarga de validar los datos que vienen desde el Json del paciente que nos envía Markey, en caso de que algun dato no venga, devuelve vacío ese campo.

A su vez devuelve si el Json es valido o no.

### MarkeyAPI.py
Esta clase es la responsable de tener la estructura con la cual conectarse a la API de Markey, acá se utilizan las variables definidas en config.py.

en __getHeaders se definen los header que se hacen en la consulta y en __getPayload el body que se envia.

### Paciente.py
En esta clase, en el método **toJson** se define el formato que tiene que tener el paciente para que pueda ser consumido por Debmedia.

### ProcessOrganizer.py
Objeto que me sirve para organizar todo el proceso de llamado de la API, es un "pseudo-service"


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Llamador Fake Entry

Este desarrollo es más sencillo, simplemente es el endpoint de **Fake entry** de la docu de Numia, pero modificado para funcionar con GET y poder pasarle los párametros por query, que era lo que nos habían pedido desde Markey.

### ¿Que parametros puede recibir?
+ consultorio (string)
+ token (string) (este es el token de la instancia que se pide a Numia)
+ pantallas (list[int])
+ turno (string) (se puede pasar el numero del turno o también nombre y apellido o cualquier cosa que se quiera mostrar por pantalla en esa columna)
+ server (string) (opcional)
Este último parametro es para **SOLO PARA TESTING EN OTRA INSTANCIA** si quiero testear si el endpoint funciona en **server** pongo `debq2` y en **token** pongo el token de la instancia de prueba de musux, de esta forma puedo probarlo en alguna de las pantallas de nuestra instancia que esten habilitadas para mostrar Fake Entry. 
