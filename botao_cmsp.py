import pyautogui
import time
from selenium import webdriver

from emails_e_senhas_de_login import ra, digito, senha_cmsp

def entra_no_site_da_aula():
    # Minimizando a central de sites e esperando 1 segundo
    pyautogui.hotkey('win', 'down')
    time.sleep(1)

    # Mensagem de confirmação
    confirmacao = pyautogui.confirm(text="O código vai começar, não mexa no computador antes da mensagem de fim", title='Confimação', buttons=['Sim', 'Não'])
    
    if confirmacao == 'Sim':
        # Fazendo o navegador
        navegador = webdriver.Chrome()
        navegador.get('https://cmspweb.ip.tv/')
        # Esperando o site carregar
        while len(navegador.find_elements_by_id('logoImg')) == 0:
            time.sleep(1)
        # Clicando no botão de login
        navegador.find_element_by_id('access-student').click()
        time.sleep(1)
        # Fazendo login
        navegador.find_element_by_id('ra-student').send_keys(ra)
        navegador.find_element_by_id('digit-student').send_keys(digito)
        navegador.find_element_by_id('password-student').send_keys(senha_cmsp)
        navegador.find_element_by_id('btn-login-student').click()
        # Esperando a página principal carregar
        while len(navegador.find_elements_by_name('Canal da 3ª Série do Ensino Médio')) == 0:
            time.sleep(1)
        time.sleep(1)
        # Clicando nas turmas
        navegador.find_element_by_xpath('//*[@id="chng"]/div[2]').click()
        #Esperando "Turmas" carregar
        while len(navegador.find_elements_by_xpath('//*[@id="lproom_r6dd4591c9caaa3247-l"]/div/div/span[1]')) == 0:
            time.sleep(1)
        time.sleep(1)
        # Clicando em na minha turma
        navegador.find_element_by_xpath('//*[@id="lproom_r6dd4591c9caaa3247-l"]/div/div/span[1]').click()
        # Esperando a sala carregar
        while len(navegador.find_elements_by_id('hp__Channel__')) == 0:
            time.sleep(1)
        time.sleep(1)
        # Clicando nas tarefas
        navegador.find_element_by_xpath('//*[@id="channelTaskList"]').click()
        # Mensagem falando que acabou
        time.sleep(1)
        pyautogui.alert(text = 'Acabou.')
    else:
        pyautogui.alert("O programa não será executado, pode mexr no computador.")