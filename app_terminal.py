from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
#from dramapy import activate
import webbrowser
import threading
import statistics # em estudo...
import requests
import platform
import getpass
import random
import smtplib
import hashlib
import sqlite3
import string
import difflib#em estudo para ser usado...
import math
import time
import sys
import os
##################
def varrer():
    os.system('cls' if os.name == 'nt' else 'clear')
##################
def usuarios_SV_():
    return sqlite3.connect("usuario_SV.db")
##################
def bloco_de_notas_SV_():
    return sqlite3.connect("notas_SV.db")
##################
def data_acesso():
    return datetime.now().strftime("%d/%m/%Y")
#################
def banco():
    con = usuarios_SV_()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuario_SV (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT UNIQUE,
    senha TEXT,
    email TEXT,
    ultimo_acesso TEXT

    )  
""")  
    con.commit()  
    con.close()
###################
def banco_notas():
    con = bloco_de_notas_SV_()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notas_SV (
    id INTEGER PRIMARY KEY                         AUTOINCREMENT,
    usuario_login TEXT NOT NULL,
    titulo_nota TEXT NOT NULL,
    corpo_nota TEXT,
    UNIQUE (usuario_login, titulo_nota)
    )
""")
    con.commit()
    con.close()
###################
def continua():
    input("\n    Pressione Enter para continuar...")
##################
def enviar_email():
    con = usuarios_SV_()
    cur = con.cursor()
    cur.execute(  
        "SELECT id, email FROM usuario_SV WHERE login = ?",  
        (usuario_logado,)
)
    usuario = cur.fetchall()
    con.close()
    email = usuario[0][1]

    mensagem = MIMEMultipart()  
    mensagem["From"] = "email_aleatorio_teste@gmail.com"  
    mensagem["To"] = email  
    mensagem["Subject"] = "???"  
    texto_email = MIMEText("???", "plain")  
    mensagem.attach(texto_email)  
    mensagem.as_string()  
    fim = smtplib.SMTP("smtp.gmail.com", 587)  
    fim.starttls()  
    fim.login("email_aleatorio_teste@gmail.com", "SENHA_DO_APP")#prefiro nao mostrar minha senha de app nem email  
    fim.sendmail(mensagem["From"], mensagem["To"], mensagem.as_string())  
    fim.quit()

#################
def instalando():
    for i in range(101):
        print(f"\r\033[1m\033[91m    instalando app SV {i}%\033[0m", end="")
        time.sleep(0.06)
    print("\n\033[91m    confirmando...\033[0m")
    time.sleep(2)
    varrer()
##################
def titulo():
    print("\033[93m=\033[0m"*60)
    print("\033[1m\033[33m                    app_terminal_SV\033[0m")
    print("\033[93m=\033[0m"*60)
    print()
    print("-"*60)
    print()
#################
def titulo_funcao(titulo):
    print("\033[92m+-\033[0m"*30)
    print(f"\033[1m\033[32m  {titulo}\033[0m")
    print("\033[92m+-\033[0m"*30)
    print()
    print()
##################
def continuacao_jogo_quatro():
    continuar = input("    deseja reiniciar esta partida?:    ").lower().strip()

    if continuar == "sim":  
        print("    reiniciando...")  
        time.sleep(2)  
        varrer()  
        jogo_quatro()  
    elif continuar == "nao":  
        print("    voltando...")  
        time.sleep(1)  
        varrer()  
        jogos()  
    elif continuar == "não":  
        print("    voltando...")  
        time.sleep(1)  
        varrer()  
        jogos()

#################
def token():
    API_URL = "https://router.huggingface.co/hf-inference/models/BlinkDL/rwkv-4-mini-7b"
    API_TOKEN = "SEU_TOKEN"
    auth = {"Authorization": f"Bearer {API_TOKEN}"}
    return API_URL, auth
#################
def chat_SV_AI():
    API_URL, autorizacao = token()
    
    while True:
        entrada = input("    Ask Chat_IA_SV: ").lower()
        
        if entrada in ["sair", "exit"]:
            break
        
        data = {"inputs": entrada}
        resposta = requests.post(API_URL, headers=autorizacao, json=data)
    
        try:
            dados = resposta.json()

            if isinstance(dados, list):
                print("    IA:\n", dados[0].get("generated_text", "Sem texto"))
            elif isinstance(dados, dict):
                print("    IA:\n", dados.get("generated_text") or dados.get("error"))
            else:
                print("    erro: 110...")
                continua()
                varrer()
                continue

        except Exception as e:
            print("    erro: 1580...", e)
            continua()
            varrer()
            continue
################
def sobre():
    titulo()
    titulo_funcao("                    sobre")
    print("""    versão: 0.9 alpha
    data de inicio do projeto: 10/12/2025
    termino do projeto: ~
    apoiadores: ~
    programadores: SER VIVO.
    ideia de: SER VIVO
    nome real de SER VIVO: Dennis Alexandre
    Classificação indicativa: 14+
    créditos:\n    -ao chatGPT (openAI) por ajudar com a ideia do jogo cinco \n    -a Franciele Alexandre (mãe de SER VIVO) por testar o app durante seu desenvolvimento \n""")
    continua()
    varrer()
    interface_dois()
