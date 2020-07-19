# Author: Vanessa Lopes Klein
# Date: 19/07/2020
# Desenvolvido usando o Google colab
#!pip install googletrans  #para poder usar o google translate
import re
from google.colab import files
from googletrans import Translator

translator = Translator()

#Converte numeros romanos em numeros inteiros
def roman_to_int(input):
  nums = {'M':1000,
          'D':500,
          'C':100,
          'L':50,
          'X':10,
          'V':5,
          'I':1}
  sum = 0
  for j in range(len(input)):
    value = nums[input[j]]
    if j+1 < len(input) and nums[input[j+1]] > value:
      sum -= value
    else:
      sum += value
  return sum
  
arq = 'n.txt' # define o nome do arquivo onde contem as anotações
uploaded = files.upload() # necessario para rodar programa no colab
f = open(arq, 'r')
####
simb_interg = []
simb_rom = []
metal= []
valor_metal= []
metais = 0
value_metal = 0

#Definindo a notação de intergalatico para romano

for line in f:
  phrase = line.strip()
  if re.search('\\brepresenta\\b', line.strip(), re.IGNORECASE):
    simb_interg.append(phrase.split()[0])
    simb_rom.append(phrase.split()[2].upper())    
  else:    
    simb_interg.append('null')
    simb_rom.append('null')

f.close()
f = open(arq, 'r')
for line in f:
  phrase = line.strip()
  phrase.split()
  romano = []
  verifica = 0
  if re.search('\\brepresenta\\b', line.strip(), re.IGNORECASE):
    ax = 0
  else:
    for i in range(0,len(phrase.split())):
    
      if phrase.split()[i].lower() == simb_interg[0]:
        romano.append(simb_rom[0])
        verifica = verifica + 1
      elif phrase.split()[i].lower() == simb_interg[1]:
        romano.append(simb_rom[1])
        verifica = verifica + 1
      elif phrase.split()[i].lower() == simb_interg[2]:
        romano.append(simb_rom[2])
        verifica = verifica + 1
      elif phrase.split()[i].lower() == simb_interg[3]:
        romano.append(simb_rom[3])
        verifica = verifica + 1
      elif phrase.split()[i].lower() == simb_interg[4]:
        romano.append(simb_rom[4])
        verifica = verifica + 1
      elif phrase.split()[i].lower() == simb_interg[5]:
        romano.append(simb_rom[5])
        verifica = verifica + 1
      elif phrase.split()[i].lower() == simb_interg[6]:
        romano.append(simb_rom[6])
        verifica = verifica + 1
      
    romano = ''.join(romano)    
    sum = roman_to_int(romano)

  #### verifica o metal e seu valor   
    if re.search('\\bvalem\\b', line.strip(), re.IGNORECASE):      
      for i in range(0,len(phrase.split())):
        if phrase.split()[i].lower() == "valem":
          metal.append(phrase.split()[i-1])
          metais = metais + 1;
          value_metal = float(phrase.split()[i+1]) / sum
          valor_metal.append(value_metal)
### caso 1 de pergunta
    elif re.search('\\bquanto\\b', line.strip(), re.IGNORECASE) and verifica != 0:
      print(phrase, "=" ,sum)
### caso 2 de pergunta
    elif re.search('\\bquantos\\b', line.strip(), re.IGNORECASE) and verifica != 0:      
      for h in range(0,len(phrase.split())):        
        for k in range(0,metais): #no caso 2 é preciso multiplicar o valor pelo metal correspondente       
          translated = translator.translate(metal[k], src = 'pt', dest ='en')
          translated_2 = translator.translate(metal[k], src = 'en', dest ='pt')
          if  phrase.split()[h].lower() == metal[k] or phrase.split()[h].lower() == translated.text or phrase.split()[h].lower() == translated_2.text:
            sum = sum * valor_metal[k]            
            print(phrase, "=" , sum, "créditos")
    elif verifica == 0:
      print("Entrada inválida!")