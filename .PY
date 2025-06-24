frase = """
Concluímos que chegamos à conclusão que não concluímos nada.
Por isso, conclui-se que a conclusão será concluída quando todas
tiverem concluído que já é tempo de concluir uma conclusão.
"""

import string

frase_limpa = frase.lower()
for pontuacao in string.punctuation + '“”‘’´`–':
    frase_limpa = frase_limpa.replace(pontuacao, '')


palavras = frase_limpa.split()


contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1


for palavra, ocorrencias in contagem.items():
    print(f"'{palavra}': {ocorrencias}")