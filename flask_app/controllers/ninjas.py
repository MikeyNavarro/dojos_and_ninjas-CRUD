from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.ninja import Ninja 
from flask_app.models.dojo import Dojo

# I want to be able to create a new ninja and have it redirect back on my main homepage 

# I need two app routes for cretaing one that displays and one that handles the data 

# # ! This route displays the form on my new_ninja page

@app.route('/ninja/new')
def new_ninja():
    return render_template('new_ninja.html', dojos = Dojo.get_all())

# ! This one handles the data from the form
# POST needs a redirect 
# Were redirecting back to my main homepage

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    # my route to show dojo is / dojo
    # i need my dojo id from my request form on my dojo route
    return redirect(f"/dojo/{request.form['dojo_id']}")

# # ! ////////  READ or RETRIEVE  //////////
@app.route('/ninjas')
def ninjas():
    ninjas = Ninja.get_all()
    return render_template('index.html', ninjas = ninjas )

@app.route('/ninja/<int:id>')
def show_ninja(id):
    data = {'id': id}
    ninjas = Ninja.get_one(data)
    return render_template('showninja.html', ninja = ninjas)


# ! //////// UPDATE  //////////
# ! POST requires two routes

# ! This one displays the form
@app.route('/ninja/edit/<int:id>')
def edit_ninja(id):
    data ={'id': id}
    return render_template('edit_ninja.html', ninja = Ninja.get_one(data))

# ! This one handles the data from the form
@app.route('/ninja/update', methods=['POST'])
def update_ninja():
    Ninja.update(request.form)
    return redirect('/')

# # ! //// DELETE //////

# @app.route('/ninja/destroy/<int:id>')
# def destroy_ninja(id):
#     data = {'id': id}
#     Ninja.destroy(data)
#     return redirect('/')