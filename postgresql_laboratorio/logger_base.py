# la libreria de warnognin permite potenciar los mensajes por consola almacenarlos en otra parte, o mostrarlos en determinado formato
import logging

# variable publica usada por otros archivos
logger = logging

# Configurando la forma para controlar el nivel de importancia de las alertas
"""
level=logger.DEBUG  // especifica el nivel de relevancia
handlers=[logger.FileHandler('log_datos.txt'), logger.StreamHandler]  // medios en los que se mostrara las altertas
    .FileHandler('name_archivo.ext')  # archivo donde se almacenaran
    .StreamHandler() # especifrica que se mostrara por consola
format=''  #especifca como se registrara la formateada del string de los valores a mostrar en el log
    asctime # timestamp de ejecucion
    levelname  # nivel de error
    [filename]  # nombre del arhivo que provoco el error
    [lineno]  # # numero de linea de error
    message  # string mensaje pasado por parametro
datefmt='formato de fecha a mostrar'
"""
logger.basicConfig(level=logger.DEBUG,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%m/%d/%Y %I:%M:%S %p',
                   handlers=[logger.FileHandler('log_datos.log'), logger.StreamHandler()])

# __name__ variable reservada de py retorna el nombre del arhivo ejecutado
# para este caso si la ejecucion es el mismo archivo retorna __main__
if __name__ == '__main__':
    logger.error('Prueba error')
    logger.info('Prueba Info')
    logger.debug('Prueba debug')
    logger.warning('Prueba warnign')
