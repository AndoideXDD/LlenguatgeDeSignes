from ._anvil_designer import Teoria_InicialTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Teoria_Inicial(Teoria_InicialTemplate):
  def __init__(self, **properties):
    
    self.init_components(**properties)
    
    # Econde las preguntas de la teoria 
    
    self.Preguntas_1.visible = False
    self.drop_down_1.background = "Primary"
  # Al darle a este boton muestra las respuestas y esconde la teoria 
  
  def ejercicio_click(self, **event_args):
    
    self.Preguntas_1.visible = True
    self.indtroduccion.visible = False
  
  # Ejercicio de multiples opciones con una correcta 

  def respuesta_click(self, **event_args):
    
    # Coje la respuesta de la barra de selección 
    
    textAnswer = self.drop_down_1.selected_value
    
    # En caso de ser correcta la respuesta muestra un mensaje de correcto cambia
    # el nombre del boton por correcto 
    
    if textAnswer == "La dominante":
      self.call_js("PlaySound")
      self.respuesta.text = "Correcto"
      Notification("Correcto!").show()
    
    if textAnswer != "La dominante":
      
      self.call_js("MalHecho")
    
    # Si todas las preguntaas son correctas deja mostrar la segunda 
    # parte de la teoria
    if self.button_1.text == "Correcto" and self.respuesta.text == "Correcto":
        open_form('Inicio.Vocales', my_parameter="an_argument")

  # Ejercicio de seleccionar si es correcta o no la respuesta 
  
  def button_1_click(self, **event_args):
    
    # Guarda las respuesta en estas variables 
    
    seleccionSeUsaTodo = self.check_box_2.checked
    seleccionUsarUnaMano = self.check_box_1.checked
    seleccionUsarExpresiones = self.check_box_3.checked 
    Caraenfadado = self.check_box_4.checked 
    
    # Mira si las respuestas son correctas 
    
    if seleccionUsarExpresiones == True: 
      if seleccionUsarUnaMano == False:
        
      
        if seleccionSeUsaTodo == True:
          if Caraenfadado == True:
            
            self.call_js("PlaySound")
            # En caso de ser correcta la respuesta muestra un mensaje de 
            # correcto cambia el nombre del boton por correcto 
            
            self.button_1.text = "Correcto" 
            Notification("Correcto!").show()
            
            # Si todas las preguntaas son correctas deja mostrar la segunda 
            # parte de la teoria
            if self.button_1.text == "Correcto" and self.respuesta.text == "Correcto":
              open_form('Inicio.Vocales', my_parameter="an_argument")
              
             
          else:
            self.call_js("MalHecho")
        else:
          self.call_js("MalHecho")
        
      else:
        self.call_js("MalHecho")
    else:
      
      self.call_js("MalHecho")
  

    
  #Esta parte tiene la función de dar acceso a las diferentes partes de la web

  def TeoriaInicial_click(self, **event_args):
    
    open_form('Inicio.Teoria_Inicial', my_parameter="an_argument")

  def Consonantes_click(self, **event_args):
    
    open_form('Inicio.Consonantes', my_parameter="an_argument")

  def Vocales_click(self, **event_args):
    
    open_form('Inicio.Vocales')
