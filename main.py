from flask import Flask, render_template, request

app = Flask(__name__)

# Film kataloğu
films = [
    {"TITLE": "The Shawshank Redemption", "DIRECTOR": "Frank Darabont"},
    {"TITLE": "The Godfather", "DIRECTOR": "Francis Ford Coppola"},
    {"TITLE": "The Dark Knight", "DIRECTOR": "Christopher Nolan"},
    {"TITLE": "Forrest Gump", "DIRECTOR": "Robert Zemeckis"},
    {"TITLE": "Inception", "DIRECTOR": "Christopher Nolan"},
    {"TITLE": "Fight Club", "DIRECTOR": "David Fincher"},
    {"TITLE": "Pulp Fiction", "DIRECTOR": "Quentin Tarantino"},
    {"TITLE": "The Lord of the Rings: The Return of the King", "DIRECTOR": "Peter Jackson"},
    {"TITLE": "The Matrix", "DIRECTOR": "Lana Wachowski, Lilly Wachowski"},
    {"TITLE": "The Empire Strikes Back", "DIRECTOR": "Irvin Kershner"},
    {"TITLE": "Interstellar", "DIRECTOR": "Christopher Nolan"},
    {"TITLE": "The Social Network", "DIRECTOR": "David Fincher"},
    {"TITLE": "Goodfellas", "DIRECTOR": "Martin Scorsese"},
    {"TITLE": "The Silence of the Lambs", "DIRECTOR": "Jonathan Demme"},
    {"TITLE": "City of God", "DIRECTOR": "Fernando Meirelles, Kátia Lund"},
    {"TITLE": "Se7en", "DIRECTOR": "David Fincher"},
    {"TITLE": "The Usual Suspects", "DIRECTOR": "Bryan Singer"},
    {"TITLE": "Gladiator", "DIRECTOR": "Ridley Scott"},
    {"TITLE": "The Prestige", "DIRECTOR": "Christopher Nolan"},
    {"TITLE": "Schindler's List", "DIRECTOR": "Steven Spielberg"},
    {"TITLE": "The Green Mile", "DIRECTOR": "Frank Darabont"},
    {"TITLE": "Titanic", "DIRECTOR": "James Cameron"},
    {"TITLE": "The Lion King", "DIRECTOR": "Roger Allers, Rob Minkoff"}
]

@app.route('/katalog')
def katalog():
    search_query = request.args.get('q', '')  # Arama kutusundan gelen değer
    filtered_films = []  # Boş liste ile başla
    
    if search_query:  # Kullanıcı arama yapmışsa filtrele
        filtered_films = [
            film for film in films 
            if search_query.lower() in film["TITLE"].lower()  # Başlıkta arama yap
            or search_query.lower() in film["DIRECTOR"].lower()  # Yönetmen adında arama yap
        ]
    
    return render_template('katalog.html', data=filtered_films, query=search_query)

if __name__ == '__main__':
    app.run(debug=True)
