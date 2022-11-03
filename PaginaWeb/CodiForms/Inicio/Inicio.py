from ._anvil_designer import InicioTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

 


class Inicio(InicioTemplate):
  def __init__(self, **properties):
    
    self.init_components(**properties)
     
    
  # Da acceso a la primera lección  
  
  def buttonStart_click(self, **event_args):
    
    open_form('Inicio.Teoria_Inicial', my_parameter="an_argument")
    
  
  #Esta parte tiene la función de dar acceso a las diferentes partes de la web
  
  def Consonantes_click(self, **event_args):
    
    open_form('Inicio.Consonantes', my_parameter="an_argument")

  def Vocales_click(self, **event_args):
    
    open_form('Inicio.Vocales', my_parameter="an_argument")

  def TeoriaInicial_click(self, **event_args):
    
    open_form('Inicio.Teoria_Inicial', my_parameter="an_argument")