###################
def criptografia_de_ponta(senha):
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()
##################
def registrar_login():
    while True:
        titulo()
        titulo_funcao("                        login")

        login = input("    seu nome ou voltar para voltar:    ").lower().strip()  
      
        print()  
      
        if login in ("voltar", "sair", "2"):  
            varrer()  
            interface_um()  
  
        if login == "":  
            print("    erro: digite um nome valido...")  
            continua()  
            varrer()  
            continue  
          
        confirma_login = input("    confirme o nome:    ").lower().strip()  
  
        if confirma_login == "":  
            print("    erro: o campo de nome não pode estar vazio...")  
            continua()  
            varrer()  
            continue  
        elif confirma_login != login:  
            print("    erro: os nomes precisam ser iguais...")  
            continua()  
            varrer()  
            continue  
  
        print("    seu nome é:", login.capitalize())  
      
        idade = input("    sua idade:    ").strip()  
      
        if not idade.isdigit():  
            print("    erro: digite uma idade valida...")  
            continua()  
            varrer()  
            continue  
          
        idade = int(idade)  
      
        if idade < 14:  
            print("    erro: você deve ter 14+ anos para usar nosso app...")  
            continua()  
            varrer()  
            titulo()  
            titulo_funcao("                        fim!!!")  
            sys.exit()  
  
        senha = getpass.getpass("    diga uma senha:    ").strip()  
  
        if senha == "":  
            print("    erro: o campo de senha não pode estar vazio...")  
            continua()  
            varrer()  
            continue  
          
        digitos_senha1 = len(senha)  
      
        if digitos_senha1 < 8:  
            print("    a senha não pode ter menos de 8 digitos...")  
            continua()  
            varrer()  
            continue  
        if digitos_senha1 > 38:  
            print("    a senha não pode ter mais de 35 digitos...")  
            continua()  
            varrer()  
            continue  
          
        confirma_senha = getpass.getpass("    confirme a senha:    ").strip()  
  
        if confirma_senha == "":  
            print("    erro: o campo de senha não pode estar vazio...")  
            continua()  
            varrer()  
            continue  
        elif confirma_senha != senha:  
            print("    erro: as senhas precisam ser iguais...")  
            continua()  
            varrer()  
            continue  
      
        digito_senha = ["*"]*len(senha)  
        print("    sua senha é:", "".join(digito_senha))  
      
        email = input("    seu gmail:    ").strip()  
      
        if not email:  
            print("    erro...", "\a"*2)  
            continua()  
            varrer()  
            continue  
          
        confirma_email = input("    confirme o gmail:    ").strip()  
      
        if confirma_email != email:  
            print("    erro: os dois gmail devem ser iguais...")  
            continua()  
            varrer()  
            continue  

        if not login or not senha or not idade or not email:  
            print("    login e senha não podem estar vazios")  
            continua()  
            varrer()  
            continue  

        con = usuarios_SV_()  
        cur = con.cursor()  
        cur.execute("SELECT * FROM usuario_SV WHERE login = ?", (login,))  

        if cur.fetchone():  
            print("    o login digitado já existe.")
            con.close()  
            continua()  
            varrer()  
            entrar_login()  
            break  

        senha_criptografada = criptografia_de_ponta(senha)  

        cur.execute("INSERT INTO usuario_SV (login, senha, email) VALUES (?, ?, ?)", (login, senha_criptografada, email))  
        con.commit()  
        con.close()  

        print("    login registrado com sucesso!")  
        continua()  
        varrer()  
        entrar_login()  
        break

###################
def entrar_login():
    while True:

        titulo()  
        titulo_funcao("                            entrar")
  
        nome_login = input("    seu nome ou 1 para sair:    ").lower().strip()  
      
        if nome_login in ("1", "sair"):  
            varrer()  
            interface_um()  
            break  
        print("    seu nome é:", nome_login.capitalize())  
        print()  
      
        senha_login = getpass.getpass("    sua senha:    ").strip()  
        digitos_senha = ["*"]*len(senha_login)
        print("    sua senha é:", "".join(digitos_senha))  
        print()  

        senha_criptografada = criptografia_de_ponta(senha_login)  
      
        con = usuarios_SV_()  
        cur = con.cursor()  
        cur.execute("SELECT * FROM usuario_SV WHERE login = ? AND senha = ?", (nome_login, senha_criptografada))  
        usuario = cur.fetchone()  
        con.close()  
      
        if usuario:  
            global usuario_logado  
            usuario_logado = nome_login  
            data = data_acesso()  
            con = usuarios_SV_()  
            cur = con.cursor()  
            cur.execute("UPDATE usuario_SV SET ultimo_acesso = ? WHERE login = ?",  
            (data, usuario_logado)  
)  
            con.commit()  
            con.close()
            print("    acesso permitido...")
            time.sleep(3)
            print()  
            continua()  
            varrer()  
            interface_dois()  
            break  
        else:  
            print("    login não existente ou senha incorreta")  
            continua()  
            varrer()  
            continue

#####################
def nova_nota():
    while True:
        titulo()
        titulo_funcao("                    notas SV")

        nota = []  
  
        titulo_nota = input("    titulo da nota:    ").lower().strip()  
      
        if not titulo_nota:  
            print("    erro: titulo não pode estar vazio")  
            continua()  
            varrer()  
            continue  
      
        print("    digite a nota e de duplo enter para finalizala: ")  
  
        print()  
  
        print("    nota:")  
      
        while True:  
          
            linha_nota = input("    ")  
      
            nota.append(linha_nota)  
      
            if linha_nota == "":  
                nota.pop()  
                for i in range(101):  
                    print(f"\r\033[1m\033[91m    salvando nota {i}%\033[0m", end="")  
                    time.sleep(0.03)  
                print("\n\033[91m    confirmando...\033[0m")  
                time.sleep(2)  
                nota_pronta = "\n".join(nota)  
                con = bloco_de_notas_SV_()  
                cur = con.cursor()  
                cur.execute("INSERT INTO notas_SV (usuario_login, titulo_nota, corpo_nota) VALUES (?, ?, ?)", (usuario_logado, titulo_nota, nota_pronta))
                con.commit()  
                con.close()  
              
                escolhe = input("""    digite
    1-para.voltar ao menu anterior   
    2-para ver nota
    3-para escrever outra nota:    """).lower().strip()  
    
                if escolhe == "1":  
                    varrer()  
                    notas()  
                    break  
                elif escolhe == "2":  
                    print("    opção em desemvolvimento aquarde ser adcionada;")  
                    continua()  
                    varrer()  
                    notas()  
                    break  
                elif escolhe == "3":  
                    varrer()  
                    break  
                else:  
                    print("    erro: degite apenas 1, 2 ou 3")  
                    continua()  
                    varrer()  
                    continue
####################
def nota_ja_existente():
    while True:
        titulo()
        titulo_funcao("                    nota já existente")
    
        print("""    escolha:
    1-ver notas
    2-editar nota
    3-voltar""")

        nota_existente = input("    opção:    ").lower().strip()  
  
        if nota_existente in ("1", "ver", "ver nota"):  
            varrer()  
            ver_nota()  
            break  
        elif nota_existente in ("2", "editar", "editar nota"):  
            print("    opção 2 em desenvolvimento aquarde ser adcionada...")  
            continua()  
            varrer()  
            continue  
        elif nota_existente in ("3", "voltar"):  
            varrer()  
            notas()  
            break  
        else:  
            print("    erro: responda apenas com 1, 2 ou 3...")  
            continua()  
            varrer()  
            continue
