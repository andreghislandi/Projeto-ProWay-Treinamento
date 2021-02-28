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
    #fazer a query -> colocar informacao das salas e espaços na tabela pessoas e SORTEAR
    c.execute("SELECT oid FROM pessoas")
    id_pessoas = c.fetchall()
    metade_muda = int(len(id_pessoas)/2)
    for id in id_pessoas:
        if id[0]==1 or id[0]%2==1 and id[0]<=metade_muda:
            #primeira metade NAO muda de sala // id IMPAR começa na sala 1
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
        elif id[0]%2==0 and id[0]<=metade_muda:
            #primeira metade NAO muda de sala // id PAR começa na sala 2
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
        elif id[0]%2==1 and id[0]>metade_muda:
            #segunda metade muda de sala // id IMPAR começa na sala 1
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
        elif id[0]%2==0 and id[0]>metade_muda:
            #segunda metade muda de sala // id PAR começa na sala 2
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
        
    for id in id_pessoas:  
        if id[0]<=metade_muda:
            #espaço cafe 1
            intervalo = c.execute("SELECT nome_cafe FROM esp_cafe WHERE oid=1")
            intervalo_ = c.fetchall()[0]  
            c.execute("""UPDATE pessoas SET 
                intervalo_cafe = :sala_1
                
                WHERE oid = :oid""",
                {
                    'sala_1': intervalo_[0],
                    'oid': id[0]
                })      
        elif id[0]>metade_muda:
            #espaço cafe 2
            intervalo = c.execute("SELECT nome_cafe FROM esp_cafe WHERE oid=2")
            intervalo_ = c.fetchall()[0]
            c.execute("""UPDATE pessoas SET 
                intervalo_cafe = :sala_1
                
                WHERE oid = :oid""",
                {
                    'sala_1': intervalo_[0],
                    'oid': id[0]
                })    
             
    ####fazer a query -> colocar informacao das salas na tabela pessoas#####
    #buscar nome das salas na db e colocar em variaveis internas da funcao, tirando da tupla#
    c.execute("SELECT sala FROM salas")
    salass=c.fetchall()
    salinha1=salass[0]
    salinha_1=str(salinha1[0])
    c.execute("SELECT sala FROM salas")
    salass=c.fetchall()
    salinha2=salass[1]
    salinha_2=str(salinha2[0])
    c.execute("SELECT sala FROM salas")
    salass=c.fetchall()
    salinha3=salass[2]
    salinha_3=str(salinha3[0])
    c.execute("SELECT sala FROM salas")
    salass=c.fetchall()
    salinha4=salass[3]
    salinha_4=str(salinha4[0])
    c.execute("SELECT nome_cafe FROM esp_cafe")
    cafess=c.fetchall()
    cafezin1=cafess[0]
    cafezin_1=str(cafezin1[0])
    c.execute("SELECT nome_cafe FROM esp_cafe")
    cafess=c.fetchall()
    cafezin2=cafess[1]
    cafezin_2=str(cafezin2[0])
    
    #pegar nome e sobrenome para cada sala e espaço
    d = { "sala": salinha_1 }
    c.execute("SELECT nome, sobrenome FROM pessoas WHERE sala_etapa_1=:sala", d)
    galera_sala1_et1 = c.fetchall()
    
    e = { "sala": salinha_2 }
    c.execute("SELECT nome, sobrenome FROM pessoas WHERE sala_etapa_2 = :sala", e)
    galera_sala1_et2 = c.fetchall()
    
    f = { "sala": salinha_3 }
    c.execute("SELECT nome, sobrenome FROM pessoas WHERE sala_etapa_1 = :sala", f)
    galera_sala2_et1 = c.fetchall()
    
    g = { "sala": salinha_4 }
    c.execute("SELECT nome, sobrenome FROM pessoas WHERE sala_etapa_2 = :sala", g)
    galera_sala2_et2 = c.fetchall()

    h = { "cafe": cafezin_1 }
    c.execute("SELECT nome, sobrenome FROM pessoas WHERE intervalo_cafe = :cafe", h)
    galera_esp1 = c.fetchall()

    i = { "cafe": cafezin_2 }
    c.execute("SELECT nome, sobrenome FROM pessoas WHERE intervalo_cafe = :cafe", i)
    galera_esp2 = c.fetchall()

    #update nas tabela salas e espaços
    joined = [','.join(row) for row in galera_sala1_et1]
    sala_1_et_1_pess = '\n'.join(joined)
    joined = [','.join(row) for row in galera_sala1_et2]
    sala_1_et_2_pess = '\n'.join(joined)
    joined = [','.join(row) for row in galera_sala2_et1]
    sala_2_et_1_pess = '\n'.join(joined)
    joined = [','.join(row) for row in galera_sala2_et2]
    sala_2_et_2_pess = '\n'.join(joined)
    joined = [','.join(row) for row in galera_esp1]
    esp_1_pess = '\n'.join(joined)
    joined = [','.join(row) for row in galera_esp2]
    esp_2_pess = '\n'.join(joined)
            #salas
    c.execute("""UPDATE salas SET 
                participantes = :part
                
                WHERE oid = :oid""",
                {
                    'part': sala_1_et_1_pess,
                    'oid': 1
                })   
    c.execute("""UPDATE salas SET 
                participantes = :part
                
                WHERE oid = :oid""",
                {
                    'part': sala_1_et_2_pess,
                    'oid': 2
                })   
    c.execute("""UPDATE salas SET 
                participantes = :part
                
                WHERE oid = :oid""",
                {
                    'part': sala_2_et_1_pess,
                    'oid': 3
                }) 
    c.execute("""UPDATE salas SET 
                participantes = :part
                
                WHERE oid = :oid""",
                {
                    'part': sala_2_et_2_pess,
                    'oid': 4
                })  
            #espaços 
    c.execute("""UPDATE esp_cafe SET 
                participantes = :part
                
                WHERE oid = :oid""",
                {
                    'part': esp_1_pess,
                    'oid': 1
                })      
    c.execute("""UPDATE esp_cafe SET 
                participantes = :part
                
                WHERE oid = :oid""",
                {
                    'part': esp_2_pess,
                    'oid': 2
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
    sj_cad_sala.geometry("540x200")
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


#subfuncao de CADASTRO de ESPAÇOS
def bt_apply_cad_esp():   
        #criar database
        conn = sqlite3.connect("dados_treinamento.db")
        #criar cursor da database
        c = conn.cursor()

        nome_esp = entry_esp.get()
        cap_esp = entry_cap_esp.get()
        esp_inserir= (nome_esp, cap_esp)
        prin=Label(sj_cad_esp, text=esp_inserir)
        prin.pack()


        #inserir na tabela
        c.execute("INSERT INTO esp_cafe (nome_cafe, capacidade) VALUES (?,?)", esp_inserir)
        #commit na db
        conn.commit()
        

        #popadinha e clear
        entry_esp.delete(0, END)
        entry_cap_esp.delete(0, END)
        entry_esp.insert(0, "Nome do Espaço")
        entry_cap_esp.insert(0, "Capacidade")
        messagebox.showinfo("Status de Cadastro" , "Espaço cadastrado!")

        #fechar conexao
        conn.close()


#funcao de CADASTRO de ESPAÇOS
def bt_cad_esp():
    #criando sub-janela (sj)
    global sj_cad_esp
    sj_cad_esp = Toplevel()
    sj_cad_esp.title("Cadastro de Espaços do Intervalo")
    sj_cad_esp.geometry("600x200")
    global lbl_cad_esp, entry_esp, entry_cap_esp
    lbl_cad_esp = Label(sj_cad_esp, text="Insira os dados do Espaço:")
    lbl_cad_esp.pack()
    entry_esp = Entry(sj_cad_esp, width=25, borderwidth=5)
    entry_esp.pack()
    entry_esp.insert(0, "Nome do Espaço")
    entry_cap_esp = Entry(sj_cad_esp, width=25, borderwidth=5)
    entry_cap_esp.pack()
    entry_cap_esp.insert(0, "Capacidade")
    apply_cad_esp = Button(sj_cad_esp, text="Cadastrar Espaço", command=bt_apply_cad_esp, bd=5)
    apply_cad_esp.pack()


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
    consulta_etapa_1 = c.fetchall()[0]
    consulta_etapa_1_ = consulta_etapa_1[2]
    #fazer a query da sala na etapa 2
    c.execute("SELECT * FROM salas WHERE sala = :sala", e)
    consulta_etapa_2 = c.fetchall()[0]
    consulta_etapa_2_ = consulta_etapa_2[2]

    # meta = c.execute("PRAGMA table_info('pessoas')")
    # for r in meta:
    #     print(r)
    lbla=Label(sj_con_sala, text="Etapa 1:")
    lbla.pack()
    lbl_con_sala_done_et_1 = Label(sj_con_sala, text=consulta_etapa_1_)
    lbl_con_sala_done_et_1.pack()
    lblb=Label(sj_con_sala, text="Etapa 2:")
    lblb.pack()
    lbl_con_sala_done_et_2 = Label(sj_con_sala, text=consulta_etapa_2_)
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
    sj_con_sala.geometry("500x1200")
    global lbl_con_sala, entry_sala_con
    lbl_con_sala = Label(sj_con_sala, text="Insira nome da Sala:")
    lbl_con_sala.pack()
    entry_sala_con = Entry(sj_con_sala, width=20, borderwidth=5)
    entry_sala_con.pack()
    entry_sala_con.insert(0, "Nome da Sala")
    
    apply_con_sala = Button(sj_con_sala, text="Consultar Sala", command=bt_apply_con_sala, bd=5)
    apply_con_sala.pack()

#subfuncao de CONSULTA de ESPAÇOS
def bt_apply_con_esp():   

    #get no nome e sobrenome
    esp_consultar=entry_esp_con.get()
    
    d = { "cafe": esp_consultar }
    #criar database
    conn = sqlite3.connect("dados_treinamento.db")
    #criar cursor da database
    c = conn.cursor()
    #fazer a query do espaço
    c.execute("SELECT * FROM esp_cafe WHERE nome_cafe = :cafe", d)
    consulta_esp_cafe = c.fetchall()[0]
    consulta_esp_cafe_ = consulta_esp_cafe[2]

    # meta = c.execute("PRAGMA table_info('pessoas')")
    # for r in meta:
    #     print(r)
    print(consulta_esp_cafe)
    lbla=Label(sj_con_esp, text="Participantes:")
    lbla.pack()
    lbl_con_esp_done_et_1 = Label(sj_con_esp, text=consulta_esp_cafe_)
    lbl_con_esp_done_et_1.pack()

    #commit na db
    conn.commit()
    #fechar conexao
    conn.close()



#funcao de CONSULTA de ESPAÇOS
def bt_con_esp():
    #criando sub-janela (sj)
    global sj_con_esp
    sj_con_esp = Toplevel()
    sj_con_esp.title("Consultar Espaço")
    sj_con_esp.geometry("500x1200")
    global lbl_con_esp, entry_esp_con
    lbl_con_esp = Label(sj_con_esp, text="Insira nome do Espaço:")
    lbl_con_esp.pack()
    entry_esp_con = Entry(sj_con_esp, width=20, borderwidth=5)
    entry_esp_con.pack()
    entry_esp_con.insert(0, "Nome do Espaço")
    apply_con_esp = Button(sj_con_esp, text="Consultar Espaço", command=bt_apply_con_esp, bd=5)
    apply_con_esp.pack()




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
    c.execute("SELECT * FROM pessoas WHERE nome = :nome AND sobrenome = :sobrenome", d)
    records = c.fetchall()
    participante = records[0]
    nome_completo = participante[0] + " " + participante[1]
    salas = participante[2] + " ," + participante[4]
    cafe = participante[3]
    lbl_con_pess_done1 = Label(sj_con_pess, text=nome_completo)
    lbl_con_pess_done1.pack()
    lbl_con_pess_done2 = Label(sj_con_pess, text="Salas:")
    lbl_con_pess_done2.pack()
    lbl_con_pess_done3 = Label(sj_con_pess, text=salas)
    lbl_con_pess_done3.pack()
    lbl_con_pess_done4 = Label(sj_con_pess, text="Intervalo:")
    lbl_con_pess_done4.pack()
    lbl_con_pess_done5 = Label(sj_con_pess, text=cafe)
    lbl_con_pess_done5.pack()
    

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
    sj_con_pess.geometry("600x900")
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
cadastra_cafe = Button(root, text="Cadastrar Espaço", command=bt_cad_esp, padx=125, pady=20, fg="white", bg="blue", bd=5)
consulta_pessoa = Button(root, text="Consultar Participante", command=bt_con_pess, padx=95, pady=20, fg="white", bg="blue", bd=5)
consulta_sala = Button(root, text="Consultar Sala", command=bt_con_sala, padx=145, pady=20, fg="white", bg="blue", bd=5)
consulta_cafe = Button(root, text="Consultar Espaço", command=bt_con_esp, padx=125, pady=20, fg="white", bg="blue", bd=5)
sortear_salas = Button(root, text="Sortear Salas", command=bt_sort_salas, padx=155, pady=20, fg="white", bg="blue", bd=5)


#colocando botoes
cadastra_pessoa.grid(row=2, column=0)
cadastra_sala.grid(row=0, column=0)
cadastra_cafe.grid(row=1, column=0)
consulta_pessoa.grid(row=2, column=1)
consulta_sala.grid(row=0, column=1)
consulta_cafe.grid(row=1, column=1)
sortear_salas.grid(row=3, column=0)








root.mainloop()