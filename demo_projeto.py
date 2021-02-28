from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Gerenciador de Treinamento")

#criar funcao submit pra DB
def submit():
    #criar database
    conn = sqlite3.connect("dados_treinamento.db")
    #criar cursor da database
    c = conn.cursor()
    #inserir na tabela
    c.execute("INSERT INTO cadastros VALUES (:f_name, :l_name) "
        {
            "f_name": f_name.get(),
            "l_name": l_name.get()
        }
    
    )

#criar funcao query
def query():
    return



#criar botao de query
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=3, column=1, padx=145, pady=20, fg="white", bg="blue", bd=5)


#criando funções dos botôes


#subfuncao de cadastro de pessoas
def bt_apply_cad_pess():   
        nome=entry_nome.get()
        sobrenome=entry_sobrenome.get()
        entry_nome.delete(0, END)
        entry_sobrenome.delete(0, END)
        entry_nome.insert(0, "Nome")
        entry_sobrenome.insert(0, "Sobrenome")
        messagebox.showinfo("Status de Cadastro" , "Cadastrado: " + nome + " " + sobrenome)


#funcao de cadastro de pessoas
def bt_cad_pess():
    #criando sub-janela (sj)
    sj_cad_pess = Toplevel()
    sj_cad_pess.title("Cadastro de Participante")
    sj_cad_pess.geometry("500x200")
    global lbl_cad_pess, entry_nome, entry_sobrenome
    lbl_cad_pess = Label(sj_cad_pess, text="Insira os dados do Participante:")
    lbl_cad_pess.pack()
    entry_nome = Entry(sj_cad_pess, width=20, borderwidth=5)
    entry_nome.pack()
    entry_nome.insert(0, "Nome")
    entry_sobrenome = Entry(sj_cad_pess, width=20, borderwidth=5)
    entry_sobrenome.pack()
    entry_sobrenome.insert(0, "Sobrenome")
    apply_cad_pess = Button(sj_cad_pess, text="Cadastrar Participante", command=bt_apply_cad_pess, bd=5)
    apply_cad_pess.pack()
    


#criando menu principal

#criando botoes
cadastra_pessoa = Button(root, text="Cadastrar Participante", command=submit, padx=96, pady=20, fg="white", bg="blue", bd=5)
cadastra_sala = Button(root, text="Cadastrar Sala", padx=145, pady=20, fg="white", bg="blue", bd=5)
cadastra_cafe = Button(root, text="Cadastrar Espaço", padx=125, pady=20, fg="white", bg="blue", bd=5)
consulta_pessoa = Button(root, text="Consultar Participante", padx=96, pady=20, fg="white", bg="blue", bd=5)
consulta_sala = Button(root, text="Consultar Sala", padx=145, pady=20, fg="white", bg="blue", bd=5)
consulta_cafe = Button(root, text="Consultar Espaço", padx=125, pady=20, fg="white", bg="blue", bd=5)


#colocando botoes
cadastra_pessoa.grid(row=2, column=0)
cadastra_sala.grid(row=0, column=0)
cadastra_cafe.grid(row=1, column=0)
consulta_pessoa.grid(row=2, column=1)
consulta_sala.grid(row=0, column=1)
consulta_cafe.grid(row=1, column=1)









root.mainloop()