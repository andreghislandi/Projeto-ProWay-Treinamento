# Projeto ProWay: Programa GoDEV_

Este projeto foi feito no intuito de participar do programa GoDEV_

A seguir estão as instruções de instalação do ambiente para
reproduzir o programa.
As instruções de operação estão mais adiante.

##Instalar Ambiente
*Para a construção deste programa foi usada a linguagem Python,
mais especificamente na versão 3.9.0
*[Python](https://www.python.org/)
*Para compilar e executar o programa foi utilizada a IDE VSCode
*[VSCode](https://code.visualstudio.com/download)
*Além disso, o manager de virtual environments pyenv foi utilizado.
*As bibliotecas (instaladas usando o pip) estão listadas no requirements.txt,
o qual sugere-se utilizar para instalação das dependências.

*Caso o usuário prefira usar sua IDE e manager de virtual environment preferidos, pode assim fazê-lo.
*Caso queira usar os recomendados, a seguir estão algumas instruções e links de vídeos para auxiliar

#Instalação

*Instalar a IDE VSCode (link acima)
*Dentro da IDE, na aba Extensões a esquerda, buscar Python e instalar
*Instalar o pyenv
*Usar o terminal para setar o git e clonar o repositório
*Abrir o repositório no VSCode
*Selecionar (ou criar) qualquer arquivo .py
*Criar um virtual environment para este repositório e instalar o python 3.9.0 neste environment
*Selecionar um terminal python caso ainda não o tenha feito: Ctrl + Shift + P abre os comandos -> Python: Select Interpreter para escolher a versão com o environment
*Com o VSCode aberto no repositório, verifique no canto inferior esquerdo a versão e o environment
*Execute o comando: pip install -r requirements.txt    para instalar as dependencias no environment
*Seguem vídeos que podem ajudar: [Video1](https://www.youtube.com/watch?v=f9sD1DpnhuI) , [Vídeo2](https://www.youtube.com/watch?v=fv8YxO3AJqg)


##Instruções de Uso

*Após selecionar o Python Terminal, o botão Run deve estar no canto superior direito do editor de texto
*Selecione o arquivo "criar_db.py" e o execute. Ele é responsavel por criar a DB e as tabelas usadas no programa
*Depois de criada a DB, selecione "main.py" e execute. Surgirá o menu principal.

#Suposições

*Antes de prosseguir saiba que foi considerado que assim como para os espaços de intervalo, também serão somente e exatamente duas salas
*Também foi considerado que o operador sabe que não deve inserir um número de participantes maior que o dobro da sala de menor capacidade
*Prossiga na seguinte ordem:
1. Clique no botão Cadastrar Sala e cadastre as duas salas
2. Clique no botão Cadastrar Espaço e cadastre os espaços do intervalo
3. Clique no botão Cadastrar Participante e cadastre todos os participantes
4. Clique no botão Sortear Salas. Cada participante recebe as salas de cada etapa e o espaço do intervalo
5. Use os botões de consulta para verificar pessoas, salas ou espaços nas janelas que abrem.
