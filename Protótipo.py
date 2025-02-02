import customtkinter as ctk
from tkinter import messagebox

# Listas para guardar nome dos clientes e os agendamentos
clientes = []
agendamentos = []

# Função para adicionar clientes ao sistema da barbearia
def adicionar_cliente():
    nome = add_nome.get()
    sobrenome = add_sobrenome.get()
    telefone = add_telefone.get()
    email = add_email.get()
    
    if nome and sobrenome and telefone and email:
        cliente = {
            "nome": nome,
            "sobrenome": sobrenome,
            "telefone": telefone,
            "e-mail": email
        }
        clientes.append(cliente)
        messagebox.showinfo("Sucesso", f"Cliente {nome} adicionado com sucesso! Seja bem-vindo!")
        add_nome.delete(0, 'end')
        add_sobrenome.delete(0, 'end')
        add_telefone.delete(0, 'end')
        add_email.delete(0, 'end')
    else:
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")

# Função para listar os clientes dentro do prog
def listar_clientes():
    if not clientes:
        messagebox.showinfo("Clientes", "Nenhum cliente registrado ainda.")
    else:
        lista_clientes = "\n".join([f"{cliente['nome']} {cliente['sobrenome']} - {cliente['telefone']} - {cliente['e-mail']}" for cliente in clientes])
        messagebox.showinfo("Lista de Clientes", lista_clientes)

# Função para buscar clientes
def buscar_cliente():
    nome_busca = add_busca.get()
    encontrados = [cliente for cliente in clientes if nome_busca.lower() in cliente['nome'].lower()]
    
    if encontrados:
        lista_clientes = "\n".join([f"{cliente['nome']} {cliente['sobrenome']} - {cliente['telefone']} - {cliente['e-mail']}" for cliente in encontrados])
        messagebox.showinfo("Clientes Encontrados", lista_clientes)
    else:
        messagebox.showinfo("Clientes Encontrados", "Nenhum cliente encontrado com esse nome.")

# Função para agendar horário (a resolver os bugs)
def agendar_horario():
    nome = add_agenda_nome.get()
    data = add_agenda_data.get()
    horario = add_agenda_horario.get()
    serviço = add_agenda_servico.get()
    
    if nome and data and horario and serviço:
        agendamento = {
            "nome": nome,
            "data": data,
            "horario": horario,
            "serviço": serviço
        }
        agendamentos.append(agendamento)
        messagebox.showinfo("Sucesso", f"Agendamento para {nome} no dia {data} às {horario} foi registrado com sucesso! O cliente desejará realizar {serviço}")
        add_agenda_nome.delete(0, 'end')
        add_agenda_data.delete(0, 'end')
        add_agenda_horario.delete(0, 'end')
        add_agenda_servico.delete(0, 'end')
    else:
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")

# Função para listar agendamentos (messagebox é mais fácil para exibir as informações, além de mais harmônico para a interface)
def listar_agendamentos():
    if not agendamentos:
        messagebox.showinfo("Agendamentos", "Nenhum agendamento registrado ainda.")
    else:
        lista_agendamentos = "\n".join([f"{agendamento['nome']} - {agendamento['data']} às {agendamento['horario']}" for agendamento in agendamentos])
        messagebox.showinfo("Lista de Agendamentos", lista_agendamentos)

# Configuração da interface gráfica (Será desenvolvido)
ctk.set_appearance_mode("white")
ctk.set_default_color_theme("dark-blue")

interface = ctk.CTk()
interface.title("Barbearia (Projeto)")
interface.geometry("1920x1080")

frame = ctk.CTkFrame(interface)
frame.pack(pady=20, padx=20, fill="both", expand=True)

adicionar_titulo = ctk.CTkLabel(frame, text="Gerenciamento de barbearia (Teste)", font=("Calisto MT", 24))
adicionar_titulo.pack(pady=12, padx=10)

# Configurações para adicionar cliente no sistema
adicionar_nome = ctk.CTkLabel(frame, text="Nome")
adicionar_nome.pack()
add_nome = ctk.CTkEntry(frame)
add_nome.pack(pady=2)

adicionar_sobrenome = ctk.CTkLabel(frame, text="Sobrenome")
adicionar_sobrenome.pack()
add_sobrenome = ctk.CTkEntry(frame)
add_sobrenome.pack(pady=2)

adicionar_telefone = ctk.CTkLabel(frame, text="Telefone")
adicionar_telefone.pack()
add_telefone = ctk.CTkEntry(frame)
add_telefone.pack(pady=2)

adicionar_email = ctk.CTkLabel(frame, text="E-mail")
adicionar_email.pack()
add_email = ctk.CTkEntry(frame)
add_email.pack(pady=2)

botão_adicionar = ctk.CTkButton(frame, text="Adicionar Cliente", command=adicionar_cliente)
botão_adicionar.pack(pady=2)

# Buscar clientes cadastrados
label_busca = ctk.CTkLabel(frame, text="Buscar Cliente por Nome")
label_busca.pack()
add_busca = ctk.CTkEntry(frame)
add_busca.pack(pady=2)

botão_buscar = ctk.CTkButton(frame, text="Buscar Cliente", command=buscar_cliente)
botão_buscar.pack(pady=2)

# Agendamento de horários
label_agenda_nome = ctk.CTkLabel(frame, text="Nome do Cliente")
label_agenda_nome.pack()
add_agenda_nome = ctk.CTkEntry(frame)
add_agenda_nome.pack(pady=2)

label_agenda_data = ctk.CTkLabel(frame, text="Data")
label_agenda_data.pack()
add_agenda_data = ctk.CTkEntry(frame)
add_agenda_data.pack(pady=2)

label_agenda_horario = ctk.CTkLabel(frame, text="Horário")
label_agenda_horario.pack()
add_agenda_horario = ctk.CTkEntry(frame)
add_agenda_horario.pack(pady=2)

label_serviço = ctk.CTkLabel(frame, text="Serviço")
label_serviço.pack()
add_agenda_servico = ctk.CTkEntry(frame)
add_agenda_servico.pack(pady=2)

botão_agendar = ctk.CTkButton(frame, text="Agendar Horário", command=agendar_horario)
botão_agendar.pack(pady=2)

# Listar clientes de agendamentos no programa
botão_listar_clientes = ctk.CTkButton(frame, text="Listar Clientes", command=listar_clientes)
botão_listar_clientes.pack(pady=2)

botão_listar_agendamentos = ctk.CTkButton(frame, text="Listar Agendamentos", command=listar_agendamentos)
botão_listar_agendamentos.pack(pady=2)

interface.mainloop()

# Correção de bugs serão realizadas durante a semana (Principalmente o do botão do agendamento)
# Modificações de fontes serão feitas
# Imagens para dar mais autenticidade serão adicionadas
# Ordenação correta dos itens (Cadastro, Agendamento, Listas de agendados e de clientes cadastrados)