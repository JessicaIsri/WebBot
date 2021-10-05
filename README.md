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

### Motor de extração de dados Geograficos
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
### Processo de Leitura
```
b = 102400
kb = b*100
def read_in_chunks(file_object, chunk_size=kb):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


f = open('E:\\FATEC\\PI\\Files\\K3241.K03200DV.D90805.L00001')
count = 1
for piece in read_in_chunks(f):
    print(piece)
    new = open('E:\\FATEC\\PI\\Files\\frags\\frag'+str(count)+'.txt', 'w')
    new.writelines(piece)
    new.close()
    count += 1
```

**O uso do yield:** O yield cria um generator, uma lista de dados que serão consumidos sob demanda, sendo assim pode ser utilizado para uma melhor abstração do codigo. Nesse caso em especifico era necessário ele foi utilizado para fragmentar arquivos txt com mais de 5Gb, que seriam grandes demais para ler de uma unica vez. Logo o codigo retora os dados presentes para cara "pedaço" de 10mb, um novo arquivo é gerado.



# Aprendizados Efetivos
Com base nas rotinas desenvolvidas, pode se  absorver o uso do generator para criar estados de codigo que serão aproveitados ao longo da execução, posteriormente foi cogitado o uso do pandas para tal, uma vez que ele lida com a manipulação de dataframes, logo, além de apresentar melhor desempenho ainda entrega uma serie de funções uteis e facilidades para o uso dos dados principalmente quando está aliado ao numpy.
Para o caso do webbot, foi essencial o uso do wait para a espera dos eventos do navegador, e dessa maneira evitar erros relacionados a falta de algum elemento na pagina.
Contudo, pode se afirmar que o real aprendizado se deu em relação ao inicio da manipulação dos dados contanto quase que exclsivamente das bibliotecas nativas da propria linguagem do python.
