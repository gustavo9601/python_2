import os

current_directory = os.getcwd()
print("current_directory", current_directory)

# devuelve todo los archivos en el directorio pasado por parametro
list_files_in_dir = os.listdir('.')
print("list_files_in_dir", list_files_in_dir)

# Navegando hacia una ruta en PY, cambiando el puntero de acceso a los archivos
os.chdir('./test')
print("os.getcwd()", os.getcwd())