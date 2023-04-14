from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import Form, SelectField, SubmitField 
from flask_sqlalchemy import SQLAlchemy

class FoodSearchForm(FlaskForm):
    choice = SelectField('Search for Recommendations', choices=[('1', 'Name'), ('2', 'Ingredient'), ('3', 'Allergen')])

    submit = SubmitField("Search for Result")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ingredients.db'

app.config["SECRET_KEY"] ="HIIII"
db = SQLAlchemy(app)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Ingredient {self.name}>'


@app.route('/')
def index():
    form = FoodSearchForm(request.form)
    if request.method == 'POST' and form.validate():
        print(f'GOT HERE, your choice was {form.choices.data}')
    return render_template('trash.html', form=form)

@app.route('/search')
def search():
    ingredient = request.args.get('ingredient')
    if ingredient == '':
        return "Please enter an ingredient in the search bar."
    else:
            return f"{ingredient} is searchable now."



@app.before_first_request
def create_db():
    db.create_all()
    ingredients = ['salt', 'pepper', 'sugar', 'flour', 'eggs', 'milk', 'butter', 'oil', 'garlic', 'onion', 'tomato',
                   'chicken', 'beef', 'pork', 'lettuce', 'spinach', 'carrots', 'potatoes', 'rice', 'pasta']
    with app.app_context():
        for ingredient in ingredients:
            db.session.add(Ingredient(name=ingredient))
        db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)