###################
def ver_nota():
    while True:
        titulo()
        titulo_funcao("                        album de notas SV")

        con = bloco_de_notas_SV_()  
        cur = con.cursor()  

        cur.execute("SELECT id, titulo_nota FROM notas_SV WHERE usuario_login = ?",  
        (usuario_logado,)  
)  
        notas = cur.fetchall()  
        con.close()  
      
        if not notas:  
            print("    nenhuma nota encontrada")  
            continua()  
            varrer()  
            nota_ja_existente()  
            break   
        else:  
            for i, (id_, titulo_nota) in enumerate(notas, 1):  
                print(f"    {i}- {titulo_nota}")  
              
            continua()  
            varrer()  
            nota_ja_existente()  
            break
##################
def notas():
    while True:
        titulo()
        titulo_funcao("                        notas")

        print("""    opções de nota:  
    1-nova nota  
    2-nota já existente  
    3-voltar""")  
  
        escolha_nota = input("    qual opção deseja?:    ").lower().strip()  
  
        if escolha_nota in ("1", "nova nota", "nova"):  
            print("    processando...")  
            varrer()  
            nova_nota()  
        elif escolha_nota == "2":  
            varrer()  
            nota_ja_existente()  
            break  
        elif escolha_nota in ("3", "voltar"):  
            varrer()  
            utilidades()  
            break  
        else:  
            print("\033[91m    erro: digite apenas 1,2 ou 3...")  
            continua()  
            varrer()  
            continue
######################
def relogio():
    while True:
        titulo()
        titulo_funcao("                    relogio")

        print("""    1-data e hora   
    2-temporizador  
    3-cronometro  
    4-temporizador_bip  
    5-voltar""")  
  
        escolha_relogio = input("    escolha:    ").lower().strip()  
  
        if escolha_relogio in ("1", "data", "hora", "data e hora"):  
            varrer()  
            relogio_oficial()  
            break  
        elif escolha_relogio == "2":  
            print("    aguarde...")  
            time.sleep(3)  
            varrer()  
            temporizador()  
            break  
        elif escolha_relogio == "3":  
            cronometro()  
            varrer()  
            break  
        elif escolha_relogio == "4":  
            print("    ...")  
            time.sleep(2)  
            varrer()  
            temporizador_bip()  
            break  
        elif escolha_relogio == "5":  
            varrer()  
            utilidades()  
            break  
        else:  
            print("    resposta invalida responda apenas 1,2,3,4 ou 5:")  
            continua()  
            varrer()  
            continue
#####################
def relogio_oficial():
    titulo()
    titulo_funcao("                    data e hora")

    inicio = time.time()  

    parar = False  

    def espera_enter():  
        nonlocal parar  
        input()  
    parar = True  

    threading.Thread(target=espera_enter, daemon=True).start()  

    while not parar:  
        data = time.localtime()  
        print(f"    {data.tm_mday:02d}/{data.tm_mon:02d}/{data.tm_year}")  
        print(f"    {data.tm_hour:02d}:{data.tm_min:02d}:{data.tm_sec:02d}", end="")  
        time.sleep(1)  

    continua()  
    varrer()  
    relogio()
####################
def cronometro():
    titulo()
    titulo_funcao("                    cronometro")
    print("    pressione ENTER para parar")

    inicio = time.time()  

    parar = False  

    def espera_enter():  
        nonlocal parar  
        input()  
        parar = True  

    threading.Thread(target=espera_enter, daemon=True).start()  

    while not parar:  
        tempo = int(time.time() - inicio)  
        minutos = tempo // 60  
        segundos = tempo % 60  
        print(f"\r    Tempo: {minutos:02d}:{segundos:02d}", end="")  
        time.sleep(1)  

    print("    cronômetro travado:")  
    continua()  
    varrer()  
    relogio()
####################
def temporizador():
    while True:
        titulo()
        titulo_funcao("            temporizador")

        print("""    digite o tempo minutos  
    ou sair para sair""")  
      
        tempo = input("    tempo:    ").strip().lower()

        if tempo == "sair":  
            varrer()  
            relogio()  
            break  
      
        if not tempo.isdigit():  
            print("    erro: numero invalido...")  
            continua()  
            varrer()  
            continue  

        segundos = int(tempo)*60  
      
        while segundos:    
            minutos, seg = divmod(segundos, 60)  
            print(f"    tempo restante: {minutos:02d}:{seg:02d}", end='\r')  
            time.sleep(1)    
            segundos -= 1  
  
        print("    fim!")  
        continua()  
        varrer()  
        continue
####################
def temporizador_bip():
    while True:
        titulo()
        titulo_funcao("            despertador_bip")

        print("""    digite o tempo minutos ou sair para sair""")  
      
        tempo = input("    tempo:    ").strip()  

        if tempo == "sair":  
            varrer()  
            relogio()  
            break  
      
        if not tempo.isdigit():  
            print("    erro: numero invalido...")  
            continua()  
            varrer()  
            continue  

        segundos = int(tempo)*60  
      
        while segundos:    
            minutos, seg = divmod(segundos, 60)  
            print(f"    tempo restante: {minutos:02d}:{seg:02d}", end='\r')  
            time.sleep(1)    
            segundos -= 1  
  
        print("    fim!", "\a"*5)  
        continua()  
        varrer()  
        continue
###################
def meu_usuario():
    while True:
        titulo()
        titulo_funcao("                    meu usuario")

        minha_senha = getpass.getpass("    sua senha:    ").strip()  
        digitoss_senha = ["*"]*len(minha_senha)  
        print("    sua senha é:", "".join(digitoss_senha))  
        print()  

        senha_criptografada = criptografia_de_ponta(minha_senha)  
      
        con = usuarios_SV_()  
        cur = con.cursor()  
        cur.execute("SELECT login, ultimo_acesso FROM usuario_SV WHERE login = ? AND senha = ?", (usuario_logado, senha_criptografada))  
        usuario = cur.fetchone()  
        con.close()  
      
        if not usuario:  
            print("    erro: senha incorreta...")  
            continua()  
            continue  
      
        nome, ultimo_acesso = usuario  
        print("    nome:", usuario_logado.capitalize())  
        print("    senha:", "".join(digitoss_senha))
        print("    ultimo acesso em:", ultimo_acesso if ultimo_acesso else "~/~/~")  
        print("    sistema operacional sendo usado:", platform.system())  
        print("    média de ganhos nos jogos: ~")  
        print("    jogo preferido: ~")  
        print("    quantidade de notas: ~")  
        print("    ultima nota: ~")  
      
        continua()  
        varrer()  
        interface_dois()
