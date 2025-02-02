import customtkinter as ctk
 from tkinter import messagebox

 # Listas para guardar nome dos clientes e os agendamentos
 clientes = []
 agendamentos = []

 # ... (Suas funções adicionar_cliente, listar_clientes, buscar_cliente, agendar_horario, listar_agendamentos permanecem as mesmas)

 # Configuração da interface gráfica
 ctk.set_appearance_mode("white")
 ctk.set_default_color_theme("dark-blue")

 interface = ctk.CTk()
 interface.title("Barbearia (Projeto)")
 interface.geometry("1920x1080")

 # Frame principal com layout em grid
 frame_principal = ctk.CTkFrame(interface)
 frame_principal.pack(pady=20, padx=20, fill="both", expand=True)
 frame_principal.columnconfigure(0, weight=1) # Peso para a primeira coluna
 frame_principal.columnconfigure(1, weight=1) # Peso para a segunda coluna

 # Frame para adicionar cliente
 frame_adicionar = ctk.CTkFrame(frame_principal, corner_radius=10) # Bordas arredondadas
 frame_adicionar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

 adicionar_titulo = ctk.CTkLabel(frame_adicionar, text="Novo Cliente", font=("Calisto MT", 20)) # Título mais amigável
 adicionar_titulo.pack(pady=12, padx=10)

 # Labels e Entrys com melhor espaçamento e dicas
 adicionar_nome = ctk.CTkLabel(frame_adicionar, text="Nome:", anchor="w") # Alinhado à esquerda
 adicionar_nome.pack(pady=(0, 5)) # Espaçamento superior ajustado
 add_nome = ctk.CTkEntry(frame_adicionar, placeholder_text="Digite o nome") # Dica de preenchimento
 add_nome.pack(pady=(0, 10))

 # ... (Repita o padrão para os outros campos: sobrenome, telefone, email)

 botão_adicionar = ctk.CTkButton(frame_adicionar, text="Cadastrar Cliente", command=adicionar_cliente, corner_radius=8) # Botão com bordas arredondadas
 botão_adicionar.pack(pady=15)

 # Frame para agendar horário (similar ao frame_adicionar)
 frame_agendar = ctk.CTkFrame(frame_principal, corner_radius=10)
 frame_agendar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

 agendar_titulo = ctk.CTkLabel(frame_agendar, text="Agendar Horário", font=("Calisto MT", 20))
 agendar_titulo.pack(pady=12, padx=10)

 # ... (Campos e botões para agendar horário dentro do frame_agendar)

 # Frame para buscar e listar
 frame_buscar_listar = ctk.CTkFrame(frame_principal, corner_radius=10)
 frame_buscar_listar.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

 # Buscar Cliente
 label_busca = ctk.CTkLabel(frame_buscar_listar, text="Buscar Cliente:", anchor="w")
 label_busca.pack(pady=(0, 5))
 add_busca = ctk.CTkEntry(frame_buscar_listar, placeholder_text="Digite o nome para buscar")
 add_busca.pack(pady=(0, 10))

 botão_buscar = ctk.CTkButton(frame_buscar_listar, text="Buscar", command=buscar_cliente, corner_radius=8)
 botão_buscar.pack(pady=10)

 # Listar Clientes e Agendamentos (em um frame separado dentro do frame_buscar_listar)
 frame_listar = ctk.CTkFrame(frame_buscar_listar)
 frame_listar.pack(pady=(10, 0))

 botão_listar_clientes = ctk.CTkButton(frame_listar, text="Listar Clientes", command=listar_clientes, corner_radius=8)
 botão_listar_clientes.pack(pady=5, side="left", padx=(0, 5)) # Lado a lado

 botão_listar_agendamentos = ctk.CTkButton(frame_listar, text="Listar Agendamentos", command=listar_agendamentos, corner_radius=8)
 botão_listar_agendamentos.pack(pady=5, side="left")

 interface.mainloop()