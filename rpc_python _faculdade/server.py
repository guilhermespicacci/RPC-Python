# Server
# Guilherme  de Souza Spicacci Faria Lima
# 3022200160
import rpyc 
from rpyc.utils.server import ThreadedServer 



class MyService(rpyc.Service):
   # Função Calcula o IMC
   def exposed_CalculaImc(self,peso:float,altura:float):
     classificacao = ""
     imc =(peso/(altura*altura))
     if imc <= 18.5:
         classificacao = "Magreza"
     elif imc >= 18.5 and imc <= 24.9 :
         classificacao = "Normal"
     elif imc >= 25 and imc >= 29.9:
         classificacao = "Sobrepeso"
     elif imc >=30 and imc >= 34.9:
         classificacao = "Obesidade grau I"
     elif imc >= 35 and imc>=39.9:
         classificacao = "Obesidade grau II"
     else:
         classificacao = "Obesidade grau III"
     
     return imc,classificacao
   # Função Equação Segundo Grau
   def exposed_EquacaoSegundo(self, a:float,b:float,c:float):
       if a != 0:
        delta = b**2 - 4 * a * c
 
        if delta < 0:
            print("DELTA = ", delta)
            return f"DELTA = {delta}\nNão existem raízes reais!"
        elif delta == 0:
            x1 = -b/(2*a)
            print("DELTA = ", delta)
            return f"x' = x'' = {x1}"
        else:
            x1 = (-b - (delta)**0.5) / (2 * a)
            x2 = (-b + (delta)**0.5) / (2 * a)
            
            return f"x =  {x1}\nx =  {x2}\n Não é uma equação do 2º grau!"
        #Função Palindromo
   def exposed_retornaPalindromo(self,palavra:str):
        palin =""
        for p in reversed(palavra):
            palin += p
        if palin == palavra:
            return palin
        else:
            return False
       
# Inicia O servidor
if __name__ == "__main__":
    server = ThreadedServer(MyService, hostname='0.0.0.0', port = 18812)
    print('Servidor online')
    server.start()