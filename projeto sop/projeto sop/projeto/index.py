from flask import Flask, render_template, request, jsonify
import mysql.connector
import json

app = Flask(__name__)

# Conexão com o banco de dados (mesmo que você ainda não tenha um banco funcionando, esse código permanecerá inalterado)
#db = mysql.connector.connect(
#    host='10.225.0.4',
#    user='20211164010012',
#    password='20211164010012+soares',
#    database='20211164010012_bancoProjeto'
#)

# Lista de palavras ofensivas a serem bloqueadas
PALAVRAS_BLOQUEADAS = ["porra", "caralho", "puta"] 

# Função para verificar se um comentário contém palavras ofensivas
def verificar_palavras_ofensivas(comentario):
    for palavra in PALAVRAS_BLOQUEADAS:
        if palavra in comentario.lower():
            return True
    return False

# Rota para renderizar a página HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('page2.html')

# Rota para receber dados do frontend e inserir no banco de dados
@app.route('/teste', methods=['POST'])
def teste():
    data = request.json
    comentario = data.get("sugestaodousuario", "")

    # Verifica se o comentário contém palavras ofensivas
    if verificar_palavras_ofensivas(comentario):
        return jsonify({'status': 'Comentário contém palavras ofensivas e não foi publicado'}), 400

    cursor = db.cursor()
    try:
        cursor.execute('INSERT INTO comments (user, comment) VALUES (%s, %s)', (data["user"], comentario))
        db.commit()
        response = jsonify({'status': 'Comentário publicado com sucesso'})
    except Exception as e:
        print(f"Erro ao inserir dados no banco de dados: {e}")
        db.rollback()
        response = jsonify({'status': 'Erro ao inserir dados no banco de dados'})
    finally:
        cursor.close()

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)