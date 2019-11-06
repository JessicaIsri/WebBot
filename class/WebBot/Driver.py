from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class Driver:
    def __init__(self, cep=False):
        directory = 'E:\\FATEC\\PI\\Files'
        chrome_options = webdriver.ChromeOptions()
        preferences = {"download.default_directory": directory}
        chrome_options.add_experimental_option("prefs", preferences)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\\webbot\\chromedriver')
        self.wait = WebDriverWait(self.driver, 5)
        self.cep = cep
        self.openSite()

    def openSite(self):
        self.driver.get("https://www.mapacep.com.br/index.php")
        self.wait.until(EC.presence_of_element_located((By.ID, 'keywords')))
        self.driver.find_element_by_id('keywords').send_keys(self.cep)
        self.driver.find_element_by_xpath('/html/body/header/div[1]/div/div[2]/div/form/span/button').click()
        sleep(10)
        try:
            text = self.driver.find_element_by_xpath('/html/body/main/div[3]/div/div[1]/p').text.split('\n')
            endereco = text[0]
            latitude = text[3]
            longitude = text[4]
            return [latitude, longitude, endereco]
            # print(endereco, latitude, longitude)
        except:
            cnpj = self.driver.find_element_by_xpath('/html/body/main/div[7]/div/div[1]/p[1]').text
            print(cnpj)


    def getArchives(self):
        self.driver.get(
            'http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj')
        links = self.driver.find_elements_by_css_selector('a.external-link')
        for link in links:
            link.click()
            sleep(1)
        self.waitDownload()

    def waitDownload(self):
        if not self.driver.current_url.startswith("chrome://downloads"):
            self.driver.get("chrome://downloads/")
            # elemento = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftSpacer"]/h1')))

        retorno = self.driver.execute_script("""
                var items = downloads.Manager.get().items_;
                if (items.every(e => e.state === "COMPLETE"))
                    return items.map(e => e.fileUrl || e.file_url);
                else
                    return false
                """)
        # print(retorno)
        count = 0
        while retorno == False and count < 15:
            sleep(1)
            retorno = self.driver.execute_script("""
                var items = downloads.Manager.get().items_;
                if (items.every(e => e.state === "COMPLETE"))
                    return items.map(e => e.fileUrl || e.file_url);
                else
                    return false
                """)
            count += 1
            # print(retorno)
        return
