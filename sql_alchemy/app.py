from flask import Flask, request, render_template, redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from form import AddPetForm, EditPetForm
from models import db, connect_db, Pet


app = Flask(__name__)

app.config['SECRET_KEY'] = 'whomadethispotatosalad'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """Show home page with pets."""
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Add a pet to the list."""
    form = AddPetForm()

    if form.validate_on_submit():
      ###  name = form.name.data
      ###  species = form.species.data
      ###  photo_url = form.photo_url.data
      ###  age = form.age.data
      ###  notes = form.notes.data
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{pet.name} added!")
        return redirect(url_for('home_page'))

    else:
        return render_template("add_pet.html", form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit a pet on the list."""
    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(edit=pet)
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated!")
        return redirect(url_for('home_page'))

    else:
        return render_template("edit_pet.html", form=form, pet=pet)
