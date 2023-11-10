# EFI Práctica Profesionalizante Parte 2

#### En esta segunda fase de la práctica profesionalizante, hemos ampliado nuestra aplicación miniblog desarrollada en Flask, incorporando dos herramientas avanzadas: Marshmallow y MethodView. Estas adiciones permitirán la creación de endpoints sólidos para interactuar con nuestra aplicación de manera eficiente.

##### En esta instancia, hemos tomado la decisión de ofrecer nuestro miniblog como una API consumible. Esto implica que no estará disponible ni visible como una aplicación web convencional.

**A continuación, se presenta un manual para implementar el repositorio:**

Instrucciones para implementar el repositorio:
------------

1. Antes de clonar el repositorio, es recomendable ubicarse en la carpeta deseada desde la terminal de git.
2. Posteriormente, se puede clonar el repositorio dentro de la carpeta seleccionada. Esto se puede realizar desde la terminal de git mediante el comando `git clone git@github.com:NicoBufrini/EFI_Buf_Gen_Python.git` o descargándolo en formato zip desde **"code"** para descomprimirlo posteriormente en la carpeta.

**A partir de este punto, se puede implementar en dos formas diferentes: en la máquina local o mediante Docker.**

Cómo implementarlo en la máquina local:
----------------

1. Después de clonar el repositorio, acceda a la carpeta que contiene todos los archivos del repositorio para crear un entorno virtual. La carpeta en este caso es **EFI_Buf_Gen**, también se puede realizar desde la terminal.

    Se puede crear el entorno con el comando:
    `python -m venv entorno`
    
    O con el comando:
    `virtualenv entorno`

2. Activa el entorno virtual con el comando:

    Para Windows:
    `entorno\Scripts\activate.bat`

    Para Unix o Mac:
    `source entorno/bin/activate`

3. Posteriormente, instale todas las librerías necesarias para utilizar el proyecto. Para ello, utilice el archivo **requirements.txt** (un archivo en el repositorio clonado). Instale las dependencias con el siguiente comando:

    `pip install -r requirements.txt`

4. Ahora, cree la base de datos que se utilizará para el proyecto y complete el archivo **.env** (que no está en el repositorio, pero tiene el archivo **.env.sample**). Renómbrelo a **.env** y complete las variables (ROOT_USER, MYSQL_ROOT_PASSWORD, MYSQL_CONTAINER_NAME y MYSQL_DATABASE) con los datos correspondientes.

5. Luego, ejecute los siguientes comandos para crear las tablas en la base de datos:

    `flask db init`

    `flask db migrate -m "creando tablas del blog"`

    `flask db upgrade`

6. Por último, se puede ejecutar el proyecto para comenzar a utilizarlo:

    `flask run --reload`

Cómo implementarlo con Docker:
-------------

1. Complete el archivo **.env**. Utilice el archivo **.env.sample** y renómbrelo a **.env**. Complete las variables (ROOT_USER, MYSQL_ROOT_PASSWORD, MYSQL_CONTAINER_NAME, MYSQL_PASSWORD y MYSQL_DATABASE) con los datos correspondientes.

2. Ejecute el siguiente comando para crear una imagen para MySQL y para la aplicación Flask. Asegúrese de estar en la carpeta donde tiene el proyecto (**EFI_Buf_Gen** en este caso). Si está en Windows, asegúrese de tener la aplicación Docker abierta antes de ejecutar el comando:

    `docker-compose build`

    NOTA: Si está en Linux, agregue "sudo" al principio de todos los comandos de Docker.

3. Ahora, ejecute el siguiente comando para crear y ejecutar los contenedores de MySQL y Flask:

    `docker-compose up`

    **NOTA: Se puede unificar los pasos 2 y 3 con el comando:**

    `docker-compose build && docker-compose up`

4. Luego, abra la siguiente ruta en el navegador para verificar si el contenedor está funcionando:

    `localhost:5005`