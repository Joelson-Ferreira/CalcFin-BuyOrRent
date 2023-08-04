import os
from flask import Flask, render_template, url_for, request, redirect
from forms import FormCalc
from calculator import calcular_valor_total_aluguel, calcular_valor_total_investimento, calcular_valorizacao_imovel, decisao_comprar_ou_alugar
app = Flask(__name__)

lista_usuarios = ['O resultado foi AAAA', 'O resultado foi BBBB', 'O resultado foi CCCC', 'O resultado foi DDDD', 'O resultado foi DDDD']

app.config['SECRET_KEY'] = os.urandom(32) #'14eb2912a289b928503809e548288a3b'

@app.route("/", methods=['GET', 'POST'])
def home():

    formCalc = FormCalc()

    if formCalc.validate_on_submit() and 'botao_calcular' in request.form:


        valor_mensal_aluguel = formCalc.valor_mensal_aluguel.data
        valor_compra_imovel = formCalc.valor_compra_imovel.data
        taxa_valorizacao_imovel = formCalc.taxa_valorizacao_imovel.data
        taxa_aumento_aluguel = formCalc.taxa_aumento_aluguel.data
        taxa_juros_aplicacao = formCalc.taxa_juros_aplicacao.data

        valor_total_aluguel = calcular_valor_total_aluguel(valor_mensal_aluguel, taxa_aumento_aluguel)
        valor_total_investido = calcular_valor_total_investimento(valor_compra_imovel, taxa_juros_aplicacao)
        valor_total_investido_lucro = round(valor_total_investido - valor_compra_imovel, 2)
        valor_imovel = calcular_valorizacao_imovel(valor_compra_imovel, taxa_valorizacao_imovel)

        decisao = decisao_comprar_ou_alugar(valor_total_aluguel, valor_total_investido, valor_imovel)

        return render_template('resultado.html', valor_total_aluguel=valor_total_aluguel, valor_imovel=valor_imovel,
                               valor_total_investido=valor_total_investido_lucro, decisao=decisao, formCalc=formCalc)
    if formCalc.validate_on_submit() and 'botao_limpar' in request.form:
        return redirect(url_for('home'))

    return render_template('calcimobiliaria.html', formCalc=formCalc)

@app.route("/contato")
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)