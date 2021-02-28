from tkinter import *

root = Tk()

#criando entrada
entry_nome = Entry(root, width=20, borderwidth=5)
entry_nome.grid(row=0, column=1)
entry_sobrenome = Entry(root, width=20, borderwidth=5)
entry_sobrenome.grid(row=1, column=1)

#armazenando o dado de entrada: usa nomedavariaveldoinput.get()


#criando função do comando do botão
def butao1():
    
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    label3 = Label(root, text= nome + " " + sobrenome)
    label3.grid()

#creating label widget
myLabel1 = Label(root, text="Nome:")
myLabel2 = Label(root, text="Sobrenome:")
#jogando na tela
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0) 

#cria botão
butao = Button(root, text="Enviar", command=butao1, padx=125, pady=20, fg="white", bg="blue")
#joga botão
butao.grid(row=2, column=1, columnspan=3)


root.mainloop()