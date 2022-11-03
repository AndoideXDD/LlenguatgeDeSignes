from ._anvil_designer import PruebaTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from time import sleep 
from ..Module1  import randoms
class Prueba(PruebaTemplate):
  def __init__(self, **properties):


    self.init_components(**properties)
    
    # Hace el boton de reiterar oculto al principio y la nota oculta tambien
    
    self.reintentar.visible = False  
    self.card_1.visible = False
    
    # Esconde los label que guardan la información de la respuesta correcta
    
    self.respuestas.visible = False 
    
    # Extrae preguntas aleatorias para que no se repitan en el examen 
    signo = []
    signo2 = []
    signo3 = []
    signo4 = []
    signo5 = []
    signo6 = []
    signo7 = []
    # Esta parte permite hacer que no se repitan las preguntas a coste eso si de mucha lentitud, seria pues recomendable su mejora 
    listasignos = []
 
    listasignos   = randoms(False,True)
    
    signo = listasignos[0]
    signo2 = listasignos[1]
    signo3 = listasignos[2]
    signo4 = listasignos[3]
    signo5 = listasignos[4]
    signo6 = listasignos[5]
    signo7 = listasignos[6]
    
            
    # Guarda las respuestas
    
    self.Corregir.text = signo[1]
    self.Corregir2.text = signo2[1]
    self.Corregir3.text = signo3[1]
    self.Corregir4.text = signo4[1]
    self.Corregir5.text = signo5[1]
    self.Corregir6.text = signo6[1]
    self.Corregir7.text = signo7[1]
  
    # Coloca las imagenes de los ejercicios de los signos del abecedario 
  
    self.signoImage_1.source = signo[0]
    self.signoImage_2.source = signo2[0]
    self.signoImage_3.source = signo3[0]
    self.signoImage_4.source = signo4[0]
    self.signoImage_5.source = signo5[0]
    self.signoImage_6.source = signo6[0]
    self.signoImage_7.source = signo7[0]
    
    
  # Al darle al boton calcula la nota
  
  def button_1_click(self, **event_args):
    # A base de mirar donde se guarda la información calcula nota 
    self.card_1.visible = False
    puntiacion = 0.0 
    
    if self.signo1.text.lower().strip() == self.Corregir.text:
      
      puntiacion = puntiacion + 1
      
    if   self.signo2.text.lower().strip() == self.Corregir2.text:
      
      puntiacion = puntiacion + 1
    
    if   self.signo3.text.lower().strip() == self.Corregir3.text:
      
      puntiacion = puntiacion + 1
      
    if   self.signo4.text.lower().strip() == self.Corregir4.text:
      
      puntiacion = puntiacion + 1
      
    if   self.signo5.text.lower().strip() == self.Corregir5.text:
      
      puntiacion = puntiacion + 1
      
    if   self.signo6.text.lower().strip() == self.Corregir6.text:
      
      puntiacion = puntiacion + 1
      
    if   self.signo7.text.lower().strip() == self.Corregir7.text:
      
      puntiacion = puntiacion + 1
      
    self.ejerciciosParaCorregir.visible = False 
    self.button_1.visible = False 

    self.notaa.text = round(puntiacion/7*10,2)
    self.aciertos.text =  str(int(puntiacion)) + "/7"
    # Si aprueba sale una imagen felicitando con un tick
    
    if round(puntiacion/7*10,2) >= 5:
      self.call_js("PlaySound")
      self.bienMal.source = "https://enesarrate.files.wordpress.com/2015/07/lg-green-tick-simple.png"
    
    # Si suspende sale una imagen de cruz de error y da acceso a un boton para reinitar
    
    if round(puntiacion/7*10,2) <= 5:
      
      self.call_js("MalHecho")
      self.reintentar.visible = True 
      self.bienMal.source = "https://png.pngtree.com/png-vector/20210225/ourlarge/pngtree-error-cross-png-image_2951813.jpg"
    
    self.card_1.visible = True
    
    # Dice las respuestas 
    
    self.respuestas.visible = True
    
    
    
  # Este es el boton de reiniciar la prueba para generar otra prueba    
  
  def reintentar_click(self, **event_args):
    
    open_form('Prueba')

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Inicio')
