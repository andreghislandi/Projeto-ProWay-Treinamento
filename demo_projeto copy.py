from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Gerenciador de Treinamento")

    

#criar funcao query
def query():
    #criar database
    conn = sqlite3.connect("dados_treinamento.db")
    #criar cursor da database
    c = conn.cursor()
    #fazer a query
    c.execute("SELECT *, oid FROM pessoas")
    records = c.fetchall()
    print(records)

    #commit na db
    conn.commit()
    #fechar conexao
    conn.close()


#funcao sorteio de salas
def bt_sort_salas():
    #criar database
    conn = sqlite3.connect("dados_treinamento.db")
    #criar cursor da database
    c = conn.cursor()
    #fazer a query
    c.execute("SELECT oid FROM pessoas")
    id_pessoas = c.fetchall()
    metade_muda = int(len(id_pessoas)/2)
    for id in id_pessoas:
        if id[0]%2==1 and id[0]<=metade_muda:
            #primeira metade muda de sala // id IMPAR começa na sala 1
            sala1 = c.execute("SELECT sala FROM salas WHERE oid=1")
            sala1_ = c.fetchall()[0]
            sala2 = c.execute("SELECT sala FROM salas WHERE oid=4")
            sala2_ = c.fetchall()[0]
            c.execute("""UPDATE pessoas SET 
                sala_etapa_1 = :sala_1,
                sala_etapa_2 = :sala_2
                
                WHERE oid = :oid""",
                {
                    'sala_1': sala1_[0],
                    'sala_2': sala2_[0],
                    'oid': id[0]
                })
        elif id[0]%2==0 and id[0]<=metade_muda:
            #primeira metade muda de sala // id PAR começa na sala 2
            sala1 = c.execute("SELECT sala FROM salas WHERE oid=3")
            sala1_ = c.fetchall()[0]
            sala2 = c.execute("SELECT sala FROM salas WHERE oid=2")
            sala2_ = c.fetchall()[0]
            c.execute("""UPDATE pessoas SET 
                sala_etapa_1 = :sala_1,
                sala_etapa_2 = :sala_2
                
                WHERE oid = :oid""",
                {
                    'sala_1': sala1_[0],
                    'sala_2': sala2_[0],
                    'oid': id[0]
                })            
        elif id[0]%2==1 and id[0]>metade_muda:
            #segunda metade NAO muda de sala // id IMPAR começa na sala 1
            sala1 = c.execute("SELECT sala FROM salas WHERE oid=1")
            sala1_ = c.fetchall()[0]
            sala2 = c.execute("SELECT sala FROM salas WHERE oid=2")
            sala2_ = c.fetchall()[0]
            c.execute("""UPDATE pessoas SET 
                sala_etapa_1 = :sala_1,
                sala_etapa_2 = :sala_2
                
                WHERE oid = :oid""",
                {
                    'sala_1': sala1_[0],
                    'sala_2': sala2_[0],
                    'oid': id[0]
                })       
        elif id[0]%2==0 and id[0]>metade_muda:
            #segunda metade NAO muda de sala // id PAR começa na sala 2
            sala1 = c.execute("SELECT sala FROM salas WHERE oid=3")
            sala1_ = c.fetchall()[0]
            sala2 = c.execute("SELECT sala FROM salas WHERE oid=4")
            sala2_ = c.fetchall()[0]
            c.execute("""UPDATE pessoas SET 
                sala_etapa_1 = :sala_1,
                sala_etapa_2 = :sala_2
                
                WHERE oid = :oid""",
                {
                    'sala_1': sala1_[0],
                    'sala_2': sala2_[0],
                    'oid': id[0]
                })           
             

    #commit na db
    conn.commit()
    #fechar conexao
    conn.close()







#criando funções dos botôes


