# Feito por: Mainjota
# http://twitter.com/mainjota
# Como usar:
# Baixe o driver do google chrome da versão do seu navegador.
# Executa o programa, tanto em sua IDE quanto em Python ou se quiser pode até transformar em .exe usando o pyinstaller.
# Vai pedir o link do video que quer impulsionar, depois vai abrir 3 abas do chrome, da play nas 3 guias e muta. 
# O bot vai dar refresh de 10 em 10 secs no video (da pra mudar, só trocar o numero dentro do sleep na linha 26 pelo numero de segundos.)



from selenium import webdriver
from time import sleep

x = input('Link do vídeo: ')

driver1 = webdriver.Chrome(executable_path="PATH DO CHROMEDRIVER AQUI")
driver2 = webdriver.Chrome(executable_path="PATH DO CHROMEDRIVER AQUI")
driver3 = webdriver.Chrome(executable_path="PATH DO CHROMEDRIVER AQUI")

driver1.get(x)
driver2.get(x)
driver3.get(x)


while True:
    sleep(10)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    