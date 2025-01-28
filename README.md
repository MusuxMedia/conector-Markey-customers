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
