# Aqui es guardan les funcions globals de la pagina creats en un modul on es pot importar com objecta i cridar la funció 
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from time import sleep 
import random

texto = ["a","b","c","ch","d","e","f","g","h","i","j","k","l","ll","m","n","ñ","o","p","q","r","rr","s","t","u","v","w","x","y","z"]

c = ["https://i.pinimg.com/564x/07/dc/94/07dc946dc2f7a42f7dbfeb6ad6451cf4.jpg",
             "https://i.pinimg.com/736x/71/1f/9b/711f9b23816978b47f74f3227fde419c.jpg",
             "https://i.pinimg.com/564x/3c/3e/bd/3c3ebdce0ccab4e3ccf3c2d2658c7623.jpg",
             "https://i.pinimg.com/564x/cb/d9/84/cbd9849792054a30679d77f2cfdd99d6.jpg",
             "https://i.pinimg.com/originals/c1/19/24/c119243a49304f6f20b4e01247c63e91.jpg" ,
             "https://i.pinimg.com/564x/a9/ea/f5/a9eaf59c7270bcb0c1dee68d2ff75a72.jpg",
             "https://i.pinimg.com/564x/dd/6d/52/dd6d5272d7f4f72d4eb350ff639d2a3c.jpg",
             "https://i.pinimg.com/564x/29/42/a7/2942a7e849292b46e2320114cea52e19.jpg",
             "https://i.pinimg.com/564x/41/1e/77/411e774911cc36434dfd5c7dc3c6a990.jpg",
             "https://i.pinimg.com/originals/8f/8b/62/8f8b62e2c0a6fb89a33c77a4671f678b.jpg",
             "https://i.pinimg.com/originals/ab/84/0a/ab840a3b7b3bb24ed22c2876f02ca746.jpg" ,
             "https://i.pinimg.com/originals/ed/73/91/ed73911b881c1cb161bfdb95211f77fe.jpg",
             "https://i.pinimg.com/originals/bf/46/eb/bf46ebe4ff389214746d7bce27fd2fd2.jpg",
             "https://i.pinimg.com/originals/85/b0/07/85b00738e1e27c6e8df2869c1687b515.jpg",
             "https://i.pinimg.com/originals/fb/7e/22/fb7e224cd8edcb69573227241ca39404.jpg",
             "https://i.pinimg.com/originals/e4/16/51/e41651abcfce5381daaef60af05cdbad.jpg" ,         
             "https://i.pinimg.com/originals/c6/1a/74/c61a74baf1159be0c42b38fd18bf4873.jpg" ,
             "https://i.pinimg.com/564x/e4/61/13/e46113cd44f799f4b7f6c1bff93dde64.jpg",
             "https://i.pinimg.com/originals/50/4a/2c/504a2c08a23fa9343be94bb4ebf32fe4.jpg",
             "https://i.pinimg.com/originals/20/94/b8/2094b8e26bac1a09a4e9feb1b5448751.jpg" ,
             "https://i.pinimg.com/564x/cf/42/99/cf4299d6fda5d0336d81e0142071833d.jpg" ,
             "https://i.pinimg.com/originals/2a/a2/0a/2aa20a3564fe918d867da73088741473.jpg",
             "https://i.pinimg.com/originals/0b/fb/2e/0bfb2ebc324b123fede9a1b87a96a03c.jpg" ,
             "https://i.pinimg.com/originals/ea/a1/ba/eaa1ba0898c7e419b24adbf63c17ef37.jpg" ,
             "https://i.pinimg.com/564x/52/bf/6f/52bf6f72659cbb21d95546023678baac.jpg" ,
             "https://i.pinimg.com/originals/8a/ea/43/8aea435a0c2d7672da2a119658c3443a.jpg" ,  
             "https://i.pinimg.com/originals/90/74/5f/90745fe86847b8bd527326b4e07ed8e5.jpg ",
             "https://i.pinimg.com/564x/25/33/16/25331636d30c743345b0e75726514835.jpg",
             "https://i.pinimg.com/originals/de/6b/72/de6b7247502b55f550ed30fae5566760.jpg ",
             "https://i.pinimg.com/originals/30/d4/7f/30d47f50a2832c92f1d0b34f9c1318df.jpg "

            ]

def animacion(x):
  
  # Si pones True te devuelve el link de la animacion de "correcto"
  if x == True: 
    
    return "https://media3.giphy.com/media/PkdAzq9yBI3Gv7GUrP/giphy.gif?cid=ecf05e479ifbpypelhwbohs8g8o1f1iomfiq46p1i9xsp00s&rid=giphy.gif&ct=g"
  
  # Si pones False te devuelve el link de la animacion de "incorrecto"
  else:
    
    return "https://i.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.webp"
  

# Genera los ejercicios del abecedario
  
def randoms(soloNuevoejercicio, randomSinRepetir):
    
  if soloNuevoejercicio == True:
     

      

      x = random.randint(0,len(c)-1)
      return [c[x], texto[x]]
    
  if randomSinRepetir == True: 
      
      examen = random.sample(abecedario, 7)
      lista = []
      lista2 = []
      
      for d in examen:

        lista.append(abecedario.index(d))

      for f in lista:

        lista2.append([imagenesAbecedario[f],abecedario[f]])

        
        
      return lista2 
    
# Genera la traduccion 

def traducir(letra):
  
  letra = letra.lower().strip()
  contador = -1
  for abecedario in texto:
    contador = contador + 1
    if abecedario == letra:
        
      return c[contador]
         
      break 
        
