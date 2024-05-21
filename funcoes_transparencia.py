import os 
import pandas as pd
from unidecode import unidecode
import time



def nomesArquivosContracheque():
    lista_de_arquivos_diretorio = os.listdir('C:/Users/lucas/Downloads/')
    nomes_arquivos = [] 
    for arquivo in lista_de_arquivos_diretorio:
        if len(nomes_arquivos) == 12:
            break
        if arquivo.startswith("Servidor_"):
            nomes_arquivos.append(arquivo)
    return nomes_arquivos

def criarPastaDoServidor():

    nomes_arquivos = nomesArquivosContracheque()
    a = pd.read_excel('C:/Users/lucas/Downloads/'+nomes_arquivos[0])
    nome_servidor = a.iloc[3, 0]  # Obtém o valor do Nome e Matrícula

    nome_servidor = nome_servidor.strip()
    nome_servidor = nome_servidor.replace('/','_')
    nome_servidor = nome_servidor.rsplit("-")
    nome_servidor = nome_servidor[0]

    os.mkdir('C:/Users/lucas/Downloads/'+nome_servidor)
    for i in range(len(nomes_arquivos)):
        os.rename('C:/Users/lucas/Downloads/'+nomes_arquivos[i], 'C:/Users/lucas/Downloads/'+nome_servidor+'/'+str(i)+'.xls')


