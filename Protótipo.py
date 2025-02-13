import customtkinter as ctk
from tkinter import messagebox
import sqlite3

# Listas para guardar nome dos clientes e os agendamentos

clientes = []
agendamentos = []

# Função para adicionar clientes ao sistema da barbearia
def adicionar_cliente():
    
    # uso do get() para obter o valor de uma chave, se não houver, retorna "none"
    # o get() retona o valor de um item de uma chave especificada
    nome = msg_nome.get()
    sobrenome = msg_sobrenome.get()
    telefone = msg_telefone.get()
    email = msg_email.get()
    
    if nome and sobrenome and telefone and email:
        cliente = {
            "nome": nome,
            "sobrenome": sobrenome,
            "telefone": telefone,
            "e-mail": email
        }
        clientes.append(cliente)
        
        # mensagem que aparece após o registro do cliente
        messagebox.showinfo("Sucesso", f"{nome} {sobrenome} adicionado com sucesso! Seja bem-vindo!")
    else:
        
        # mensagem que aparece caso o cliente não preencha todos os campos
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")
        
bancoDados = sqlite3.connect('barbearia.db')

# recebe o objeto onde criei o banco e usar o método cursor, que é o cursor que conseguimos usar os comandos do sql
cursor = bancoDados.cursor()

cursor.execute ("""CREATE TABLE IF NOT EXISTS Usuarios
(
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE,
    data_cadastro DATE DEFAULT (DATE('now'))
);
""")

# Função para listar os clientes registrados no programa

def listar_clientes():
    if not clientes:
        
        # mensagem que aparece caso não haja clientes registrados no programa
        messagebox.showinfo("Clientes", "Nenhum cliente registrado ainda.")
    else:
        
        # mensagem informada quando já há clientes registrados, informando o nome, sobrenome, telefone e e-mail
        lista_clientes = "\n".join([f"{cliente['nome']} {cliente['sobrenome']} - {cliente['telefone']} - {cliente['e-mail']}" for cliente in clientes])
        messagebox.showinfo("Lista de Clientes", lista_clientes)

# Função para buscar clientes

def buscar_cliente():
    
    # uso do get() para buscar um cliente específico
    nome_busca = msg_busca.get()
    encontrados = [cliente for cliente in clientes if nome_busca.lower() in cliente['nome'].lower()]
    
    if encontrados:
        
        # caso haja um cliente com o nome procurado será mostrado uma lista com os clientes com o nome informado
        lista_clientes = "\n".join([f"{cliente['nome']} {cliente['sobrenome']} - {cliente['telefone']} - {cliente['e-mail']}" for cliente in encontrados])
        messagebox.showinfo("Clientes Encontrados", lista_clientes)
    elif not encontrados:
        
        # se não houver nenhum cliente com o nome informado, essa mensagem será impressa na tela
        messagebox.showwarning("Clientes Encontrados", "Nenhum cliente encontrado.")

# Função para agendar horário (a resolver os bugs)

def agendar_horario():
    nome = msg_agenda_nome.get()
    data = msg_agenda_data.get()
    horario = msg_agenda_horario.get()
    serviço = msg_agenda_servico.get()
    
    if nome and data and horario and serviço:
        agendamento = {
            "nome": nome,
            "data": data,
            "horario": horario,
            "serviço": serviço
        }
        
        # adição de clientes a lista de agendamento
        agendamentos.append(agendamento)
        
        # mensagem que aparece após o agendamento do cliente
        messagebox.showinfo("Sucesso", f"Agendamento para {nome} no dia {data} às {horario} foi registrado com sucesso! O cliente desejará realizar {serviço}")
    else:
        
        # mensagem que aparece caso o cliente não preencha todos os campos
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")

# Função para listar agendamentos (messagebox é mais fácil para exibir as informações, além de mais harmônico para a interface)