##################
def calculadora():
    while True:
        titulo()
        titulo_funcao("                        calculadora")

        numero_um = input("    digite o primeiro numero:    ").strip()  

        if not numero_um.replace(".", "", 1).isdigit():  
            print("    erro: digite um número válido")  
            continua()  
            varrer()  
            continue  

        numero_um = float(numero_um)  

        print()  

        operacao = input("""    operação:  
    +  soma  
    -  subtração  
    x  multiplicação  
    ÷  divisão  
    P  potência  
    R  raiz quadrada  
    F  fatorial  
    %  porcentagem""")
    
        operacao = input("    escolha:    ").lower().strip()  

        print()  

        if operacao in ("r", "f"):  
            numero_dois = None  
          
        else:  
            numero_dois = input("    diga outro numero:    ").strip()  

            if not numero_dois.replace(".", "", 1).isdigit():  
                print("    erro: digite um número válido")  
                continua()  
                varrer()  
                continue  

            numero_dois = float(numero_dois)  

        try:  
            if operacao == "+":  
                total = numero_um + numero_dois  
            elif operacao == "-":  
                total = numero_um - numero_dois  
            elif operacao in ("x", "×", "*"):  
                total = numero_um * numero_dois  
            elif operacao in ("÷", "/"):  
                if numero_dois == 0:  
                    print("    erro: não é possivel dividir por 0")  
                    continua()  
                    varrer()  
                    continue  
                total = numero_um / numero_dois  
            elif operacao == "p":  
                total = math.pow(numero_um, numero_dois)  
            elif operacao == "r":  
                if numero_um < 0:  
                    print("    erro: não é posivel raiz negativa")  
                    continua()  
                    varrer()  
                    continue  
                total = math.sqrt(numero_um)  
            elif operacao == "f":  
                if numero_um < 0 or not numero_um.is_integer():  
                    print("    erro: o numero necessita ser positivo")  
                    continua()  
                    varrer()  
                    continue  
                total = math.factorial(int(numero_um))  
            elif operacao == "%":  
                total = (numero_um * numero_dois) / 100  
            else:  
                print("    erro: operação inválida") 
                continua()  
                varrer()  
                continue  
        except Exception as e:  
            print("    erro inesperado:", e)  
            continua()  
            varrer()  
            continue  

        input("    pressione Enter para calcular...")  
        print("    calculando...")  
        time.sleep(1)  

        print("\n    o resultado da conta é:", total)  

        print()  
        continuar = input("    deseja realizar outra conta?:    ").lower().strip()  

        if continuar == "sim":  
            varrer()  
            continue  
        else:  
            varrer()  
            utilidades()  
            break
#################
def gerador_senhas():
    while True:
        titulo()
        titulo_funcao("                    gerador de senhas SV")

        quantidade = input("    quantos caracteres quer que tenha sua senha?:    ")  
        if not quantidade:  
            print("    erro: digite algo...")  
            continua()  
            varrer()  
            continue  
     
        print("    gerando a senha...")  
        espera_e = random.randint(1,2)  
        time.sleep(espera_e)  
  
        if not quantidade.isdigit():  
            print("    erro: digite apenas numeros:")  
            print("    iniciando...")  
            espera_f = random.randint(1,3)  
            time.sleep(espera_f)  
            continue  
              
        quantidade = int(quantidade)  
      
        if quantidade > 350:  
            print("    erro: a senha deve ter menos de 350 digitos...")  
            continua()  
            varrer()  
            continue  
      
        caracteres = string.ascii_letters + string.digits + r"+=%|<>{)]!@#$/&^*(\~-?"  

        senha = ''.join(random.choices(caracteres, k=quantidade))  
      
        print()  
      
        print("    sua senha é:", senha)  
          
        print()  
          
        while True:  
      
            continua = input("    deseja continuar?:    ").lower().strip()  
          
            if not continua:  
                print("    erro: digite sim ou nao...")  
                continua()  
                varrer()  
                continue  
          
            if continua not in ("sim", "nao", "não"):  
                print("    erro: responda apenas com sim ou nao...")  
                continua()  
                varrer()  
                continue  
            if continua == "sim":  
                print("    reiniciando...")  
                espera_h = random.randint(1,3)  
                time.sleep(espera_h)  
                varrer()  
                gerador_senhas()  
                break  
            elif continua in ("nao", "não"):  
                print("    encerrando...")  
                espera_i = random.randint(1,2)  
                time.sleep(espera_i)  
                varrer()  
                utilidades()  
                break  
            break  
        break
################
def desenvolvedor_SV():
    titulo()
    titulo_funcao("                    desenvolvedor")
    print("    esta função será adcionada na proxima versão, aguarde...")  
    SV = input("    Precione Enter para continuar...").lower().strip()  
  
    if SV == "sv":  
        varrer()  
        banco()  
        banco_notas()  
        global usuario_logado
        usuario_logado = "__DEV_user_SV__"  
        interface_dois()  
    else:  
        varrer()  
        interface_um()
###############
def gerador_nomes():
    while True:
        titulo()
        titulo_funcao("                        gerador de nomes SV")

        nomes_f = ("ana", "paula", "fernanda", "juana", "franciele", "aryane", "cida", "alesandra", "gabriela", "julia")  
      
        nomes_m = ("dennis", "denis", "alexandre", "alesandro", "alecsandro", "joão", "vitor", "zé", "josé", "lucas", "luca", "davi")  
      
        nomes_a = (nomes_f, nomes_m)  
      
        print("""    escolha:  
    1-nome feminino  
    2-nome mascolino  
    3-aleatorio  
    4-voltar""")  
      
        escolha_nome = input("    sua escolha:    ").lower().strip()  
      
        if escolha_nome not in ("feminino", "f", "masculino", "m", "aleatorio", "a", "voltar", "v", "1", "2", "3", "4"):  
            print("    erro: responda apenas 1, 2, 3 ou 4...")  
            continua()  
            varrer()  
            continue  
        elif escolha_nome in ("1", "f", "feminino"):  
            nome = random.choice(nomes_f)  
            print("o nome é:", nome.capitalize())
            print()  
            continua()  
            varrer()  
            continue  
        elif escolha_nome in ("2", "m", "masculino"):  
            nome = random.choice(nomes_m)  
            print("o nome é:", nome.capitalize())
            print()  
            continua()  
            varrer()  
            continue  
        elif escolha_nome in ("3", "v", "aleatorio"):  
            sexo = random.choice(nomes_a)  
            nome = random.choice(sexo)  
            print("o nome é:", nome.capitalize())  
            print()  
            continua()  
            varrer()  
            continue  
        else:  
            return
