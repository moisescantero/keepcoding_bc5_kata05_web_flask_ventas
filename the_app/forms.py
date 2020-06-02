from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length

class ProductForm(FlaskForm):
    tipo_producto = StringField('Tipo de producto', validators=[DataRequired(), Length(min=3, message="Debe tener al menos 3 caracteres.")])
    precio_unitario = FloatField('Precio Unitario', validators=[DataRequired(message="Introduce algo, nano")])
    coste_unitario = FloatField('Coste Unitario', validators=[DataRequired()])

    submit = SubmitField('Aceptar')