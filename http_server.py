import os
import json
import time


from flask import jsonify, Flask
from flask import render_template, request, redirect
from web_helper import make_qrcode, converter_dicionário_em_query_string

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/api')
def mass_flow_run():
    return jsonify("Unimplemented...")



@app.route('/acessar_topico_em_aberto')
def acessar_topico_aberto():
    titulo = request.args.get('titulo')  
    tema = request.args.get('tema')  
    questao = request.args.get('questao')  
    
    qstring_source = {
        'titulo': titulo,
        'tema': tema,
        'questao': questao,
        'voto': 'tela_votacao',
    }

    if request.args.get('voto') is None:
        qstring = converter_dicionário_em_query_string(qstring_source)
        qstring = f'http://192.168.0.130:5000/acessar_topico_em_aberto?{qstring}'
        make_qrcode(qstring)
        return render_template('topico_por_deliberar.html', titulo=titulo, tema=tema, questao=questao)
    return render_template('tela_de_deliberacao.html', titulo=titulo, tema=tema, questao=questao)

    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)





