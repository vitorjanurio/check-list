from checklist import Checklist

nome_banco = "checklist_teste.db"

banco = Checklist(nome_banco)

print(f"Banco de dados '{nome_banco}' criado e tabelas inicializadas com sucesso!")

banco.fechar_conexao()
print("Conexão com o banco de dados fechada.")