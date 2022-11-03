from ._anvil_designer import VocalesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Module1
from time import sleep
 

class Vocales(VocalesTemplate):
  
  def __init__(self, **properties):
    
    self.init_components(**properties)
    
    # Oculta las correcciones de los ejercicios 
    
    self.Correccion.visible = False 
    self.CorreccionU.visible = False  
    self.CorrecionE.visible = False 
    self.CorrecionO.visible = False 
    self.correccionI.visible = False 
    
    # Esconde los ejercios al inicio 
    
    self.ejerciciosVocales.visible = False
   
  
  # Importa las funciones de los ejercicios
  
  
    
  
  # Esconde la teoria y muestra los ejercicios al darle al boton 
  
  def button_2_click(self, **event_args):
    
    self.ejerciciosVocales.visible = True
    self.Teoria_2.visible = False
    
  #Esta parte tiene la función de dar acceso a las diferentes partes de la web

  def TeoriaInicial_click(self, **event_args):
    
    open_form('Inicio.Teoria_Inicial', my_parameter="an_argument")

  def Consonantes_click(self, **event_args):
    
    open_form('Inicio.Consonantes', my_parameter="an_argument")

  def Vocales_click(self, **event_args):
    
    open_form('Inicio.Vocales')
  
  #______________________________________________________________________________________________________-
  # Estos son los ejercicios 
  #______________________________________________________________________________________________________
  def button_3_click(self, **event_args):
    
    
    
    # Corrige el primer ejercicio (a) el if muestra una 
    # animacion de correcto 
    # , el else en cambio muestra la correccion y la animacion de una cruz
    
    
    
    if self.significaA.text.lower().strip() == "a":
      self.call_js("PlaySound")
          
      self.image_11.source = Module1.animacion(True)
      self.button_3.visible = False
      self.significaA.visible = False
      sleep(2)
      self.image_11.visible = False 
      self.button_3.text = "Correcto"
      
          
      
      
      Notification("Correcto!").show()
    
    else:
    
      self.call_js("MalHecho")
      self.button_3.visible = False
      self.image_11.source = Module1.animacion(False) 
      self.significaA.visible = False
      self.Correccion.visible = True 
      sleep(2)
      self.image_11.visible = False 
      self.Correccion.visible = False 
      
      # Deja que se intente el ejercicio otra vez 
      
      self.button_3.visible = True
      self.significaA.text = ""
      self.significaA.visible = True
      self.image_11.source = "https://i.pinimg.com/564x/30/14/a9/3014a91617fb75cf90c22f4976eaf31e.jpg"
      self.image_11.visible = True 
    
    # Mira si todos los ejercicios están bien para pasar a la siguieente parte 
    
    B1 = self.button_3.text
    B2 = self.button_4.text
    B3 = self.button_5.text
    B4 = self.button_5_copy.text
    B5 = self.button_5_copy_2.text 
  
  
  
    if B1 == "Correcto" and B2 == "Correcto":
      
      if B3 == "Correcto" and B4 == "Correcto":
      
        if B5 == "Correcto":
        
          open_form('Inicio.Consonantes')
    
  def button_4_click(self, **event_args): 
    
    # Corrige el segundo ejercicio (u) el if muestra 
    # una animacion de correcto 
    # , el else en cambio muestra la correccion y la animacion de una cruz
    
    if self.significaU.text.lower().strip() == "u":  
      self.call_js("PlaySound")
      self.image_12.source = Module1.animacion(True)
      self.button_4.visible = False
      self.significaU.visible = False
      sleep(2)
      self.image_12.visible = False 
      Notification("Correcto!").show()
      self.button_4.text = "Correcto"
      
    else:
    
      self.call_js("MalHecho")
      self.button_4.visible = False
      self.image_12.source = Module1.animacion(False) 
      self.significaU.visible = False
      self.CorreccionU.visible = True 
      sleep(2)
      self.image_12.visible = False 
      self.CorreccionU.visible = False 
      
      # Deja que se intente el ejercicio otra vez 
      
      self.button_4.visible = True
      self.significaU.text = ""
      self.significaU.visible = True
      self.image_12.source = "https://i.pinimg.com/originals/f6/bc/e3/f6bce391e4404372ab312d4f76c260fd.jpg"
      self.image_12.visible = True 
          
      
    
      
      
    # Mira si todos los ejercicios están bien para pasar a la siguieente parte 
    
    B1 = self.button_3.text
    B2 = self.button_4.text
    B3 = self.button_5.text
    B4 = self.button_5_copy.text
    B5 = self.button_5_copy_2.text 
  
  
  
    if B1 == "Correcto" and B2 == "Correcto":
      
      if B3 == "Correcto" and B4 == "Correcto":
      
        if B5 == "Correcto":
        
          open_form('Inicio.Consonantes')


  def button_5_click(self, **event_args):
    
    

    # Corrige el tercer ejercicio ( i )
    # el if muestra una animacion de correcto 
    # , el else en cambio muestra la correccion y la animacion de una cruz
    
    if self.significa_I.text.lower().strip() == "i":
      self.call_js("PlaySound")
      self.image_13.source = Module1.animacion(True)
      self.button_5.visible = False
      self.significa_I.visible = False
      sleep(2)
      self.image_13.visible = False 
      self.button_5.text = "Correcto"
      Notification("Correcto!").show()
      
    else:
    
      self.call_js("MalHecho")
      self.button_5.visible = False
      self.image_13.source = Module1.animacion(False) 
      self.significa_I.visible = False
      self.correccionI.visible = True 
      sleep(2)
      self.image_13.visible = False 
      self.correccionI.visible = False 
          
      # Deja que se intente el ejercicio otra vez 
      
      self.button_5.visible = True
      self.significa_I.text = ""
      self.significa_I.visible = True
      self.image_13.source =  "https://i.pinimg.com/originals/bb/8c/82/bb8c82830f05911a94fb89b4ba0897b6.jpg"
      self.image_13.visible = True 
          
    
      
    
    # Mira si todos los ejercicios están bien para pasar a la siguieente parte 
    
    B1 = self.button_3.text
    B2 = self.button_4.text
    B3 = self.button_5.text
    B4 = self.button_5_copy.text
    B5 = self.button_5_copy_2.text 
  
  
  
    if B1 == "Correcto" and B2 == "Correcto":
      
      if B3 == "Correcto" and B4 == "Correcto":
      
        if B5 == "Correcto":
        
          open_form('Inicio.Consonantes')

  def button_5_copy_click(self, **event_args):
    
    # Corrige el quarto ejercicio (o) 
    # el if muestra una animacion de correcto 
    # , el else en cambio muestra la correccion y la animacion de una cruz
    
    if self.significaO.text.lower().strip() == "o":
      self.call_js("PlaySound")
      self.image_13_copy.source = Module1.animacion(True)
      self.button_5_copy.visible = False
      self.significaO.visible = False
      sleep(2)
      self.image_13_copy.visible = False 
      self.button_5_copy.text = "Correcto"
      Notification("Correcto!").show()
      
    else:
    
      self.call_js("MalHecho")
      self.button_5_copy.visible = False
      self.image_13_copy.source = Module1.animacion(False) 
      self.significaO.visible = False
      self.CorrecionO.visible = True 
      sleep(2)
      self.image_13_copy.visible = False 
      self.CorrecionO.visible = False 
      
      # Deja que se intente el ejercicio otra vez 
      
      self.button_5_copy.visible = True
      self.significaO.text = ""
      self.significaO.visible = True
      self.image_13_copy.source = "https://i.pinimg.com/originals/8f/29/e2/8f29e2fd0fd4e541085e7e075c8ba1df.jpg"
      self.image_13_copy.visible = True 
    
    # Mira si todos los ejercicios están bien para pasar a la siguieente parte 
    
    B1 = self.button_3.text
    B2 = self.button_4.text
    B3 = self.button_5.text
    B4 = self.button_5_copy.text
    B5 = self.button_5_copy_2.text 
  
  
  
    if B1 == "Correcto" and B2 == "Correcto":
      
      if B3 == "Correcto" and B4 == "Correcto":
      
        if B5 == "Correcto":
        
          open_form('Inicio.Consonantes')

  def button_5_copy_2_click(self, **event_args):
    
    # Corrige el quinto ejercicio (e) 
    # el if muestra una animacion de correcto 
    # , el else en cambio muestra la correccion y la animacion de una cruz
    
    if self.significaE.text.lower().strip() == "e":  
      self.call_js("PlaySound")
      self.image_13_copy_2.source = Module1.animacion(True)
      self.button_5_copy_2.visible = False
      self.significaE.visible = False
      sleep(4)
      self.image_13_copy_2.visible = False 
      self.button_5_copy_2.text = "Correcto"
      Notification("Correcto!").show()
      
    else:
    
      self.call_js("MalHecho")
      self.button_5_copy_2.visible = False
      self.image_13_copy_2.source = Module1.animacion(False) 
      self.significaE.visible = False
      self.CorrecionE.visible = True 
      sleep(4)
      self.image_13_copy_2.visible = False 
      self.CorrecionE.visible = False 
      
      # Deja que se intente el ejercicio otra vez 
      
      self.button_5_copy_2.visible = True
      self.significaE.text = ""
      self.significaE.visible = True
      self.image_13_copy_2.source = "https://i.pinimg.com/originals/2f/18/08/2f180838758b5a81ae0f1bd30233cdd6.jpg"
      self.image_13_copy_2.visible = True 
      
    # Mira si todos los ejercicios están bien para pasar a la siguieente parte 
    
    B1 = self.button_3.text
    B2 = self.button_4.text
    B3 = self.button_5.text
    B4 = self.button_5_copy.text
    B5 = self.button_5_copy_2.text 
  
  
  
    if B1 == "Correcto" and B2 == "Correcto":
      
      if B3 == "Correcto" and B4 == "Correcto":
      
        if B5 == "Correcto":
        
          open_form('Inicio.Consonantes')
