from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuração do MySQL
# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='suaSenha',
#     database='seuBancoDeDados'
# )

# Rota para renderizar a página HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def page2():
    return render_template('page2.html')


# # Rota para receber dados do frontend e inserir no banco de dados
# @app.route('/enviar_dados', methods=['POST'])
# def enviar_dados():
#     data = request.json
#     nome = data['nome']
#     idade = data['idade']

#     cursor = db.cursor()
#     cursor.execute('INSERT INTO suaTabela (nome, idade) VALUES (%s, %s)', (nome, idade))
#     db.commit()
#     cursor.close()

#     return jsonify({'status': 'Dados inseridos com sucesso'})

if __name__ == '__main__':
    app.run( host='0.0.0.0',port=8888,debug=True)