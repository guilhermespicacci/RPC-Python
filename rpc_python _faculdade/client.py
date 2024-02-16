# Client
# Guilherme  de Souza Spicacci Faria Lima
# 3022200160
# Opc Calcular IMC
 
def Opc1IMC():
    # entrada de dados
    peso = float(input("Informe seu Peso em Kgs: "))
    altura = float(input("Informe sua altura em metros: "))

    # executando função remotamente
    retorno1, retorno2 = requisicao.root.CalculaImc(peso,altura)

    # Saida do IMC 
    print(f"Seu IMC: {retorno1:.2f}\nSua Classificação: {retorno2}")



# Opção de Calcular Equação
 
def Opc2CalcSeg():
    #entrada de dados
    a  = int(input("Informe o a: "))
    b = int(input("Informe o b: "))
    c = int(input("Informe o c: "))
    # executando função remotamente
    retorno = requisicao.root.EquacaoSegundo(a,b,c)
    print(retorno)


# Opção de Calcular Palindromo
def Opc3RetPalin():
    # entrada de dados 
    palavra = str(input("Digite a palavra:  "))
    # executando função remotamente
    retorno = requisicao.root.retornaPalindromo(palavra)
    if retorno == 0 :
      print("Não é um Palíndromo")
    else:
      print(f"O palindromo é {retorno}")

import rpyc
MyIp = "localhost"
Port = 18812
# Conectando ao Servidor
requisicao = rpyc.connect(MyIp, Port)
print("Conectado")

# Switch Case 
opc = {
   1:Opc1IMC,
   2:Opc2CalcSeg,
   3:Opc3RetPalin
   }
while True:
  # leitura do teclado para as opções
  selectop = int(input("1. Calcula IMC\n2. Calcular Equação Segundo Grau\n3. Retorne Palindromo\nOpção: "))
  if selectop == 1 or selectop == 2 or selectop == 3:
     opc[selectop]()
  else:
     print("Opção Invalida")
     pass
 

# Para o Programa
  stop = str(input("Digite Sim para Parar o Programa ")).lower().strip()
  if stop[0] == "s":
    break
  
    
