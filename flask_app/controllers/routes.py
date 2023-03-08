from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojos import Dojos
from flask_app.models.ninjas import Ninjas


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/view/<int:id>')
def view_dojo(id):
    city_name = {
        "id": id
    }
    return render_template("view.html", dojo = Dojos.ninja_with_dojo(city_name))

@app.route('/dojos')
def all_dojos():
    all_dojos = Dojos.get_all_dojos()
    return render_template("dojos.html",all_dojos=all_dojos)
    

@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    dojo_data = {
    'name': request.form['name'],
    }
    Dojos.save(dojo_data)
    return redirect('/dojos')

# ******NINJA & DOJO********

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojos.html', dojos=Dojos.ninja_with_dojo(data))



    # *****NINJAS******

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html',all_dojos=Dojos.get_all_dojos())

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    Ninjas.save(request.form)
    return redirect('/')