
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models.ninja import Ninja

DATABASE = 'dojos_and_ninjas_schema'

#  make sure your fucking names match the database

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

#  method for my read 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( Dojo(dojo) )
        return dojos
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        dojo = result[0]
        return Dojo(dojo)
    
    @classmethod
    def get_one_with_ninjas(cls,data):
        # Select all from dojos Leftjoin ninjas on dojos.id = ninjas.dojos_id  
        query = "SELECT * FROM dojos Left join ninjas on dojos.id = ninjas.dojo_id where dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])
        for result in results:
            ninja_dict = {
           "id" : result['id'],
           "first_name" : result['first_name'],
           "last_name" : result['last_name'],
           "age" : result['age'],
           "dojo_id" : result['dojo_id'],
           "created_at" : result['created_at'],
           "updated_at" : result['updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_dict))
        print(results)
        return dojo
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET first_name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

