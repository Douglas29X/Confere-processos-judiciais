class Verificador:
	def __init__(self, arquivo):
		links = []
		with open(arquivo, mode="r") as arquivo:
			conteudo = arquivo.readlines()
			for linha in conteudo:
				linha = linha.replace('\n','')
				local = linha.find(';')
				link_tratado = linha[local + 1:]
				if local != -1:
					links.append(link_tratado)
		self.__links = links
		self.__links_processos = []
		self.__numero_de_processos = 0

	def verifica_sites_aceitos(self, sites):
		for site in sites:
			for link in self.__links:
				if site in link:
					self.__links_processos.append(link)
					self.__numero_de_processos+=1

	def verifica_site_judicial(self):
		self.verifica_sites_aceitos(["jusbrasil", "projudi", "justica"])

		if self.__numero_de_processos != 0:
			if self.__numero_de_processos > 1:
				print(f"Foram encontrados {self.__numero_de_processos} processos nesse nome.")
				print("Os links para acessá-los são:")
			else:
				print(f"Fora encontrado apenas {self.__numero_de_processos} processo nesse nome.")
				print("O link para acessá-lo é:")
			with open("links.csv", mode="w") as arquivo:
				for processo in self.__links_processos:
					print(processo)
					arquivo.write(f'{processo}\n')
		else:
			print("Nenhum processo encontrado.")