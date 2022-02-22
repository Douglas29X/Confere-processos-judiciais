from script import Script
from verificador import Verificador
from jus import Jus

def inicia():
	script = Script()
	arquivo = script.get_arquivo()
	verificador = Verificador(arquivo)
	verificador.verifica_site_judicial()
	jus = Jus(script.get_nome_pesquisado())

if __name__ == "__main__":
	inicia()