#subfuncao de CADASTRO de SALAS
def bt_apply_cad_sala():   
        #criar database
        conn = sqlite3.connect("dados_treinamento.db")
        #criar cursor da database
        c = conn.cursor()

        nome_sala_etapa_1=str(entry_sala.get() + "_etapa_1")
        nome_sala_etapa_2=str(entry_sala.get() + "_etapa_2")
        cap_sala_etapa_1=entry_cap_sala.get()
        cap_sala_etapa_2=entry_cap_sala.get()
        salas_inserir= (nome_sala_etapa_1, cap_sala_etapa_1), (nome_sala_etapa_2, cap_sala_etapa_2)
        prin=Label(sj_cad_sala, text=salas_inserir)
        prin.pack()


        #inserir na tabela
        c.executemany("INSERT INTO salas (sala, capacidade) VALUES (?,?)", salas_inserir)
        #commit na db
        conn.commit()
        

        #popadinha e clear
        entry_sala.delete(0, END)
        entry_cap_sala.delete(0, END)
        entry_sala.insert(0, "Nome da Sala")
        entry_cap_sala.insert(0, "Capacidade")
        messagebox.showinfo("Status de Cadastro" , "Sala cadastrada!")

        #fechar conexao
        conn.close()


#funcao de CADASTRO de SALAS
def bt_cad_sala():
    #criando sub-janela (sj)
    global sj_cad_sala
    sj_cad_sala = Toplevel()
    sj_cad_sala.title("Cadastro de Salas")
    sj_cad_sala.geometry("500x200")
    global lbl_cad_sala, entry_sala, entry_cap_sala
    lbl_cad_sala = Label(sj_cad_sala, text="Insira os dados da Sala:")
    lbl_cad_sala.pack()
    entry_sala = Entry(sj_cad_sala, width=20, borderwidth=5)
    entry_sala.pack()
    entry_sala.insert(0, "Nome da Sala")
    entry_cap_sala = Entry(sj_cad_sala, width=20, borderwidth=5)
    entry_cap_sala.pack()
    entry_cap_sala.insert(0, "Capacidade")
    apply_cad_sala = Button(sj_cad_sala, text="Cadastrar Sala", command=bt_apply_cad_sala, bd=5)
    apply_cad_sala.pack()


#subfuncao de CADASTRO de PESSOAS
def bt_apply_cad_pess():   
        #criar database
        conn = sqlite3.connect("dados_treinamento.db")
        #criar cursor da database
        c = conn.cursor()

        nome=entry_nome.get()
        sobrenome=entry_sobrenome.get()

        #inserir na tabela
        c.execute("INSERT INTO pessoas (nome, sobrenome) VALUES (:nome, :sobrenome)",
        {
            'nome': entry_nome.get(),
            'sobrenome': entry_sobrenome.get()
        } )

        #commit na db
        conn.commit()
        #fechar conexao
        conn.close()

        #popadinha e clear
        entry_nome.delete(0, END)
        entry_sobrenome.delete(0, END)
        entry_nome.insert(0, "Nome")
        entry_sobrenome.insert(0, "Sobrenome")
        messagebox.showinfo("Status de Cadastro" , "Cadastrado: " + nome + " " + sobrenome)


#funcao de CADASTRO de PESSOAS
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
    

#subfuncao de CONSULTA de SALAS
def bt_apply_con_sala():   

    #get no nome e sobrenome
    sala_consultar=entry_sala_con.get()
    sala_consultar_1=sala_consultar+"_etapa_1"
    sala_consultar_2=sala_consultar+"_etapa_2"
    
    d = { "sala": sala_consultar_1 }
    e = { "sala": sala_consultar_2 }
    #criar database
    conn = sqlite3.connect("dados_treinamento.db")
    #criar cursor da database
    c = conn.cursor()
    #fazer a query da sala na etapa 1
    c.execute("SELECT * FROM salas WHERE sala = :sala", d)
    consulta_etapa_1 = c.fetchall()
    #fazer a query da sala na etapa 2
    c.execute("SELECT * FROM salas WHERE sala = :sala", e)
    consulta_etapa_2 = c.fetchall()
    
    # meta = c.execute("PRAGMA table_info('pessoas')")
    # for r in meta:
    #     print(r)


    lbl_con_sala_done_et_1 = Label(sj_con_sala, text= consulta_etapa_1)
    lbl_con_sala_done_et_1.pack()
    lbl_con_sala_done_et_2 = Label(sj_con_sala, text= consulta_etapa_2)
    lbl_con_sala_done_et_2.pack()

    #commit na db
    conn.commit()
    #fechar conexao
    conn.close()



