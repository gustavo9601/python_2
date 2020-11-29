from setuptools import setup

setup(
    name="paquete_no_1",
    version="1.0.0",
    description="Documentacion de paquete_1",
    author="GM",
    author_email = "ing.gustavo.marquez@gmail.com",
    scripts=[], # en el arreglo se pasa el nombre de los scrripts de necesitarse
    packages=["paquete_1"]  # se pasa el paquete (directorio), paquete.direcotiro hijo etc
)

# En consola en el directorio donde este el archivo setup se ejecuta:
# py setup.py sdist
# de esta forma se generara el archivo de distribucion basica para que sea reconocido los directorios de paquete

# generado el archivo se debe instalar el archivo de distribucion, y lo instala en todo el SO
# pip3 install nombre_archivo_distribucion    dentro del directorio dist
# pip3 list   # nos lista todas las librerias instaladas
# pip3 uninstall nombre_paquete   # desistalar el paquete
