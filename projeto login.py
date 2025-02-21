import customtkinter
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager as CDM
list_usuarios = []
list_senhas = []

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')#tema da self.janela



class principal:#criando a classe

    def __init__(self):
        self.janela = customtkinter.CTk()#criando self.janela
        self.janela.geometry('500x300')

        customtkinter.CTkLabel(self.janela, text='SITE DA LAMBORGHINI \n\n se ja estiver feito o cadastro\n clique em fazer login').pack(padx=10, pady=10)

        customtkinter.CTkButton(self.janela, text='fazer login', command=self.login_entra).pack(padx=10, pady=10)
        customtkinter.CTkButton(self.janela, text='se cadastre', command=self.cadastro_usuario).pack(padx=10, pady=10)
        customtkinter.CTkButton(self.janela, text='sair', command=self.janela.destroy).pack(padx=10, pady=10)# criando butões e distancias entre eles

        self.janela.mainloop()#self.janela criada

    def cadastro_usuario(self):#criando função com argumento self que se refere a ele mesmo
        janela_cadastro = customtkinter.CTk()
        janela_cadastro.geometry('500x300')
        customtkinter.CTkButton(janela_cadastro, text='se cadastre', command=self.cadastro_usuario)
        customtkinter.CTkLabel(janela_cadastro, text='TELA DE CADASTRO').pack()

        customtkinter.StringVar(janela_cadastro, "")#ele acessa oque tem dentro do butão
        box_usuario = customtkinter.CTkEntry(janela_cadastro, placeholder_text=' seu email', width=200)
        box_usuario.pack(padx=10, pady=10)
        box_senha = customtkinter.CTkEntry(janela_cadastro, placeholder_text='sua senha', width=200, show='*')
        box_senha.pack(padx=10, pady=10)

        def pegar_dados():#pegando os dodos dentro de cada caixa
            senha_pegar = box_senha.get()
            usuario_pegar = box_usuario.get()
            list_usuarios.append(usuario_pegar)
            list_senhas.append(senha_pegar)
            print(list_usuarios, list_senhas)
            janela_cadastro.destroy()

        customtkinter.CTkButton(janela_cadastro, text='confirmar', command=pegar_dados).pack(padx=10, pady=10)

        customtkinter.CTkButton(janela_cadastro, text='sair', command=janela_cadastro.destroy).pack(padx=10, pady=10)
        janela_cadastro.mainloop()

    def login_entra(self):#self.janela de login e testando as senhas dos usuarios

        self.janela_login = customtkinter.CTk()
        self.janela_login.geometry('500x300')
        texto = customtkinter.CTkLabel(self.janela_login, text='SITE DA LAMBORGHINI')
        texto.pack(padx=10, pady=10)

        customtkinter.StringVar(self.janela_login, "")
        acessar_usuario = customtkinter.CTkEntry(self.janela_login, placeholder_text='usuario', width=200)
        acessar_usuario.pack(padx=10, pady=10)
        acessar_senha = customtkinter.CTkEntry(self.janela_login, placeholder_text='senha', width=200, show='*')
        acessar_senha.pack(padx=10, pady=10)

        def comfirma_login():#criando o comando confirma
            global indice #variavel global , que não pertece a ninguem
            pegar_login = acessar_usuario.get()# pegando usuario e senhas
            pegar_senha = acessar_senha.get()

            if pegar_login in list_usuarios:
                indice = list_usuarios.index(pegar_login)
                print(list_usuarios.index(pegar_login))

            if pegar_senha in list_senhas and pegar_senha == list_senhas[indice]:
                print('\033[34m entrada bem sucedida \033[m')
                self.acessar_site()
                self.janela_login.destroy()

            if pegar_senha not in list_senhas or pegar_login not in list_usuarios:
                customtkinter.CTkLabel(self.janela_login,text="Senha ou usuário incorretos", text_color="Red").pack()

        but_confirm = customtkinter.CTkButton(self.janela_login, text='comfirmar', command=comfirma_login)
        but_confirm.pack(padx=10, pady=10)
        customtkinter.CTkButton(self.janela_login, text='sair', command=self.janela_login.destroy).pack(padx=10, pady=10)
        
        self.janela_login.mainloop()


    def acessar_site(self):# usando selenium para entra no site
        service = webdriver.ChromeService()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.lamborghini.com/en-en")
        self.janela.geometry('1x1')
        janelinha = customtkinter.CTk()

principal()