##############
def jogo_um():
    while True:
        titulo()
        titulo_funcao("                    jogo de advinhação SVgames")

        tentativas = 10  
  
        print()  
  
        print("    atenção: você tem apenas 10 tentativas")  
  
        num_sorteado = random.randint(1,50)  
  
        while True:  
      
            print()  
      
            num_adivinhado = input("    tente adivinhar o numero de 1 a 50:    ").strip()  
      
            print()  
      
            if not num_adivinhado.isdigit():  
                print("    digite apenas numeros") 
                continua()  
                varrer()  
                continue  
          
            num_adivinhado = int(num_adivinhado)  
      
            if num_adivinhado > 50:  
                print("    atenção os numeros são de 1 a 50")  
                print()  
                continua()  
                varrer()  
                continue  
      
            tentativas -= 1  
      
            if tentativas == 0:  
                print()  
                print()  
                print("    suas tentativas acabaram")  
                print("    esta partida será reiniciada")  
                print("    reiniciando...")  
                time.sleep(5)  
                varrer()  
                break  
      
            if num_adivinhado < num_sorteado:  
                print("    o numero que estou pensando é maior")  
                print()  
                continua()  
                varrer()  
                continue  
            elif num_adivinhado > num_sorteado:
                print("    o numero que estou pensando é menor")  
                print()  
                continua()  
                varrer()  
                continue      
            else:  
                print("    parabens você acertou faltando", tentativas, "tentativas")  
          
            print()  
          
            continuar = input("    deseja continuar esta partida?:    ").lower().strip() 
      
            if continuar == "sim":  
                print("    reiniciando...")  
                time.sleep(2)  
                varrer()  
                num_sorteado = random.randint(1,50)
                tentativas = 10  
                continue  
            elif continuar == "nao":  
                print("    voltando...")  
                time.sleep(1)  
                varrer()  
                jogos()  
                break  
            elif continuar == "não":  
                print("    voltando...")  
                time.sleep(1)  
                varrer()  
                jogos()  
                break
###################
def jogo_dois():
    while True:
        titulo()  
        titulo_funcao("                simulador de dado SVgames")  
  
        input("    de enter para jogar o dado...")  
  
        print("    rodando o dado...")  
        time.sleep(5)  
  
        numero_dado = random.randint(1,6)  
  
        print("    o dado sorteou o numero:", numero_dado)  
  
        print()  
  
        outra_vez = input("""    digite:  
    1-para sair do jogo  
    2-para jogar novamente  
    :    """).lower().strip()  
  
        if outra_vez == "1":  
            varrer()  
            jogos()  
            break  
        elif outra_vez == "2":  
            varrer()  
            continue  
        else:  
            print("    erro")  
            continua()  
            varrer()  
            jogos()
###################
def jogo_tres():
    while True:
        titulo()
        titulo_funcao("                pedra, papel ou tesoura SVgames")

        print("""    escolha:  
    1-pedra  
    2-papel  
    3-tesoura  
    4-sair""")  
      
        opcao_jogo = input("    qual arma usará?:    ").lower().strip()  
  
        opcoes_jogada_pc = ("pedra", "papel", "tesoura")  
      
        jogada_pc = random.choice(opcoes_jogada_pc)  
      
        if opcao_jogo not in ("pedra", "papel", "tesoura", "sair", "1", "2", "3", "4"):  
            print("    erro: digite apenas pedra, papel ou tesoura...")  
            continua()  
            varrer()  
            continue  
        elif opcao_jogo in ("4", "sair"):  
            varrer()  
            jogos()  
            break  
          
        mapa = {  
    "1": "pedra",  
    "2": "papel",  
    "3": "tesoura"

}

        if opcao_jogo in mapa:  
            opcao_jogo = mapa[opcao_jogo]  
          
        if opcao_jogo == jogada_pc:  
            print("    temos um empate!!!")  
            continua()  
            varrer()  
            continue  
        elif ((opcao_jogo == "pedra" and jogada_pc == "tesoura") or (opcao_jogo == "tesoura" and jogada_pc == "papel") or (opcao_jogo == "papel" and jogada_pc == "pedra")):  
            print("    computador:", jogada_pc, "você ganhou")  
            continua()  
            varrer()  
            continue  
        else:  
            print("    computador:", jogada_pc, "você perdeu")  
            continua()  
            varrer()  
            continue
###################
def jogo_quatro():
    titulo()
    titulo_funcao("                jogo da forca SVgames")

    palavras = ("VENTILADOR", "COPO", "PRATO", "TV", "CHINELO", "MESA", "CHAPEU", "CELULAR", "CAMA", "ROUPA", "SOFA", "PENTE", "COROA", "MOEDA", "COLHER")  

    palavra_sorteada = random.choice(palavras)    

    total_letras = len(palavra_sorteada)  
    lista_l_p = list(palavra_sorteada)    
    lista_s_p = ["_"]*len(palavra_sorteada)    

    chances = 6    
    acertos = 0    
    letras_chutadas = []    
    ganhou = 0    

    print()    
    
    while True:    
    
        print()    
        print()    
    
        print("    pensando na palavra...")    
        tempo3 = random.randint(5,8)    
        time.sleep(tempo3)    
    
        print()    
    
        print("#"*60)    
        print("    atencão:")    
        print("    você tem apenas", chances, "chances para acertar")    
        print("    você já acertou", acertos, "letras do total de", total_letras, "letras")    
        print("    você já ganhou", ganhou, "partidas")    
        print("    letras chutadas:", letras_chutadas)    
        print("#"*60)    
    
        print()    
    
        print("    carregando restante do jogo...")    
        time.sleep(3)    
    
        print()    
        print()    
        
        print("    pronto!")    
    
        print()    
    
        print("    palavra:")    
        print("    "," ".join(lista_s_p))    
    
        while True:    
    
            print()    
    
            chutes = str(input("    tente a sorte: diga uma letra:    ")).upper().strip()  
            print("    processando resposta...")
            time.sleep(3)  
            print()  
          
            digitos_chutes = len(chutes)  
          
            if chutes == "":  
                print("    erro: é necessario digitar alguma letra:")  
                print()  
                continua()  
                print()  
                continue  
            elif digitos_chutes > 1:  
                print("    erro: digite apenas uma letra...")  
                print()  
                continua()  
                varrer()  
                continue  
              
            if chutes in letras_chutadas:  
                print("    você já chutou essa letra tente uma letra diferente...")  
                continua()  
                continue  
              
            if chances == 0:  
                print("    chances zeradas você perdeu")  
                print("    a palavra era:", palavra_sorteada)  
                continua()  
                continuacao_jogo_quatro()  
                break  
  
            if "_" not in lista_s_p:  
                print("    parabens você ganhou") 
                print("    a palavra erá:", palavra_sorteada)  
                ganhou += 1  
                continua()  
                continuacao_jogo_quatro()  
                break  
              
            letras_chutadas.append(chutes)  
        
            if chutes in palavra_sorteada:  
                print("    parabens você acertou uma letra:")    
                print()    
                print("    chances:", chances)    
                print("    letras chutadas:", ",".join(letras_chutadas))  
                for i in range(len(palavra_sorteada)):    
                    if palavra_sorteada[i] == chutes:    
                        lista_s_p[i] = chutes    
                        acertos += 1   
                print("    acertos:", acertos)   
                print()    
                print("    palavra:")    
                print("    "," ".join(lista_s_p))  
                continue  
            else:  
                print("    letra errada tente novamente:")    
                chances -=1  
                print()    
                print("    chances:", chances)    
                print("    letras chutadas", letras_chutadas)    
                print("    acertos:", acertos)    
                print()    
                print("    palavra:")    
                print("    "," ".join(lista_s_p))  
                continue
