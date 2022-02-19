from script import main
from verificador import Verificador


def inicia():
	arquivo = main()
	return arquivo

def finaliza(arquivo):
	verificador = Verificador(arquivo)
	verificador.verifica_site_judicial()

if __name__ == "__main__":
	arquivo = inicia()
	finaliza(arquivo)