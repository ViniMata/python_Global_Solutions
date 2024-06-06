import pandas as pd
import matplotlib.pyplot as plt

# Função para puxar o dado da tabela que o usuario inserir
def pegar_e_ler_dados():
    dados_org = input('Para acessarmos o sua tabela com informações. Digite aqui o caminho do seu arquivo em formato ".csv": ')
    arquivo_lido = pd.read_csv(dados_org)
    return arquivo_lido

# Função para o usuario dizer quantos dados quer comparar e adiciona-los em uma lista
def selecao_de_dados(df):
    lista_dados = []
    opcao_usu = int(input("Quer comparar quantos dados?" ))
    for i in range(1, opcao_usu + 1):
        x = input("Digite o nome do dado que deseja incluir: ")
        if x in df.columns:
            lista_dados.append(x)
        else:
            print(f"{x} não está presente nas colunas do DataFrame")
    return lista_dados

# Função para mostrar dados no gráfico
def mostrar_dados(df, lista_dados):
    for dado in lista_dados:
        plt.plot(df[dado], label = dado)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.title('Comparação de Dados')
    plt.legend()
    plt.show()
# Loop principal para execução do programa
while True:
    try:    
        df = pegar_e_ler_dados()
        lista_dados = selecao_de_dados()
        mostrar_dados(df, lista_dados)
    except Exception as e:
        print(f"Erro! Verifique se o caminho do arquivo está correto e tente novamente. Detalhes do erro: {e}")
    break
