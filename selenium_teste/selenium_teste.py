from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Pasta de download
download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)

# Configuração do Chrome
options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
})
options.add_experimental_option("detach", True)  # Mantém o navegador aberto

# Inicializa o driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://ri.magazineluiza.com.br/ShowCanal/Download.aspx?Arquivo=qZk/QIMZldvMsM18h5lcHg==")
print(driver.title)

# Aceitar cookies, se aparecer
try:
    aceitar_cookies = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Aceitar")]'))
    )
    aceitar_cookies.click()
    print("Cookies aceitos")
except:
    print("Botão de cookies não encontrado ou já fechado")

# Detecta iframe, se houver
iframes = driver.find_elements(By.TAG_NAME, "iframe")
if iframes:
    print(f"{len(iframes)} iframe(s) encontrado(s), mudando contexto...")
    driver.switch_to.frame(iframes[0])  # usa o primeiro iframe
else:
    print("Nenhum iframe encontrado")

# Aguarda o botão de download aparecer
try:
    download_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" or @value="Download"] | //a[contains(@href, "Download.aspx")]'))
    )
    download_link.click()
    print("Clique no download realizado com sucesso!")
except:
    print("Não foi possível localizar ou clicar no link de download")
    driver.save_screenshot("erro_selenium.png")
    print("Screenshot salva como erro_selenium.png para depuração")

# Aguarda alguns segundos para o download iniciar
time.sleep(5)
print(f"O arquivo deve estar na pasta: {download_dir}")

input("Pressione Enter para fechar o navegador...")
driver.quit()
