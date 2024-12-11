from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

#  rota para acessar a tabela 'funcionario'
@app.route('/api/funcionario', methods=['GET'])
def listar_funcionarios():
    conn = sqlite3.connect("meu_banco_de_dados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionario")
    funcionarios = cursor.fetchall()
    conn.close()
    return jsonify(funcionarios)

if __name__ == '__main__':
    app.run(debug=True)
