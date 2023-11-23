import pandas as pd 


class CSVReader:

    def __init__(self):
        self.base_file = 'df_teses_dissertacoes_1987_2021.csv'
    # Agora, essa função por default roda com 'HISTORIA' como 
    # parametro que estou usando na linha 9 para filtrar, mas se vc quiser executar com qualquer outra materia
    # basta adicionar o texto direto como parametro na linha 18
    def filter_thesis(self, theme='HISTORIA'):
        # dataframe = pd.read_csv('df_teses_dissertacoes_1987_2021.csv', delimiter=";", nrows=50)
        dataframe = pd.read_csv(self.base_file, delimiter=";")
        dataframe_filtrado = dataframe[dataframe["nm_programa"] == theme]
        # isso daqui é um f-string
        # é uma maneira de escrever uma string colocando o conteudo de uma variavel dentro
        # nesse caso eu coloquei o parametro "theme" e pedi pro python por em minusculas
        #o que vc quer fazer em seguida?
        #Ah eu pensei a partir desse novo dataframe só com os dados de história, começar a trabalhar no df,
        #Tipo, ver os temas mais comuns, etc
        #Tipo, começar a análise mesmo, ou tentar dar mais uma limpada, mas eu queria conseguir acessar como data frame
        # hmmm, saquei. deixa eu pensar como fazer.
        dataframe_filtrado.to_csv(f'teses-de-{theme.lower()}.csv', index=False)

    def find_recurrences(self):
        dataframe = pd.read_csv('teses-de-historia.csv')
        
    
#Pˆ, muito massa
#Te respondi no zap
# bele, só um segundo
#De boa, aliás, como já está meio tarde, se você quiser podemos continuar um outro dia
# beleza, vamos fazer agora o versionamento do codigo
# da pra fazer no botao ali do lado esquerdo, mas vou fazer via linha de comando pra vc ver


instance = CSVReader()
instance.filter_thesis()




