#importar las librerias necesarias
import cyclone.web
import sys

from twisted.internet import reactor
from twisted.python import log

#Maneja si el HTTP request sera POST o GET
class MainHandler(cyclone.web.RequestHandler):
    def get(self):
      #Escribe el mensaje a pantalla
      #importar Bootstrap
        boot='<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">'
        header=self.write('<h2 style="text-align: center;">HELLO WORLD</h2>''<br><br>')
        footer=self.write('<p style="text-align: center; font-family: verdana; color: purple;">HOLA, MI NOMBRE ES FERNANDO.</p>')
        #variable cualquiera para cada componente
        button=self.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous"><button type="button" class="btn btn-warning">Warning</button>')
        #regresar cada uno de los componentes
        return(boot)
        return(header)
        return(footer)
        return(button)
#define la aplicacion de cyclone, pasando la
#ruta, junto con el metodo HTTP
if __name__ == "__main__":
    application = cyclone.web.Application([
        (r"/", MainHandler)
    ])

#Para est parte usa un metodo de salida stdout
#junto con listenTCP para abrir el puerto
#se elige la IP en interface
#Por ultimo se usa un reactor.run que conecta con el servidor y abre el puerto.
    log.startLogging(sys.stdout)
    reactor.listenTCP(8080, application, interface="0.0.0.0")
    reactor.run()

#y la app funciona
   