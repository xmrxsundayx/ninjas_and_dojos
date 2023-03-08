from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas import Ninjas

class Dojos:
    DB = "ninjas_dojos"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data):
        query= """
                    INSERT INTO 
                    dojos (name) 
                    VALUES (%(name)s)
                    ;"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

    @classmethod
    def get_all_dojos(cls):
        query ="""
                    SELECT * FROM 
                    dojos;
                    """
        results = connectToMySQL(cls.DB).query_db(query)
        all_dojos =[]
        for row in results:
            #make an object
            all_dojos.append(cls(row))
            #add to list
        return all_dojos


    @classmethod
    def ninja_with_dojo(cls, data ):
        query = """
        SELECT * FROM 
        dojos 
        LEFT JOIN 
        ninjas 
        ON dojos.id = ninjas.dojo_id WHERE 
        dojos.id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            ninja_info = {
                'id': row['id'],
                'dojo_id': row['dojo_id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            dojo.ninjas.append(Ninjas(ninja_info))
        return dojo