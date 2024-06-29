import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada: ")
#dataInicial = input("Digite a data inicial: ")
#dataFinal = input("Digite a data final: ")
#Código ação petrobras: PETR4.SA
dados = yfinance.Ticker(ticker).history(start = "2020-01-01", end = "2020-12-31")

fechamento = dados.Close

maximo = round(fechamento.max(),2)
minimo = round(fechamento.min(),2)
valor_medio = round(fechamento.mean(),2)

destinatario = "douglas.ferreirag@gmail.com"
assunto = "Análises do Projeto 2020"

mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maximo}
Cotação mínima: R${minimo}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

Atte.



"""

# Arir o navegador e ir para o gmail.

webbrowser.open("www.gmail.com")
time.sleep(20)

#Configurando uma pausa de 3 segundos 

pyautogui.PAUSE = 10

#clicar no botão escrever

pyautogui.click(x=175, y=160)

#digitar o email do destinatário e teclar tab
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")


#digitar o assunto do email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#digitar o email a mensagem e teclar tab
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

#clicar no botão enviar
pyautogui.click(x=844, y=686)

#fechar o gmail

pyautogui.click("ctrl", 'f4')

print("Email enviado com sucesso.")