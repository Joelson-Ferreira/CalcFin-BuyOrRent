from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import NumberRange, InputRequired

class FormCalc(FlaskForm):
    valor_mensal_aluguel = FloatField('Aluguel Mensal', validators=[InputRequired()])
    valor_compra_imovel = FloatField('Valor Imóvel', validators=[InputRequired()])
    taxa_valorizacao_imovel = FloatField('Valorização Imóvel (em %)', validators=[InputRequired(), NumberRange(min=0)])
    taxa_aumento_aluguel = FloatField('Atualização Aluguel (em %)', validators=[InputRequired(), NumberRange(min=0)])
    taxa_juros_aplicacao = FloatField('Juros Aplicação (em %)', validators=[InputRequired(), NumberRange(min=0)])
    botao_calcular = SubmitField('Calcular')
    botao_limpar = SubmitField('Limpar')