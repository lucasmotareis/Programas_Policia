# Generated by Selenium IDE
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import guardar_arquivos
import funcoes_transparencia
import os



class TestTransparencia():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
 
  def test_transparencia(self):
    matricula_militar = funcoes_transparencia.pegaMatriculaMilitares()
    lista_meses = ['2024/01','2023/12','2023/11','2023/10','2023/09','2023/08','2023/07','2023/06','2023/05','2023/04','2023/03','2023/02']
    self.driver.get("https://transparencia.to.gov.br/#!servidores")
    self.driver.set_window_size(1200,1000)
    wait = WebDriverWait(self.driver, 20)
    time.sleep(15)
    elemento = wait.until(EC.visibility_of_element_located((By.ID, "gwt-uid-3")))
    elemento.clear()
    time.sleep(1)
    elemento.send_keys('Polícia Militar do Estado do Tocantins')
    time.sleep(1)
    elemento.send_keys(Keys.ENTER)
    for matricula in matricula_militar:
        if funcoes_transparencia.militarBaixadoOuNaoMatricula(matricula):
          continue
        elemento = wait.until(EC.visibility_of_element_located((By.ID, "gwt-uid-7")))
        elemento.clear()
        time.sleep(1)
        elemento.send_keys(matricula)
        elemento.send_keys(Keys.ENTER)
        time.sleep(1)
        for mes in range(12):
            arquivos_anteriores = set(os.listdir('C:/Users/lucas/Downloads/'))
            elemento = wait.until(EC.visibility_of_element_located((By.ID, "gwt-uid-11")))
            for i in range(7):
              elemento.send_keys(Keys.BACK_SPACE)
              time.sleep(0.1)
            time.sleep(1)
            elemento.send_keys(lista_meses[mes])
            time.sleep(1)
            elemento.send_keys(Keys.ENTER)
            time.sleep(1)
            elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".friendly")))
            time.sleep(1)
            elemento.click()
            time.sleep(1)
            elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".v-grid-cell-focused")))
            time.sleep(1)
            elemento.click()
            time.sleep(1)
            elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".v-menubar-menuitem:nth-child(1) > .v-menubar-menuitem-caption")))
            time.sleep(1)
            elemento.click()
            time.sleep(1)
            elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".borderless-colored")))
            time.sleep(1)
            elemento.click()
            time.sleep(1)
            elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".v-slot-borderless-colored:nth-child(1) .v-button-caption")))
            time.sleep(1)
            elemento.click()
            baixou_ou_nao = funcoes_transparencia.baixouOuNaoArquivoContracheque(set(arquivos_anteriores))
            while baixou_ou_nao == False:
              elemento.click()
              time.sleep(3)
              baixou_ou_nao = funcoes_transparencia.baixouOuNaoArquivoContracheque(set(arquivos_anteriores))
            time.sleep(1)
            elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".friendly:nth-child(1) .v-button-caption")))
            time.sleep(1)
            elemento.click()
            time.sleep(3)
    
        funcoes_transparencia.criarPastaDoServidor()
        time.sleep(2)
    quit()




      
