# MODULO OS
# El módulo OS en Python proporciona funciones para interactuar con el sistema operativo. OS es un módulo estándar de Python.
import os

# #
#  SQLAlchemy es una biblioteca de Python para trabajar con bases de datos relacionales. 
#  Ofrece una manera de interactuar con las bases de datos a través de un modelo de objetos, 
#  sin tener que escribir manualmente sentencias SQL.
#  Con SQLAlchemy, puedes definir clases de Python que representan tablas en la base de datos y utilizar estas clases para insertar, 
#  actualizar y consultar datos en la base de datos.
# #
from sqlalchemy import create_engine


from sqlalchemy.orm.session import sessionmaker


from sqlalchemy.ext.declarative import declarative_base

# Se guardara el nombre de la base de datos
sqlite_file_name = '../database.sql'



# #
#  Se leera el directorio actual del archivo database
#  El módulo os.path es un submódulo del módulo OS en Python que se utiliza para la manipulación de nombres de rutas comunes.
#  Dirname()
#  El método os.path.dirname() en Python se usa para obtener el nombre del directorio de la ruta especificada.
#  Realpath()
#  El método os.path.realpath() en Python se usa para obtener la ruta canónica (por así decirlo, la URL original de una web)
#  del nombre de archivo especificado al eliminar cualquier enlace simbólico que se encuentre en la ruta.
# #

base_dir = os.path.dirname(os.path.realpath(__file__))

# #
#  sqlite:/// es la forma en la que se conecta a una base de datos, se usa el metodo join para unir las variables de url
#  Join()
#  Combina nombres de rutas en una ruta completa. Esto significa que puede fusionar varias partes de una ruta en una, 
#  en lugar de codificar manualmente cada nombre de ruta
#  La función os.path.join acepta una lista de rutas que desea fusionar en una sola:
#   ejemplo = os.path.join(ruta1, ruta2)
#  ruta1, ruta2 y todos los valores posteriores representan las rutas que desea combinar en un solo nombre.
#   ejemplo = os.path.join("/Usuarios/James/tutoriales", "index.html")
#   print(ejemplo)
#  Este código devuelve: /Users/James/tutorials/index.html
# #
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# representa el motor de la base de datos, con el comando “echo=True” para que al momento de realizar la base de datos,
# me muestre por consola lo que esta realizando, que seria el codigo
engine = create_engine(database_url, echo = True)

# Se crea session para conectarse a la base de datos, se enlaza con el comando “bind” y se iguala a engine
Session = sessionmaker(bind=engine)

# Sirve para manipular todas las tablas de la base de datos
Base = declarative_base()