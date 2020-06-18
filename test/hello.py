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
        header=self.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous"><h1 class="text-light bg-dark">MI PRIMER FORMULARIO</h1>')
        body=self.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous"><form><div class="form-group"><label for="exampleFormControlInput1">MATRICULA</label><input type="number" class="form-control" id="ControlInput1" placeholder="17180000"></div><div class="form-group"><label for="exampleFormControlInput1">NOMBRE</label><input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Juan"></div><div class="form-group"><label for="exampleFormControlInput1">PRIMER APELLIDO</label><input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Perez"></div><div class="form-group"><label for="exampleFormControlInput1">SEGUNDO APELLIDO</label><input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Gonzalez"></div><div class="form-group"><label for="exampleFormControlInput1">EDAD</label><input type="number" class="form-control" id="exampleFormControlInput1" placeholder="18"></div><div class="form-group"><label for="exampleFormControlInput1">FECHA DE NACIMIENTO</label><input type="date" class="form-control" id="exampleFormControlInput1" placeholder=""></div><div><select class="form-control form-control"><option>Hombre</option><option>Mujer</option><option>Otro</option></select></div> <div><label for="validationDefault04">Estado</label><select class="custom-select" id="validationDefault04" required><option selected disabled value="">Choose...</option><option>...</option></select></div><br><br>')
        #variable cualquiera para cada componente
        button=self.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous"><button type="button" class="btn btn-warning">ENVIAR</button>')
        #regresar cada uno de los componentes
        return(boot)
        return(header)
        return(body)
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
   