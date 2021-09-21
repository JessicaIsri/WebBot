# Webbot

Projeto de Webbot - FATEC Prof. Jessen Vidal - São José dos Campos / 2019

# Resumo do projeto desenvolvido
O sistema em questão tinha como objetivo o desenvolvimento de um webbot que fosse capaz de solucionar um problema da atualidade. O problema a ser resolvido era de livre escolha dos participantes.
Tendo isso em mente a aplicação tem o objetivo de auxiliar na pesquisa de mercado para pequenas empresas da cidade de São José dos Campos, através da coleta de dados no portal da Receita Federal e com os dados de CEP localizar a latitude e longitude aproximada para além de de dados adicionais do endereço, dessa forma sendo possivel a analise da concorrencia de um determinado estabelecimento em um determinado ramo em um local especifico da cidade de São José dos Campos.

# Técnologias utilizadas na solução
As seguintes tecnologias foram adotadas na solução desenvolvida:
- Python: O python é uma linguagem de programação interpretada, muito utilizada para analises de dados. Possui como sua principal vantagem e facilidade de aprendizado, sintaxe amigavél além de ser poderosa para diversos usos.
- Django: Django é um framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view.
- Selenium: Selenium é um framework portátil para testar aplicativos web, porém pode ser adptado para o desenvolvimento de bots que necessitem de interação direta com uma interface.
- MongoDB: O MongoDB é um sistema de banco de dados NoSql orientado a documentos, com o uso similar ao JSON.

# Contribuições individuais/pessoais
Contribui com o desenvolvimento do bot que recuperava os arquivos fornecedos pela Receita Federal, rotinas de leitura dos arquivos dos quais cada um continha aproximadamente 5GB de dados. Para além do metodo de recuperação dos dados espaciais através do dado do CEP.

Motor de extração de dados Geograficos
- Class Driver
```
def __init__(self, cep):
        self.driver = webdriver.Chrome(executable_path='C:\\webbot\\chromedriver')
        self.wait = WebDriverWait(self.driver, 5)
        self.cep = cep
        self.openSite()
```
Como podemos observar pelo construtor da classe, temos algumas configurações padrões a serem feitas para o correto funcionamento do bot que irá extrair os arquivos, tais como
- Driver a ser utilizado pelo Selenium:  O driver é um executavél que permite a manipulação de ações automáticas em cima da janela do navegador, sendo assim é necessario indicar o caminho do executavel na inicialização do Webdriver. Esse arquivo varia de navegador para navegador, por exemplo no chrome e chromium utilizamos o chromedrive, enquanto que no Mozila Firefox temos o GeckoDrive
- Wait: semelhante a função sleep ele adiciona um modo de espera ao driver, algumas ações não tem reações imediatas, por exemplo ao clickar sobre um botão de refresh, temos de aguardar até que a ação seja concluida, desse modo precisamos aguardar esse evento se concluir. Com base nisso temos de definir um tempo máximo para que essa ação seja concluida.
- Class Driver, método openSite
```
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
            print(endereco, latitude, longitude)
        except:
            cnpj = self.driver.find_element_by_xpath('/html/body/main/div[7]/div/div[1]/p[1]').text
            print(cnpj)
```
O código acima traz uma exemplificação da extração dos dados presentes no site https://www.mapacep.com.br/index.php, após ser realizado o filtro por cep.

# Aprendizados Efetivos
O principal aprendizado se deu com a leitura dos dados, uma vez que cada arquivo continha no minimo 5GB, logo não sendo possivél carrega-los inteiramente de uma unica vez sem sobrecarregas a memoria do sistema, sendo inicialente utilizado uma fragmentação do arquivo, porém posteriormente foi adotado o pandas devido sua melhor performace com os dataframes, alem de proporcionar uma serie de ferramentas uteis para a manipulação dos dados.
