from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.dojo import Dojo

# I want to be able to create a new dojo and have it redirect back on my main homepage 

# I need two app routes for cretaing one that displays and one that handles the data 

# # ! This route displays the form on my new_dojo page

@app.route('/dojo/new')
def new_dojo():
    return render_template('new_dojo.html')

# ! This one handles the data from the form
# POST needs a redirect 
# Were redirecting back to my main homepage

@app.route('/dojo/create', methods=['POST'])
def create_user():
    Dojo.save(request.form)
    return redirect('/dojos')

# # ! ////////  READ or RETRIEVE  //////////
@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos = dojos )

@app.route('/dojo/<int:id>')
def show(id):
    data = {'id': id}
    dojo = Dojo.get_one_with_ninjas(data)
    return render_template('showdojo.html', dojo = dojo)


# # ! //////// UPDATE  //////////
# # ! POST requires two routes

# # ! This one displays the form
# @app.route('/user/edit/<int:id>')
# def edit_user(id):
#     data ={'id': id}
#     return render_template('edit_user.html', user = User.get_one(data))

# # ! This one handles the data from the form
# @app.route('/user/update', methods=['POST'])
# def update_user():
#     User.update(request.form)
#     return redirect('/')

# # ! //// DELETE //////

# @app.route('/user/destroy/<int:id>')
# def destroy_user(id):
#     data = {'id': id}
#     User.destroy(data)
#     return redirect('/')