from selenium import webdriver
import time

class Jus:
	def __init__(self, nome_pesquisado):
		self.__links = self.le_arquivo()
		self._nome_pesquisado = nome_pesquisado
		self.main()

	def le_arquivo(self):
		with open("links.csv", mode="r") as arquivo:
			return arquivo.readlines()

	def main(self):
		with open(f"processos_no_jusbrasil_de_{self._nome_pesquisado}.csv", mode='w') as arquivo:
			for link in self.__links:
				link = link.replace("\n", '')
				if "jusbrasil" in link:
					#é necessário abrir uma aba todas as vezes para não identificarem o bot
					driver = webdriver.Chrome()
					driver.get(link)
					numero_de_processos = driver.find_element_by_xpath("//div[@class='PersonDescription-summary']").text
					arquivo.write(f'{numero_de_processos}\n')
					print(numero_de_processos)
					time.sleep(10)
