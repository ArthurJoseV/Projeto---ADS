import customtkinter as ctk
from tkinter import messagebox

# Listas para guardar nome dos clientes e os agendamentos
clientes = []
agendamentos = []

# listas para guardar nome dos clientes e os agendamentos

clientes = []
agendamentos = []

# função para listar os serviços para o cliente

def menu():
    print ("\n===== Barbearia =====")
    print ("1. Adicionar cliente")
    print ("2. Listar clientes")
    print ("3. Buscar cliente")
    print ("4. Agendar horário")
    print ("5. Listar agendamentos")
    print ("6. Sair")
    return input ("Escolha uma opção: ")

# função para adição de clientes ao sistema da barbearia

def adicionar_cliente(clientes):
    nome = input("Digite o nome do cliente: ")
    sobrenome = input ("Digite seu sobrenome: ")
    telefone = input("Digite o telefone do cliente: ")
    servico = input("Digite o serviço solicitado: ")
    cliente = {
        "nome": nome,
        "sobrenome": sobrenome,
        "telefone": telefone,
        "servico": servico
}
    clientes.append(cliente)
    print(f"Cliente {nome + ' ' + sobrenome} adicionado com sucesso!")

# função para listar os clientes que foram adicionados ao sistema

def listar_clientes(clientes):
    
    # se não houver clientes registrados, será imprimida uma mensagem informando que não há clientes registrados
    if not clientes:
        print("Nenhum cliente registrado ainda.")
        
    # se já houver clientes registrados, será imprimida uma mensagem informando os nomes dos clientes
    else:
        print("\nLista de Clientes:")
        for idx, cliente in enumerate(clientes, start=1):
            print(f"{idx}. Nome: {cliente['nome']}, Sobrenome: {cliente['sobrenome']}, Telefone: {cliente['telefone']}, Serviço: {cliente['servico']}")

# função para buscar os clientes que já estão cadastrados no sistema

def buscar_cliente(clientes):
    
    # ao inserir o nome de algum cliente, vai listar quais clientes possuem aquele nome e quais estão registrados na plataforma
    nome_busca = input("Digite o nome do cliente que deseja buscar: ")
    encontrados = [cliente for cliente in clientes if nome_busca.lower() in cliente['nome'].lower()]
    if encontrados:
        print("\nClientes encontrados:")
        for cliente in encontrados:
            print(f"Nome: {cliente['nome']}, Telefone: {cliente['telefone']}, Serviço: {cliente['servico']}")
    else:
        print("Nenhum cliente encontrado com esse nome.")

# função para agendamento do serviço a ser realizado, sendo elas o nome do cliente, a data e o horário

def agendar_horario(agendamentos):
    nome = input("Digite o nome do cliente para o agendamento: ")
    sobrenome = input("Digite o sobrenome do cliente para o agendamento: ")
    data = input("Digite a data do agendamento (DD/MM/AAAA): ")
    horario = input("Digite o horário do agendamento (HH:MM): ")
    agendamento = {
        "nome": nome,
        "sobrenome": sobrenome,
        "data": data,
        "horario": horario
        }
    agendamentos.append(agendamento)
    print(f"Agendamento para {nome + ' ' + sobrenome} no dia {data} às {horario} foi registrado com sucesso!")

# função função para mostrar os agendamentos realizados para clientes e barbeiros

def listar_agendamentos(agendamentos):
    if not agendamentos:
        print("Nenhum agendamento registrado ainda.")
    else:
        print("\nLista de Agendamentos:")
        for idx, agendamento in enumerate(agendamentos, start=1):
            print(f"{idx}. Nome: {agendamento['nome']}, Data: {agendamento['data']}, Horário: {agendamento['horario']}")

# função para escolha do serviço desejado

def main():
    while True:
        opcao = menu()
        if opcao == "1":
            adicionar_cliente(clientes)
        elif opcao == "2":
            listar_clientes(clientes)
        elif opcao == "3":
            buscar_cliente(clientes)
        elif opcao == "4":
            agendar_horario(agendamentos)
        elif opcao == "5":
            listar_agendamentos(agendamentos)
        elif opcao == "6":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

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
