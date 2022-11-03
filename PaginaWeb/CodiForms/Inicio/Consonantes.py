from ._anvil_designer import ConsonantesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Module1 import animacion
from ...Module1 import randoms
from ...Module1 import traducir
from time import sleep 

class Consonantes(ConsonantesTemplate):
  
  def __init__(self, **properties):
  
    self.init_components(**properties)
    #__________________________________________________________________________________
    # Como funciona el dar la respuesta si no la sabes
    #__________________________________________________________________________________
    
    # Esconde las partes de la correcion 
    self.decirRespuesta.visible = False 
     
    
    #__________________________________________________________________________________
    # Como funciona el corrector
    #__________________________________________________________________________________

    # Ocultamos la imagen
    # luego utilizaremos la funcion animacion que esta más abajo para poder mostrarla
    
    self.animacioncorrector.visible = False 
    
    
    
    
    
    
    #__________________________________________________________________________________
    # Como funciona el ejercicio
    #__________________________________________________________________________________
    
    # Genera la pregunta aleatoria llamando a una función de Jupyter Notebook 
    #y cambiando la imagen y la información de donde se guarda la respuesta
    #por la del signo generado
    
    signo = randoms(True,False)
    self.ejemplo.source = signo[0]
    
    
    # En este objeto guardo los datos de la pregunta aleatoria para practicar 
    
    self.quesoy.visible = False
    self.quesoy.text = signo[1]
    
    # Oculta el boton de confirmacion de la pagina 
    
    self.examenConfirmacion.visible = False 
  
  
    
    
  # Al darle el boton para generar otro ejercicio genera otro ejercicio
  
  
  
  
  def randomGenerador_click(self, **event_args):
    

    # El lower es para hacer el string en minusculas y 
    # el strip para eliminar espacios en blanco
    if self.practica.text.lower().strip() == self.quesoy.text:
     
      Notification("Correcto!").show()
      
      self.call_js("PlaySound")
      # Aqui hace una pequeña animación para mostrar que es correcto (parte 1)
      # La animación se realizara siempre y cuando el usuario
      #no le de al boton de no animación
      if self.noanimacion.checked == False : 
        self.respuesta.visible = False
        self.animacioncorrector.source = animacion(True)
        self.animacioncorrector.visible = True  
        self.noanimacion.visible = False
        self.ejemplo.visible = False 
        self.practica.visible = False 
        self.randomGenerador.visible = False 
        sleep(2)
      
      # Genera la pregunta aleatoria llamando a una función de Jupyter Notebook 
      #y cambiando la imagen y la información de donde se guarda la respuesta
      #por la del signo generado
      
      
      signo = randoms(True,False)
      self.ejemplo.source = signo[0]
      self.quesoy.text = signo[1]
      
      #Borra la informacion puesta 
      
      self.practica.text = ""
      
      # Aqui se quita la animacion y se vuelbe a mostrar el ejercio 
      # La animación se realizara siempre y cuando el usuario
      #no le de al boton de no animación
      
      if self.noanimacion.checked == False : 
      
        self.animacioncorrector.visible = False 
        self.respuesta.visible = True
        self.noanimacion.visible = True
        self.ejemplo.visible = True 
        self.practica.visible = True 
        self.randomGenerador.visible = True 
      
      
      
      #Enseña la respuesta en la terminal 
      
      
      print(signo[1])
    
    else: 
      
      self.call_js("MalHecho")
      if self.noanimacion.checked == False : 
        self.respuesta.visible = False
        self.animacioncorrector.source = animacion(False)
        self.animacioncorrector.visible = True  
        self.noanimacion.visible = False
        self.ejemplo.visible = False 
        self.practica.visible = False 
        self.randomGenerador.visible = False 
        sleep(2) 
        self.animacioncorrector.visible = False 
        self.respuesta.visible = True
        self.noanimacion.visible = True
        self.ejemplo.visible = True 
        self.practica.visible = True 
        self.randomGenerador.visible = True 

  
  # Estos dos eventos hacen lo siguiente:
  # El primero te enseña el boton de confirmar 
  # El segundo da acceso a la Prueba evaluable 
  
  def examen_click(self, **event_args):
 
    self.examenConfirmacion.visible = True 
  
  def examenConfirmacion_click(self, **event_args):
    
    open_form('Prueba')

  

    
  #Esta parte tiene la función de dar acceso a las diferentes partes de la web
    
    
  def TeoriaInicial_click(self, **event_args):
    
    open_form('Inicio.Teoria_Inicial', my_parameter="an_argument")

  def Vocales_click(self, **event_args):
    
    open_form("Inicio.Vocales")

  def Consonantes_click(self, **event_args):
    
    open_form('Inicio.Consonantes', my_parameter="an_argument")

  def respuesta_click(self, **event_args):
   
    #__________________________________________________________________________________
    # Como funciona el dar la respuesta si no la sabes
    #__________________________________________________________________________________
    # 
    self.decirRespuesta.text = self.quesoy.text
    self.decirRespuesta.visible = True 
    self.noanimacion.visible = False
    self.ejemplo.visible = False 
    self.practica.visible = False 
    self.randomGenerador.visible = False 
    sleep(2)
    self.decirRespuesta.visible = False 
    self.noanimacion.visible = True
    self.ejemplo.visible = True 
    self.practica.visible = True
    self.randomGenerador.visible = True

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    palabra = self.palabra.text 
    for letraDePalabra  in palabra  :
      try:
        sleep(self.tiempo.text)
      
      except:
        sleep(1)
      
      self.traduccion.source =  traducir(letraDePalabra)
  
    
