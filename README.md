# Confere-processos-judiciais
Um robô que pesquisa no Google algo de desejo do usuário e obtém informações sobre processos na justiça.

Nesse novo projeto eu adaptei o código do robô anterior (que faz pesquisas) para, dessa vez, ele também analisar quantos processos judiciais o nome pesquisado possui, isso utilizando-se do banco de dados da própria pesquisa do google. A nova parte requer, em sua maioria, lidar com os dados coletados e dispostos no relatório, usando palavras chaves e fatiamento de String.

Ademais, organizei o módulo "script" em um método mais robusto e o módulo "verificador" em uma classe mais estruturada, para que o desenvolvedor possa ter mais controle nas mudanças pontuais.

Atualização N°1: Agora ele também é capaz de entrar dentro do site do JusBrasil e analisar os dados da (ou das), página(s), registrando o resultado em um arquivo personalizado com o nome.
