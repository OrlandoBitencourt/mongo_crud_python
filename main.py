from banco_de_dados import BancoDeDados
import pandas as pd
from bson import ObjectId

"""
    1.	Criar uma classe para o banco de dados

    2.	Criar funções para todas as operações de CRUD

    3.	Deve ser possível executar as funções com e sem WHERE

    4.	A listagem (em print()) deve ser feita em formato de tabela
    •	Ex: 
    •	Nome – Cpf – Idade – Altura
    •	Gustavo – 000 – 100 – 1.8
    •	Amanda – 154 – 45 – 1.64

    5.	Deve ser feito o tratamento de erro para caso o usuário faça besteira (exceto em coisas sem controle do 
    programador. Ex: problema interno do banco)

"""


def validar_campo_float(nome_campo):
    while True:
        valor = 0.0
        valor = input(f"\ninforme valor para {nome_campo}: ")
        try:
            valor = float(valor)
        except:
            valor = 0.0
            print(f"valor incorreto para {nome_campo}.")

        if valor != 0.0 and valor != None:
            return valor


def validar_campo_int(nome_campo):
    while True:
        valor = 0
        valor = input(f"\ninforme valor para {nome_campo}: ")
        try:
            valor = int(valor)
        except:
            valor = 0
            print(f"valor incorreto para {nome_campo}.")

        if valor != 0 and valor != None:
            return valor


def validar_campo_cpf():
    while True:
        cpf = ""
        cpf = input("\ncpf: ")

        if len(cpf) == 11:
            for i in cpf:
                if i not in "0123456789":
                    pass
            else:
                return cpf
        print("Valor incorreto para o cpf, digite 11 numeros.")


def listar_valores(tipo_busca, campo):
    df = pd.DataFrame(db.executar_select(tipo_busca, campo))
    print(df)
    return True

def validar_id_existente(id):
    lista = []
    lista = db.executar_select(1, "")
    for i in lista:
        if str(id) == str(i["_id"]):
            return True
    return False

db = BancoDeDados()
db.conectar_db()

while True:
    menu = input("""
    1 - CADASTRAR
    2 - LISTAR
    3 - ATUALIZAR
    4 - DELETAR
    5 - SAIR
    Informe a opção desejada: """)
    if menu not in ("12345"):
        break
    else:
        if menu == "1":

            while True:
                nome = input("nome: ")
                if nome != "":
                    break

            cpf = validar_campo_cpf()

            idade = validar_campo_int("idade")

            altura = validar_campo_float("altura")

            dados = {}
            dados["nome"] = nome.capitalize()
            dados["cpf"] = cpf
            dados["idade"]= idade
            dados["altura"]= altura

            db.executar_insert(dados)

        elif menu == "2":

            while True:
                menu_lista = input("""
                1 - Listar tudo
                2 - Listar por id
                3 - Listar por nome
                4 - Listar por cpf
                5 - Listar por idade
                6 - Listar por altura
                7 - Voltar
                informe a opção desejada: """)
                if menu_lista not in ("1234567"):
                    break
                else:
                    if menu_lista == "1":

                        listar_valores(1, "")

                    elif menu_lista == "2":

                        listar_valores(1, "")

                        id = input("id: ")

                        listar_valores(2, id)

                    elif menu_lista == "3":

                        listar_valores(1, "")

                        while True:
                            nome = ""
                            nome = input("\nnome: ")
                            if nome != "":
                                break

                        listar_valores(3, nome)

                    elif menu_lista == "4":

                        listar_valores(1, "")

                        cpf = validar_campo_cpf()

                        listar_valores(4, cpf)

                    elif menu_lista == "5":

                        listar_valores(1, "")

                        while True:
                            idade = input("\nidade: ")
                            try:
                                idade = int(idade)
                            except:
                                print("valor incorreto para idade.")

                            if idade != "":
                                break

                        listar_valores(5, idade)

                    elif menu_lista == "6":

                        listar_valores(1, "")

                        while True:
                            altura = input("\naltura: ")
                            try:
                                altura = float(altura)
                            except:
                                print("valor incorreto para altura.")

                            if altura != "":
                                break

                        listar_valores(6, altura)

                    elif menu_lista == "7":
                        break

        elif menu == "3":
            while True:

                menu_alterar = input("\n1 - Alterar "
                                     "\n2 - Voltar"
                                     "\nDigite a opção desejada: ")
                if menu_alterar == "1":

                    listar_valores(1, "")

                    while True:
                        id = input("id: ")
                        if validar_id_existente(id):
                            break

                    while True:
                        nome = input("nome: ")
                        if nome != "":
                            break

                    cpf = validar_campo_cpf()

                    idade = validar_campo_int("idade")

                    altura = validar_campo_float("altura")

                    dados = {}
                    dados["nome"] = nome.capitalize()
                    dados["cpf"] = cpf
                    dados["idade"] = idade
                    dados["altura"] = altura

                    db.executar_update(ObjectId(id), dados)
                elif menu_alterar == "2":
                    break

        elif menu == "4":
            while True:
                menu_deletar = input("\n1 - Deletar por id"
                                     "\n2 - Deletar TUDO"
                                     "\n3 - Voltar"
                                     "\nDigite a opção desejada: ")
                if menu_deletar == "1":

                    listar_valores(1, "")

                    while True:
                        id = input("id: ")
                        if validar_id_existente(id):
                            break

                    db.executar_delete(ObjectId(id))

                elif menu_deletar == "2":
                    print("NAO")
                elif menu_deletar == "3":
                    break

        elif menu == "5":
            break