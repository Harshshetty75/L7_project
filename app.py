from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chocolate_house.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ORM Models
class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    season = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    occasion = db.Column(db.String(50), nullable=True)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.String(100), nullable=False)
    allergy_info = db.Column(db.String(255))

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    """Home route with links to all available features."""
    return render_template('home.html')

@app.route('/get_flavors', methods=['GET'])
def get_flavors():
    """Route to retrieve and display all seasonal flavors."""
    flavors = Flavor.query.all()
    return render_template('flavors.html', flavors=flavors)

@app.route('/add_flavor_form', methods=['GET', 'POST'])
def add_flavor_form():
    """Form to add a new seasonal flavor."""
    if request.method == 'POST':
        name = request.form.get('name')
        season = request.form.get('season')
        type_ = request.form.get('type')
        brand = request.form.get('brand')
        occasion = request.form.get('occasion')

        if not name or not season or not type_ or not brand:
            flash("All fields except 'Occasion' are required!", "danger")
            return redirect(url_for('add_flavor_form'))

        # Check if a flavor with the same name already exists
        existing_flavor = Flavor.query.filter_by(name=name).first()
        if existing_flavor:
            flash("A flavor with this name already exists. Please choose a different name.", "danger")
            return redirect(url_for('add_flavor_form'))

        new_flavor = Flavor(name=name, season=season, type=type_, brand=brand, occasion=occasion)
        try:
            db.session.add(new_flavor)
            db.session.commit()
            flash("Flavor added successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('get_flavors'))
    return render_template('add_flavor.html')

@app.route('/get_ingredients', methods=['GET'])
def get_ingredients():
    """Route to retrieve and display all ingredients."""
    ingredients = Ingredient.query.all()
    return render_template('ingredients.html', ingredients=ingredients)

@app.route('/add_ingredient_form', methods=['GET', 'POST'])
def add_ingredient_form():
    """Form to add a new ingredient."""
    if request.method == 'POST':
        name = request.form.get('name')
        quantity = request.form.get('quantity')

        if not name or not quantity or int(quantity) < 0:
            flash("Valid name and non-negative quantity are required!", "danger")
            return redirect(url_for('add_ingredient_form'))

        new_ingredient = Ingredient(name=name, quantity=int(quantity))
        try:
            db.session.add(new_ingredient)
            db.session.commit()
            flash("Ingredient added successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('get_ingredients'))
    return render_template('add_ingredient.html')

@app.route('/get_suggestions', methods=['GET'])
def get_suggestions():
    """Route to retrieve and display all customer flavor suggestions."""
    suggestions = Suggestion.query.all()
    return render_template('suggestions.html', suggestions=suggestions)

@app.route('/add_suggestion_form', methods=['GET', 'POST'])
def add_suggestion_form():
    """Form to add a new customer flavor suggestion."""
    if request.method == 'POST':
        flavor = request.form.get('flavor')
        allergy_info = request.form.get('allergy_info')

        if not flavor:
            flash("Flavor is required!", "danger")
            return redirect(url_for('add_suggestion_form'))

        new_suggestion = Suggestion(flavor=flavor, allergy_info=allergy_info)
        db.session.add(new_suggestion)
        db.session.commit()
        flash("Suggestion added successfully!", "success")
        return redirect(url_for('get_suggestions'))
    return render_template('add_suggestion.html')

@app.route('/recommend_chocolates', methods=['GET', 'POST'])
def recommend_chocolates():
    """Allow users to select a season and display recommended chocolates."""
    if request.method == 'POST':
        selected_season = request.form.get('season')
        recommended_flavors = Flavor.query.filter_by(season=selected_season).all()

        if not recommended_flavors:
            flash("No flavors found for the selected season!", "info")

        return render_template('recommendations.html', season=selected_season, recommended_flavors=recommended_flavors)
    return render_template('choose_season.html')

if __name__ == '__main__':
    app.run(debug=True)
