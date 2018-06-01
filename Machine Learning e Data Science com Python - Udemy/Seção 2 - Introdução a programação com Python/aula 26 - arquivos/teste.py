"""
texto = '''Aprendendo python
machine learning
python é muito legal
'''

with open('arquivo.txt', 'w') as f:
	f.write(texto)
"""

with open('dataset.txt', 'r') as arq:
	lista = arq.read().splitlines()

print(len(lista))