#funcao de CONSULTA de SALAS
def bt_con_sala():
    #criando sub-janela (sj)
    global sj_con_sala
    sj_con_sala = Toplevel()
    sj_con_sala.title("Consultar Sala")
    sj_con_sala.geometry("500x250")
    global lbl_con_sala, entry_sala_con
    lbl_con_sala = Label(sj_con_sala, text="Insira nome da Sala:")
    lbl_con_sala.pack()
    entry_sala_con = Entry(sj_con_sala, width=20, borderwidth=5)
    entry_sala_con.pack()
    entry_sala_con.insert(0, "Nome da Sala")
    
    apply_con_sala = Button(sj_con_sala, text="Consultar Sala", command=bt_apply_con_sala, bd=5)
    apply_con_sala.pack()






#subfuncao de CONSULTA de PESSOAS
def bt_apply_con_pess():   

    #get no nome e sobrenome
    nome_consultar=entry_nome.get()
    sobrenome_consultar=entry_sobrenome.get()

    
    d = { "nome": nome_consultar , "sobrenome": sobrenome_consultar }
    #criar database
    conn = sqlite3.connect("dados_treinamento.db")
    #criar cursor da database
    c = conn.cursor()
    #fazer a query
    c.execute("SELECT *, oid FROM pessoas WHERE nome = :nome AND sobrenome = :sobrenome", d)
    records = c.fetchall()
    participante = records[0]
    lbl_con_pess_done = Label(sj_con_pess, text=participante)
    lbl_con_pess_done.pack()
    

    #commit na db
    conn.commit()
    #fechar conexao
    conn.close()



#funcao de CONSULTA de PESSOAS
def bt_con_pess():
    #criando sub-janela (sj)
    global sj_con_pess
    sj_con_pess = Toplevel()
    sj_con_pess.title("Consultar Participante")
    sj_con_pess.geometry("500x250")
    global lbl_con_pess, entry_nome, entry_sobrenome
    lbl_con_pess = Label(sj_con_pess, text="Insira nome e " + "\n" + " sobrenome do Participante:")
    lbl_con_pess.pack()
    entry_nome = Entry(sj_con_pess, width=20, borderwidth=5)
    entry_nome.pack()
    entry_nome.insert(0, "Nome")
    entry_sobrenome = Entry(sj_con_pess, width=20, borderwidth=5)
    entry_sobrenome.pack()
    entry_sobrenome.insert(0, "Sobrenome")
    apply_con_pess = Button(sj_con_pess, text="Consultar Participante", command=bt_apply_con_pess, bd=5)
    apply_con_pess.pack()




#criando menu principal

#criando botoes
cadastra_pessoa = Button(root, text="Cadastrar Participante", command=bt_cad_pess, padx=95, pady=20, fg="white", bg="blue", bd=5)
cadastra_sala = Button(root, text="Cadastrar Sala", command=bt_cad_sala, padx=145, pady=20, fg="white", bg="blue", bd=5)
cadastra_cafe = Button(root, text="Cadastrar Espaço", padx=125, pady=20, fg="white", bg="blue", bd=5)
consulta_pessoa = Button(root, text="Consultar Participante", command=bt_con_pess, padx=95, pady=20, fg="white", bg="blue", bd=5)
consulta_sala = Button(root, text="Consultar Sala", command=bt_con_sala, padx=145, pady=20, fg="white", bg="blue", bd=5)
consulta_cafe = Button(root, text="Consultar Espaço", padx=125, pady=20, fg="white", bg="blue", bd=5)
query_btn = Button(root, text="Mostrar Dados", command=query, padx=145, pady=20, fg="white", bg="blue", bd=5)
sortear_salas = Button(root, text="Sortear Salas", command=bt_sort_salas, padx=155, pady=20, fg="white", bg="blue", bd=5)


#colocando botoes
cadastra_pessoa.grid(row=2, column=0)
cadastra_sala.grid(row=0, column=0)
cadastra_cafe.grid(row=1, column=0)
consulta_pessoa.grid(row=2, column=1)
consulta_sala.grid(row=0, column=1)
consulta_cafe.grid(row=1, column=1)
query_btn.grid(row=3, column=1)
sortear_salas.grid(row=3, column=0)








root.mainloop()