def listar_agendamentos():
    if not agendamentos:
        
        # mensagem que é informada, caso não haja agendamentos no momento
        messagebox.showinfo("Agendamentos", "Nenhum agendamento registrado ainda.")
    else:
        
        # caso contrário, se tiver agendamentos, é informado o nome do cliente, a data e o horário em que ele vai realizar o serviço
        lista_agendamentos = "\n".join([f"{agendamento['nome']} - {agendamento['data']} às {agendamento['horario']}" for agendamento in agendamentos])
        messagebox.showinfo("Lista de Agendamentos", lista_agendamentos)

# Configuração da interface gráfica (Será desenvolvido)

ctk.set_appearance_mode("white")
ctk.set_default_color_theme("dark-blue")

interface = ctk.CTk()
interface.title("Gerenciador de Barbearia")
interface.geometry("700x1080")

frame = ctk.CTkFrame(interface)
frame.pack(pady=2, padx=10, fill="both", expand=True)

adicionar_titulo = ctk.CTkLabel(frame, text="Gerenciador de Barbearia", font=("Calisto MT", 24))
adicionar_titulo.pack(pady=12, padx=10)

# Configurações para adicionar cliente no sistema

adicionar_nome = ctk.CTkLabel(frame, text="Nome")
adicionar_nome.pack()
msg_nome = ctk.CTkEntry(frame)
msg_nome.pack(pady=2)

adicionar_sobrenome = ctk.CTkLabel(frame, text="Sobrenome")
adicionar_sobrenome.pack()
msg_sobrenome = ctk.CTkEntry(frame)
msg_sobrenome.pack(pady=2)

adicionar_telefone = ctk.CTkLabel(frame, text="Telefone")
adicionar_telefone.pack()
msg_telefone = ctk.CTkEntry(frame)
msg_telefone.pack(pady=2)

adicionar_email = ctk.CTkLabel(frame, text="E-mail")
adicionar_email.pack()
msg_email = ctk.CTkEntry(frame)
msg_email.pack(pady=2)

botão_adicionar = ctk.CTkButton(frame, text="Adicionar Cliente", command=adicionar_cliente)
botão_adicionar.pack(pady=2)

# Buscar clientes cadastrados

label_busca = ctk.CTkLabel(frame, text="Buscar Cliente por Nome")
label_busca.pack()
msg_busca = ctk.CTkEntry(frame)
msg_busca.pack(pady=2)

botão_buscar = ctk.CTkButton(frame, text="Buscar Cliente", command=buscar_cliente)
botão_buscar.pack(pady=2)

# Agendamento de horários

label_agenda_nome = ctk.CTkLabel(frame, text="Nome do Cliente")
label_agenda_nome.pack()
msg_agenda_nome = ctk.CTkEntry(frame)
msg_agenda_nome.pack(pady=2)

label_agenda_data = ctk.CTkLabel(frame, text="Data")
label_agenda_data.pack()
msg_agenda_data = ctk.CTkEntry(frame)
msg_agenda_data.pack(pady=2)

label_agenda_horario = ctk.CTkLabel(frame, text="Horário")
label_agenda_horario.pack()
msg_agenda_horario = ctk.CTkEntry(frame)
msg_agenda_horario.pack(pady=2)

label_serviço = ctk.CTkLabel(frame, text="Serviço")
label_serviço.pack()
msg_agenda_servico = ctk.CTkEntry(frame)
msg_agenda_servico.pack(pady=2)

botão_agendar = ctk.CTkButton(frame, text="Agendar Horário", command=agendar_horario)
botão_agendar.pack(pady=2)

# Listar clientes de agendamentos no programa

botão_listar_clientes = ctk.CTkButton(frame, text="Listar Clientes", command=listar_clientes)
botão_listar_clientes.pack(pady=2)

botão_listar_agendamentos = ctk.CTkButton(frame, text="Listar Agendamentos", command=listar_agendamentos)
botão_listar_agendamentos.pack(pady=2)

interface.mainloop()