###################
def jogo_cinco():
    while True:
        titulo()
        titulo_funcao("                    aventuras_SV")

        print("""    tema:  
    1-investigação da mansão roubada  
    2-fuga da prisão  
    3-fazendo trilha na amazonia  
    4-a procura de lucas  
    5-voltar""")
    
        tema = input("    diga qual tema quer:    ").lower().strip()  
      
        if tema not in ("1", "2", "3", "4", "5"):  
            print("responda apenas 1, 2, 3, 4 ou 5")  
            continua()  
            varrer()  
            continue  
        elif tema == "1":  
            varrer()  
            jogo_cinco_1()  
            break  
        elif tema == "2":  
            jogo_cinco_2()  
        elif tema == "3":  
            print("    jogo em desenvolvimento, aquarde ser adcionado...")  
            continua()  
            varrer()  
            continue  
        elif tema == "4":  
            print("    jogo em desenvolvimento, aquarde ser adcionado...")  
            continua()  
            varrer()  
            continue  
        elif tema == "5":  
            continua()  
            varrer()  
            jogos()
##################
def jogo_cinco_1():
    sessao = 0

    while True:  
        titulo()  
        titulo_funcao("                    misterios_SV")  
      
        if sessao == 0:  
            print("""    uma mansão foi roubada e nela avia uma formula de um  
 remedio milagroso e você é o investigador do caso""")  
            print("""    o que você faz:  
    1-investiga a mansão  
    2-fala com o dono da mansão  
    3-desiste do caso""")  
            investiga = input("    :    ").lower().strip()  
      
            if investiga not in ("1", "2", "3"):  
                print("    responda apenas 1, 2 ou 3...")  
                continua()  
                varrer()  
                continue  
            elif investiga == "1":  
                varrer()  
                sessao += 1  
            elif investiga == "2":  
                varrer()  
                sessao +=2  
            elif investiga == "3":  
                print("    desistencia em processamento...")  
                time.sleep(0.5)  
                continua()  
                varrer()  
                jogos()  
                break  
              
        elif sessao == 1:  
            print("""    já dentro da mansão você encontra na sala principal \n um papel no chão com algo excrito e um notebook na mesa""")  
            print("""    o que você faz:  
    1-pega o papel e le  
    2-da uma olhada no notebook  
    3-ignora ambos e continua a olhar a casa""")  
            investiga2 = input("    :    ").strip()  
          
            if investiga2 not in ("1","2","3"):  
                print("    responda apenas 1, 2 ou 3...")  
                continua()  
                varrer()  
                continue  
            elif investiga2 == "1":  
                varrer()  
                sessao +=2  
            elif investiga2 == "2":  
                varrer()  
                sessao +=3  
            elif investiga2 == "3":  
                varrer()  
                sessao +=4  
              
        elif sessao == 2:  
            print("    o dono da mansão não tem nenhuma informação importante")  
            print("""    o que você faz:  
    1-tortura o dono para falar  
    2-investiga a mansão""")  
            investiga3 = input("    :    ").strip()  
          
            if investiga3 not in ("1","2"):  
                print("    responda apenas  1 ou 2...")  
                continua()  
                varrer()  
                continue  
            elif investiga3 == "1":  
                varrer()  
                sessao +=4  
            elif investiga3 == "2":  
                varrer()  
                sessao -=1  
              
        elif sessao == 3:  
            print("    no papel esta escrito: não foi o irmão do dono")  
            print("""    o que você faz:  
    1-investiga o irmão do dono  
    2-acredita no papel e volta a investigar a casa""")  
            investiga4 = input("    :    ")  
          
            if investiga4 not in ("1","2"):  
                print("    responda apenas com 1 ou 2...")  
                continua()  
                varrer()  
                continue  
            elif investiga4 == "1":  
                varrer()  
                sessao +=4  
            elif investiga4 == "2":  
                varrer()  
                sessao -=2  
              
        elif sessao == 4:  
            print("    no notebook só tem o app das cameras da casa")  
            print("""    o que você faz:  
    1-olha as cameras  
    2-resolve dar uma olhada no papel que estava no chão""")  
            investiga5 = input("    :    ")  
          
            if investiga5 not in ("1","2"):  
                print("    responda apenas com 1 ou 2...")  
                continua()  
                varrer()  
                continue  
            elif investiga5 == "1":  
                varrer()  
                sessao +=4  
            elif investiga5 == "2":  
                varrer()  
                sessao -=1  
              
        elif sessao == 5:  
            print("""    no quarto do cofre você da uma olhada no cofre e \n percebe que o cofre onde estava a formula não foi arrombado mas sim \n desbloqueado com a senha que só o dono sabia""")  
            print("""    o que você faz:  
    1-confirma que foi o dono  
    2-investiga o dono""")  
            investiga6 = input("    :    ")  
          
            if investiga6 not in ("1","2"):  
                print("    responda apenas 1 ou 2...")
                continua()  
                varrer()  
                continue  
            elif investiga6 == "1":  
                print("    parabéns detetive, você ganhou o jogo...")  
                continua()  
                varrer()  
                jogos()  
                break  
            elif investiga6 == "2":  
                varrer()  
                sessao -=3  
              
        elif sessao == 6:  
            print("""    parabéns detetive, o dono confesou que era tudo mentira""")  
            continua()  
            varrer()  
            jogos()  
            break  
          
        elif sessao == 7:  
            print("""    parabéns detetive, o irmão do dono confesou que \n foi ele por inveja do irmão""")  
            continua()  
            varrer()  
            jogos()  
            break  
          
        elif sessao == 8:  
            print("""    parabéns detetive, as comeras mostraram \n que o ladrão era o professor de faculdade do dono""")  
            continua()  
            varrer()  
            jogos()  
            break
