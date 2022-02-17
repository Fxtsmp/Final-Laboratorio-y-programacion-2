# all this must be work with a db
from ..db import get_db
from flask import Blueprint, jsonify, request
from ..login.login import login_required

rest_api = Blueprint('rest_api', __name__,  url_prefix='/api')


@rest_api.route('/')
def get_data():
    return jsonify(
        {
            "get films": "../api/films",
            "get film": "../api//films/film_name",
            "get the list of all directors on the platform": "../api/directors",
            "get the list of all genders on the platform": "../api/genders",
            "get the list of all films of a director name in the platform": "../api/directors/director_name"

        }
    )

#get the last ten films added
@rest_api.route('/last_films_add')
def get_last_films():
    """ return jsonify({'films':films}) """
    db = get_db()
    films = db.execute(
        'SELECT * FROM films ORDER BY id DESC LIMIT 10'
    ).fetchall()
    films_json = []
    for film in films:
        films_json.append(
            {
                "id": film['id'],
                "title": film['title'],
                "year": film['year'],
                "director": film['director'],
                "gender": film['gender'],
                "sinopsis": film['sinopsis'],
                "cover": film['cover']
            }
        )
    return jsonify({
        "films": films_json
    })

#get all films
@rest_api.route('/films')
@login_required
def get_films():
    """ return jsonify({'films':films}) """
    db = get_db()
    films = db.execute(
        'SELECT * FROM films;'
    ).fetchall()
    films_json = []
    for film in films:
        films_json.append(
            {
                "id": film['id'],
                "title": film['title'],
                "year": film['year'],
                "director": film['director'],
                "gender": film['gender'],
                "sinopsis": film['sinopsis'],
                "cover": film['cover']
            }
        )
    return jsonify({
        "films": films_json
    })

# getting film data
# by deafut methods = ["GET"]
@rest_api.route('/films/<film_name>')
def get_film(film_name):
    db = get_db()
    film_name = "%"+film_name+"%"
    films = db.execute('SELECT * FROM films WHERE title LIKE ?;',
                       (film_name,)).fetchall()
    films_json = []
    for film in films:
        films_json.append(
            {
                "id": film['id'],
                "title": film['title'],
                "year": film['year'],
                "director": film['director'],
                "gender": film['gender'],
                "sinopsis": film['sinopsis'],
                "cover": film['cover']
            }
        )
    return jsonify({
        "films": films_json
    })


# REST Service -- > GET method
##############################

# get the list of all directors on the platform
@rest_api.route('/directors')
def get_directors():
    db = get_db()
    directors = db.execute('SELECT director FROM films;').fetchall()
    director_json = []
    directors = list(set(directors))
    for director in directors:
        director_json.append(director['director'])
    return jsonify({
        "Directors": director_json
    })
# get the list of all genders on the platform
# improve using a set to filter duplicate elements
@rest_api.route('/genders')
def get_genders():
    db = get_db()
    genders = db.execute('SELECT gender FROM films;').fetchall()
    genders = list(set(genders))
    genders_json = []
    for film in genders:
        genders_json.append(film['gender'])
    return jsonify({
        "Genders": genders_json
    })

# get the list of all films of a director name in the platform
@rest_api.route('/directors/<director_name>')
def get_films_director_name(director_name):
    db = get_db()
    films_of = db.execute('''SELECT id, title, year, gender, sinopsis, cover FROM films
                            WHERE director = ?''', (director_name,)
                          ).fetchall()
    films_of_json = []
    for film in films_of:
        films_of_json.append(
            {
                "id": film['id'],
                "title": film['title'],
                "year": film['year'],
                "gender": film['gender'],
                "sinopsis": film['sinopsis'],
                "cover": film['cover']
            }
        )
    return jsonify({
        f"{director_name}": films_of_json
    })
# list of films with image available in the platform
@rest_api.route('/covers')
def get_films_with_cover():
    db = get_db()
    films_of = db.execute('''SELECT * FROM films WHERE cover != "";'''
                          ).fetchall()
    films_with_covers = []
    for film in films_of:
        films_with_covers.append(
            {
                "id": film['id'],
                "title": film['title'],
                "year": film['year'],
                "director": film['director'],
                "gender": film['gender'],
                "sinopsis": film['sinopsis'],
                "cover": film['cover']
            }
        )
    return jsonify({
        "films with covers": films_with_covers
    })

# ABM - need login 
# adding data
# i can  take this with get method but not is recommendanble
@login_required # <---------------
@rest_api.route('/films/nfilm', methods=['POST'])
def add_film():
    new_film = {
        "title": request.json["title"],
        "year": request.json["year"],
        "director": request.json["director"],
        "gender": request.json["gender"],
        "sinopsis": request.json["sinopsis"],
        "cover": request.json["cover"]
    }
    db = get_db()
    db.execute('''INSERT INTO films (title, year, director, gender, sinopsis, cover)
                            VALUES(?,?,?,?,?,?);''',
               (new_film["title"],
                new_film["year"],
                new_film["director"],
                new_film["gender"],
                new_film["sinopsis"],
                new_film["cover"],)
               )
    db.commit()
    return jsonify(
        {
            "messaje": "added succecfully",
            "film": new_film
        }
    )

# updated data
# always the front autocomplete all field
# and thhe user modified the necesary field
@login_required
@rest_api.route('/films/<film_title>', methods=['PUT'])
def edit_film(film_title):
    db = get_db()
    if db.execute('''SELECT * FROM films WHERE title = ? ''', (film_title,)).fetchall():
        film_founded = db.execute('''
                                UPDATE films
                                SET title = ?,
                                    year = ?, 
                                    director = ?, 
                                    gender = ?, 
                                    sinopsis = ?, 
                                    cover = ?
                                WHERE title = ?;
                                ''',
                                  (request.json["title"],
                                   request.json["year"],
                                   request.json["director"],
                                   request.json["gender"],
                                   request.json["sinopsis"],
                                   request.json["cover"],
                                   film_title,)
                                  )
        db.commit()
        return jsonify(
            {
                "film": "updated",
            }
        )
    return jsonify(
        {
            "film": "No founded"
        }
    )

# Delete a film
# next step
# list all films with x name and select the correct
# because the film name can be duplicate and be diferents
# films
@login_required
@rest_api.route('/films/<film_title>', methods=['DELETE'])
def delete_film(film_title):
    db = get_db()
    if db.execute('''SELECT * FROM films WHERE title = ? ''', (film_title,)).fetchall():
        film_founded = db.execute('''
                                DELETE FROM films
                                WHERE title = ?;
                                ''',
                                  (film_title,)
                                  )
        db.commit()
        return jsonify(
            {
                "film": "deleted",
            }
        )
    return jsonify(
        {
            "film": "No founded"
        }
    )
