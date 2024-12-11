import sqlite3
from checklist import Checklist  # Importando a classe Checklist do arquivo checklist.py


class BancoDeDados:
    def __init__(self, db_checklist):
        self.db = Checklist(db_checklist)

    def inserir_funcionario(self, idCpf, nome, cargo):
        self.db.cursor.execute(
            "INSERT INTO funcionario (idCpf, nome, cargo) VALUES (?, ?, ?)",
            (idCpf, nome, cargo)
        )
        self.db.conexao.commit()

    def inserir_avaria(self, idAvaria, detalheAvaria):
        self.db.cursor.execute(
            "INSERT INTO avaria (idAvaria, detalheAvaria) VALUES (?, ?)",
            (idAvaria, detalheAvaria)
        )
        self.db.conexao.commit()

    def inserir_retorno(self, idRetorno, diaRetorno, horaRetorno, retorno):
        self.db.cursor.execute(
            "INSERT INTO retorno (idRetorno, diaRetorno, horaRetorno, retorno) VALUES (?, ?, ?, ?)",
            (idRetorno, diaRetorno, horaRetorno, retorno)
        )
        self.db.conexao.commit()

    def inserir_horarios(self, idHorarios, horarioRetirada, horarioChegada, diaRetirada, idRetorno):
        self.db.cursor.execute(
            "INSERT INTO horarios (idHorarios, horarioRetirada, horarioChegada, diaRetirada, idRetorno) VALUES (?, ?, ?, ?, ?)",
            (idHorarios, horarioRetirada, horarioChegada, diaRetirada, idRetorno)
        )
        self.db.conexao.commit()

    def inserir_destino(self, idDestino, cep, numero, complemento, idParada):
        self.db.cursor.execute(
            "INSERT INTO destino (idDestino, cep, numero, complemento, idParada) VALUES (?, ?, ?, ?, ?)",
            (idDestino, cep, numero, complemento, idParada)
        )
        self.db.conexao.commit()

    def inserir_veiculo(self, idVeiculo, placa, cor, quilometragemAtual, idDestino, idCpf, idAvaria, idHorarios):
        self.db.cursor.execute(
            "INSERT INTO veiculo (idVeiculo, placa, cor, quilometragemAtual, idDestino, idCpf, idAvaria, idHorarios) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (idVeiculo, placa, cor, quilometragemAtual, idDestino, idCpf, idAvaria, idHorarios)
        )
        self.db.conexao.commit()

    def inserir_parada(self, idParada, horaParada, horaSaida, cidade):
        self.db.cursor.execute(
            "INSERT INTO parada (idParada, horaParada, horaSaida, cidade) VALUES (?, ?, ?, ?)",
            (idParada, horaParada, horaSaida, cidade)
        )
        self.db.conexao.commit()

    def listar_tabelas(self):
        self.db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = self.db.cursor.fetchall()
        print("Tabelas no banco de dados:")
        for tabela in tabelas:
            print(tabela[0])

    def fechar_conexao(self):
        self.db.fechar_conexao()


def exibir_menu():
    print("\nEscolha uma opção:")
    print("1 - Cadastrar Funcionário")
    print("2 - Cadastrar Avaria")
    print("3 - Cadastrar Retorno")
    print("4 - Cadastrar Horários")
    print("5 - Cadastrar Destino")
    print("6 - Cadastrar Veículo")
    print("7 - Cadastrar Parada")
    print("0 - Sair")


def menu():
    db = BancoDeDados("meu_banco_de_dados.db")

    while True:
        exibir_menu()

        escolha = input("Digite o número da opção: ")

        if escolha == "1":
            idCpf = input("Digite o CPF do funcionário: ")
            nome = input("Digite o nome do funcionário: ")
            cargo = input("Digite o cargo do funcionário: ")
            db.inserir_funcionario(idCpf, nome, cargo)
            print("Funcionário cadastrado com sucesso!")

        elif escolha == "2":
            idAvaria = input("Digite o ID da avaria: ")
            detalheAvaria = input("Digite o detalhe da avaria: ")
            db.inserir_avaria(idAvaria, detalheAvaria)
            print("Avaria cadastrada com sucesso!")

        elif escolha == "3":
            idRetorno = input("Digite o ID do retorno: ")
            diaRetorno = input("Digite o dia do retorno (YYYY-MM-DD): ")
            horaRetorno = input("Digite a hora do retorno (HH:MM:SS): ")
            retorno = input("Digite o retorno: ")
            db.inserir_retorno(idRetorno, diaRetorno, horaRetorno, retorno)
            print("Retorno cadastrado com sucesso!")

        elif escolha == "4":
            idHorarios = input("Digite o ID dos horários: ")
            horarioRetirada = input("Digite o horário de retirada (HH:MM:SS): ")
            horarioChegada = input("Digite o horário de chegada (HH:MM:SS): ")
            diaRetirada = input("Digite o dia da retirada (YYYY-MM-DD): ")
            idRetorno = input("Digite o ID do retorno: ")
            db.inserir_horarios(idHorarios, horarioRetirada, horarioChegada, diaRetirada, idRetorno)
            print("Horários cadastrados com sucesso!")

        elif escolha == "5":
            idDestino = input("Digite o ID do destino: ")
            cep = input("Digite o CEP do destino: ")
            numero = input("Digite o número do destino: ")
            complemento = input("Digite o complemento do destino: ")
            idParada = input("Digite o ID da parada: ")
            db.inserir_destino(idDestino, cep, numero, complemento, idParada)
            print("Destino cadastrado com sucesso!")

        elif escolha == "6":
            idVeiculo = input("Digite o ID do veículo: ")
            placa = input("Digite a placa do veículo: ")
            cor = input("Digite a cor do veículo: ")
            quilometragemAtual = input("Digite a quilometragem atual do veículo: ")
            idDestino = input("Digite o ID do destino: ")
            idCpf = input("Digite o CPF do motorista: ")
            idAvaria = input("Digite o ID da avaria: ")
            idHorarios = input("Digite o ID dos horários: ")
            db.inserir_veiculo(idVeiculo, placa, cor, quilometragemAtual, idDestino, idCpf, idAvaria, idHorarios)
            print("Veículo cadastrado com sucesso!")

        elif escolha == "7":
            idParada = input("Digite o ID da parada: ")
            horaParada = input("Digite a hora da parada (HH:MM:SS): ")
            horaSaida = input("Digite a hora de saída (HH:MM:SS): ")
            cidade = input("Digite a cidade da parada: ")
            db.inserir_parada(idParada, horaParada, horaSaida, cidade)
            print("Parada cadastrada com sucesso!")

        elif escolha == "0":
            print("Saindo do menu...")
            db.fechar_conexao()
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