##################
def jogo_cinco_2():
    sessao = 0
    ganho = 0
    escolhas = 0

    titulo()  
    titulo_funcao("                    RPG SVgames")  
  
    while True:  
      
        if sessao == 0:  
            print("    você foi preso injustamente em uma prisão longe da civilização e precisa fugir dela o mais rapido posivel")  
            print("""    o que você faz:  
    1-tenta fugir  
    2-aceita o destino e fica preso  
    3-voltar""")  
            escolha_fuga1 = input("    :    ").strip()  
          
            if escolha_fuga1 not in ("1", "2", "3"):
                print("    erro: responda apenas 1, 2 ou 3...")  
                continua()  
                varrer()  
                continue  
            elif escolha_fuga1 == "1":  
                escolha +=1  
                sessao +=1  
            elif escolha_fuga1 == "3":  
                print("você já ganhou:", ganho, "partidas e fez", escolhas, "escolhas")  
                continua()  
                varrer()  
                jogo_cinco  
                break  
            else:  
                print("    você falesceu na prisao por falta de necessidades basicas")  
                continua()  
                varrer()  
                continue  
              
        elif sessao == 1:  
            print("    já dentro da sela você ve um clip de cabelo no chão e um chaveiro perto da grade")  
            print("""    o que bocé faz:  
    1-pega o clip e tenta abrir a sela  
    2-pega o chaveiro e tenta achar a chave""")  
            escolha_fuga2 = input("    :    ").strip()  
          
            if escolha_fuga2 not in ("1", "2"):  
                print("    erro: responda apenas 1 ou 2")  
                continua()  
                varrer()  
                continue  
            elif escolha_fuga2 == "1":  
                escolha +=1  
                sessao +=1  
            elif escolha_fuga2 == "2":  
                escolha +=1  
                sessao +=2  
              
        elif sessao == 2:  
            print("    você conseguiu abrir a sela mas agora tem varios policiais atrás de você")  
            print("""    o que você faz:  
    1-tenta lutar com os puliciais e fugir  
    2-se esconder dos policiais o mais rapido possivel""")  
            escolha_fuga3 = input("    :    ").strip()  
          
            if escolha_fuga3 not in ("1", "2"):  
                print("    erro: responda apenas 1 ou 2")  
                continua()  
                varrer()  
                continue  
            elif escolha_fuga3 == "1":  
                escolha +=1  
                sessao +=2  
            elif escolha_fuga3 == "2":  
                escolha +=1  
                sessao +=3  
              
        elif sessao == 3:  
            print("    nenhuma das chaves era a da sua sela")  
            print("""    o que você faz:  
1-pega o clip de cabelo para tentar abrir  
2-tentar novamente cada chave""")  
            escolha_fuga4 = input("    :    ").strip()  
          
            if escolha_fuga4 not in ("1", "2"):  
                print("    erro: responda apenas 1 ou 2")  
                continua()  
                varrer()  
                continue  
            elif escolha_fuga4 == "1":  
                escolha += 1  
                sessao -=1  
            elif escolha_fuga4 == "2":  
                print("    você perdeu: um policial estava pasando viu você com as chaves e lhe baleou...")  
                continua()  
                print()  
                print()  
                escolha +=1  
                print("você já ganhou:", ganho, "partidas e fez", escolhas, "escolhas")  
                continua()  
                varrer()  
                sessao = 0  
                  
        elif sessao == 4:  
            print("""    escolha:  
    1-os policiais estavam armados e te baleou  
    2-os policiais prenderam você de volta na sela""")  
            escolha_fuga5 = input("    :    ").strip()  
          
            if escolha_fuga5 not in ("1", "2"):  
                print("    erro: responda apenas 1 ou 2")  
                continua()  
                varrer()  
                continue  
            elif escolha_fuga5 == "1":  
                print("    perdeu: os policiais estavam armados e te baleou")  
                continua()  
                print()  
                print()  
                escolha +=1  
                print("você já ganhou:", ganho, "partidas e fez", escolhas, "escolhas")  
                varrer()  
                sessao = 0  
            elif escolha_fuga5 == "2":  
                sessao -=3  
              
        elif sessao == 5:  
            print("    você está fugindo e avista um beco")  
            print("""    o que você faz:  
    1-entra no beco para se esconder  
    2-segue em frente""")  
            escolha_fuga6 = input("    :    ").strip()  
          
            if escolha_fuga6 not in ("1", "2"):  
                print("    erro: responda apenas 1 ou 2...")  
                continua()  
                varrer()  
                continue  
            elif escolha_fuga6 == "1":  
                escolha +=1  
                ganho +=1  
                print("    parabéns: você conseguiu se esconder e escapar")  
                continua()  
                print()  
                print()  
                print("você já ganhou:", ganho, "partidas e fez", escolhas, "escolhas")  
                continua()  
                varrer()  
                sessao = 0  
            elif escolha_fuga6 == "2":  
                print("    você perdeu: os policiais atiraram em você")  
                continua()  
                print()  
                print()  
                escolha +=1  
                print("você já ganhou:", ganho, "partidas e fez", escolhas, "escolhas")  
                continua()  
                varrer()  
                sessao = 0