def pegaNomeMilitares():
    nome_militares = ['LINO DE SOUZA','SIDNEI REGINO CORDEIRO','CÁTILA DA SILVA NASCIMENTO BARBOSA','WEBER SOARES DOS SANTOS','JAMMES GOMES RODRIGUES','FRANCISCO NETO DE SOUSA VARGAS','SIDNEY GOMES DO NASCIMENTO','DEIVID MORAES ALVES','ANTÔNIO ARRAIAS DOS SANTOS','ALEX DE JESUS BRITO','WEDER SOARES RAMOS','CLEANDRO CACIANO QUIXABEIRA','JEOVÁ AQUINO BOTELHO','JUVENAL SOARES DE SOUSA','ANICESSO CARVALHO ROSA','CLAYDSON GALVÃO SILVA','IVANILDO DIVINO DA SILVA','FLÁVIO DE ANDRADE FERREIRA','ISMAEL NASCIMENTO DA CONCEIÇÃO','RENNAN SOUSA VIEIRA','FELIPE ALVES GAMA','FELIPE AUGUSTO LOVATO DA ROCHA','TIARLES SANTOS SOUZA','NEILSON LOPES DE OLIVEIRA','RONYERE BATISTA LIRA','JEREMIAS MEDRADO REIS JUNIOR','ELBES DE SOUZA OLIVEIRA SANTANA','JEFERSON SAMPAIO XAVIER RIBEIRO','RODRIGO ALMEIDA DE OLIVEIRA','THALLYSON CARDOSO BARAÚNA','JURANDI OLIVEIRA DE ALMEIDA JÚNIOR','MANOEL DO ESPIRITO SANTO ALVES OLIVEIRA','JOÃO CARLOS LIMA DE ARAÚJO','PAULO ERNANES RIBEIRO DINIZ','BRENO PINTO RAMALHO','DENIS FERREIRA DE MELO','PEDRO HENRIQUE CARVALHO ALVES','JÉSSICA BARROS AGUIAR SILVA','VITOR DANTAS DE MACEDO','NILSON PEREIRA DOS SANTOS','GILSON PEREIRA DOS SANTOS','PAULO ANDRÉ RIBEIRO COSTA','JOSÉ ROBERTO MACHADO','SÉRGIO CASTRO MARINHO','VALDIVINO ARCANJO DE OLIVEIRA JÚNIOR','DIEGO JARDIM DA COSTA','MARCOS RIBEIRO DA SILVA','CARLOS RAMON MENDES DE SOUSA','ALMINO BORGES BEZERRA','JÚLIO DUARTE DA SILVA','UANDER DE SOUZA AMARAL','CLÁUDIO LACERDA MARQUES','LILIA REIS AIRES DIAS CAVALCANTE','MARIA ADRIANA DA COSTA DOS SANTOS','ANTONIO DANILO DA SILVA','MATHEUS NOBRE MORAES','LUCAS JONATHAN MESQUITA DA SILVA','ALISSON DOS SANTOS SILVA','CHRISTOPHER ROCHA GOMES','PABLO NAZARENO AZEVEDO','ADDSON ACÁCIO PIMENTEL','DORIVAL RIBEIRO SALGADO','DIVINO GOMES SANTANA DA SILVA','SILVIO CESAR JOSE DE SOUZA','APARECIDO RAIMUNDO DA SILVA','KAROLINY SILVA BATISTA MARQUES','DIRCEU AZEVEDO BOGÉA','EDIMAR PEREIRA DE CARVALHO','GENIVAL PEREIRA DE FRANÇA','RAFAEL COSTA SILVA','MICHALANY TURIBIO GLÓRIA','ALTAMIRO MARIA DE ALMEIDA','MARCOS ALVES DIONISIO','GISLÉRIA MARTINS DA SILVA','OSÉAS DE PAULA AMORIM CRUZ','JARBAS INÁCIO FERNANDES','WESLYYANE RODRIGUES DA SILVA','MILTON BATISTA BORGES','EDSON SOUZA BASTOS','GABRIEL PINHEIRO RODRIGUES','MAURICIO HEIDSON DOS SANTOS BORGES','JOSIVAN ALVES BARROS','GUILHERME MACEDO LINHARES','VALDEIR GONÇALVES DE CARVALHO','JOSÉ WISLEY PEREIR ADE FIGUEIREDO','MANOEL PADILHAS DE CASTRO','EDUARDO SOUSA SILVA','WALBER BATISTA LOPES JÚNIOR','ACSA NASCIMENTO ALVES','MILLA ROCHA RODRIGUES','TIRSIA COELHO VIEIRA','JÉSSICA MAÍRA ROCHA DOS SANTOS','DANUSAFIGUEIREDODESOUSADIAS','PEDRODEALCÂNTARABONILHA','EDISLEYFERREIRASILVA','GUILHERMEMARTINSCOSTA','SAULOARTHURSILVADESOUZA','CLEIDSON AUGUSTO DA SILVA SANTOS','THIAGO LOPES TRINDADE','THEYLISON FERNANDO PINHEIRO FEITOSA','ALEX DE ASSIS SAO LEÃO','RAFAEL CONCEIÇÃO DE SOUSA','CARLOS BRUNO DA CÂMARA SANTOS','ADEMIR ALVES PEREIRA','RONALDO JUNOT PEREIRA DA SILVA','WERLLEY SOARES DA SILVA','NOBERTO BEZERRA DA SILVA JÚNIOR','DAVI CIRQUEIRA CARVALHO','HÉWERTON IDEMAR DE OLIVEIRA ACOSTA','FELIPE CHAVES SANTOS','EDDIE LAWSON RIBEIRO MARTINS','MARCOS MURILO PIRES DE OLIVEIRA','LUCAS MOTA REIS','JOÃO HENRIQUE MARQUES GUARINO','GENIVALDO FERREIRA GUIMARÃES','JOSÉ ANTÔNIO DIAS FONSECA','VILMAR PEREIRA DA SILVA','PEDRO SOARES DA SILVA','JOSÉ DIÔNITO BRAGA','RODRIGO CARVALHO TELES','WELINGTON MENDES DA SILVA','ANDRÉ LUIZ RODRIGUES SANTOS','MARCELO SOARES CARVALHO','FELIPE MENDES SIQUEIRA','WÉVERTHONN JHORDAN CÔRTES FERREIRA','MATEUS CAIXETA BRITO MARIANI']
    nome_militares_sem_acento = [unidecode(palavra) for palavra in nome_militares]
    nome_militares_sem_acento.sort()
    return nome_militares_sem_acento

def pegaMatriculaMilitares():
    matricula_militares = ['1079867','11783770','11782374','11787961','11556641','11780460','11776625','11784024','11776480']
    return matricula_militares

def baixouOuNaoArquivoContracheque(arquivos_anteriores):
    tempo_maximo_espera = 5
    tempo_esperado = 0
    while True:
        arquivos_atuais = set(os.listdir('C:/Users/lucas/Downloads/'))
        novos_arquivos = arquivos_atuais - arquivos_anteriores
        if novos_arquivos:
            return True
        if tempo_esperado >= tempo_maximo_espera:
            return False
        time.sleep(1) 
        tempo_esperado += 1



def militarBaixadoOuNaoMatricula(matricula_militar):
    lista_de_arquivos_diretorio = os.listdir('C:/Users/lucas/Downloads/')   
    for arquivo in lista_de_arquivos_diretorio:
        if arquivo.endswith(matricula_militar):
            return True
    return False



# def militarBaixadoOuNao(nome_militar):
#     lista_de_arquivos_diretorio = os.listdir('C:/Users/lucas/Downloads/')   
#     for arquivo in lista_de_arquivos_diretorio:
#         if arquivo.startswith(nome_militar):
#             return True
#     return False