#################
def utilidades():
    while True:
        titulo()
        titulo_funcao("                    utilidades")

        print("""    1-bloco de notas  
    2-relogio  
    3-calculadora  
    4-gerador de senhas  
    5-gerador de nomes  
    6-assistir videos  
    7-chat_SV_AI  
    8-voltar""")  
  
        escolha_utilidade = input("    qual das opções deseja?:    ")  
  
        if escolha_utilidade == "1":  
            print("    iniciando bloco de notas...")  
            time.sleep(3)  
            varrer()  
            notas()  
            break  
        elif escolha_utilidade in ("2", "relogio"):  
            print("    ...")  
            time.sleep(2)  
            varrer()  
            relogio()  
            break  
        elif escolha_utilidade in ("3", "calculadora"):  
            varrer()  
            calculadora()  
            break  
        elif escolha_utilidade == "4":  
            varrer()  
            gerador_senhas()  
            break  
        elif escolha_utilidade == "5":  
            varrer()  
            gerador_nomes()  
            break  
        elif escolha_utilidade == "6":  
            varrer()  
          
            titulo()  
            titulo_funcao("                        YouTube")  
          
            assistir = input("""    digite:  
    1-abrir o YouTube no navegador  
    2-voltar""").lower()  
  
            if assistir == "1":  
                webbrowser.open("https://www.youtube.com")  
            elif assistir == "2":  
                varrer()  
                utilidades()  
                break  
            else:  
                print("    erro...")  
                continua()  
                varrer()  
                utilidades()  
                break  
        elif escolha_utilidade == "7":  
            varrer()  
          
            titulo()
            titulo_funcao("                        Chat_IA_SV")
            
            ia_sv = input("""    digite:
    1-Chat_IA_SV  
    2-para ir ao site do ChatGPT
    3-para ir ao site do claude.ia
    4-para voltar""").lower()  
  
            if ia_sv == "1":
                varrer()
                chat_SV_AI()
                break
            elif ia_sv == "2":  
                webbrowser.open("https://chatgpt.com")
                utilidades()
                break
            elif ia_sv == "3":  
                webbrowser.open("https://claude.ai")
                varrer()
                interface_dois()
                break
            elif ia_sv == "4":  
                varrer() 
                interface_dois()  
                break  
            else:  
                print("\033[91m    erro... \033[0m \a")  
                continua()  
                varrer()  
                interface_dois()  
                break  
        elif escolha_utilidade in ("8", "sair"):  
            varrer()  
            interface_dois()  
            break  
        else:  
            print("\033[91m    erro: responda apenas 1,2,3,4,5,6,7 ou 8... \033[91m \a")  
            continua()  
            varrer()  
            continue
###################
def jogos():
    while True:
        titulo()
        titulo_funcao("                        jogos SVgames")
        print("""    opções de jogos:
    1-adivinhação
    2-simulador de dado
    3-pedra, papel ou tesoura
    4-jogo da forca
    5-aventuras_SV
    6-voltar""")

        jogo_escolhido = input("    qual jogo deseja jogar?:    ").lower().strip()  
  
        if jogo_escolhido == "1":  
            print("    carregando jogo...")  
            time.sleep(3)  
            varrer()  
            jogo_um()  
            break  
        elif jogo_escolhido == "2":  
            varrer()  
            jogo_dois()  
            break  
        elif jogo_escolhido == "3":  
            varrer()  
            jogo_tres()  
            break  
        elif jogo_escolhido == "4":  
            varrer()  
            jogo_quatro()  
            break  
        elif jogo_escolhido == "5":  
            varrer()  
            jogo_cinco()  
            break  
        elif jogo_escolhido == "6":  
            varrer()  
            interface_dois()  
            break  
        else:  
            print("    erro: responda apenas com 1, 2, 3...")  
            print()  
            continua()  
            varrer()  
            continue
###################
def interface_um():
    while True:
        titulo()
        titulo_funcao("                        inicio")
        
        print("""    opçãos login:
    1-entrar
    2-cadastrar
    3-desenvolvedor
    4-sair""")

        resposta_login = input("    qual opção deseja?:    ").lower().strip()
        
        if resposta_login in ("1", "entrar"):  
            varrer()  
            entrar_login()  
        elif resposta_login in ("2", "cadastrar"):  
            varrer()  
            registrar_login()  
        elif resposta_login in ("3", "desenvolvedor"):  
            varrer()  
            desenvolvedor_SV()  
            break  
        elif resposta_login in ("4", "sair"):  
            while True:  
                sair = input("    confirme que deseja sair com sim ou nao:    ").lower().strip()  
          
                if sair not in ("sim", "nao", "não"):  
                    print("    erro: responda apenas sim ou não...")  
                    continua()  
                    varrer()  
                    continue  
                elif sair in ("nao", "não"):  
                    varrer()  
                    break  
                elif sair == "sim":  
                    varrer()  
                    sys.exit()  
        else:  
            print("    resposta invalida: responda apenas 1, 2, 3 ou 4")  
            continua()  
            varrer()  
            continue
###################
def interface_dois():
    while True:
        titulo()
        titulo_funcao("                        opções_app")
        
        print("""    opções de nosso app:
    1-jogos
    2-utilidades
    3-sobre
    4-meu usuario
    5-dar sugestão de melhoria
    6-chat_SV_AI
    7-voltar""")

        escolha_oappsv = input("    qual das opçãos deseja?:    ").lower().strip()  
      
        if escolha_oappsv in ("1", "jogos"):  
            print("    carregando jogos...")  
            time.sleep(5)  
            varrer()  
            jogos()  
        elif  escolha_oappsv in ("2", "utilidades"):  
            print("    carregando...")  
            time.sleep(2)  
            varrer()  
            utilidades()  
            break  
        elif escolha_oappsv in ("3", "sobre"):  
            varrer()  
            sobre()  
            break  
        elif escolha_oappsv in ("4", "meu usuario"):  
            varrer()  
            meu_usuario() 
            break  
        elif escolha_oappsv == "5":  
            varrer()  
            input("    qual suas sugestões?:    ")  
            print("    sugestão enviada com sucesso!")  
            continua()  
            varrer()  
            continue  
        elif escolha_oappsv == "6":
            varrer()  
          
            titulo()
            titulo_funcao("                        Chat_IA_SV")
            
            ia_sv = input("""    digite:
    1-Chat_IA_SV  
    2-para ir ao site do ChatGPT
    3-para ir ao site do claude.ia
    4-para voltar""").lower()  
  
            if ia_sv == "1":
                varrer()
                chat_SV_AI()
                break
            elif ia_sv == "2":  
                webbrowser.open("https://chatgpt.com")
                utilidades()
                break
            elif ia_sv == "3":  
                webbrowser.open("https://claude.ai")
                varrer()
                interface_dois()
                break
            elif ia_sv == "4":  
                varrer() 
                interface_dois()  
                break  
            else:  
                print("\033[91m    erro... \033[0m \a")  
                continua()  
                varrer()  
                interface_dois()  
                break  
        elif escolha_oappsv == "7":  
            varrer()  
            interface_um()  
            break  
        else:  
            print("\033[91m    erro: digite apenas a opção: 1,2,3,4...")  
            continua()  
            varrer()  
            continue
##################
if __name__ == "__main__":
    banco()
    banco_notas()
    instalando()
    interface_um()