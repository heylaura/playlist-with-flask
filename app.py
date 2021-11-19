from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

URL = "https://5000-lavender-crocodile-t24jf8jj.ws-us18.gitpod.io/"


@app.route('/login')
def home():
    return render_template('login.html')


lista_musicas = [
    {"musica": "Wish you were here", "artista": "Pink Floyd", "genero": "Rock"},
    {"musica": "Feel Good Inc.", "artista": "Gorillaz", "genero": "Rap"},
    {"musica": "Born to die", "artista": "Lana Del Rey", "genero": "Indie"},
    {"musica": "Como os nossos pais", "artista": "Elis Regina", "genero": "MPB"},
    {"musica": "Rindo à toa", "artista": "Falamansa", "genero": "Forró"},
]


@app.route('/')
def index():
   return render_template('index.html', lista=lista_musicas)


@app.route('/results', methods=["POST"])
def results():
    item = request.form["pesquisar"]

    for item in lista_musicas:
        if item in lista_musicas:
            return {"musica": item, "artista": item, "genero": item}
            
        else:
            return render_template('notfound.html')
    
    return render_template(URL)
        



@app.route('/create')
def create():
    return render_template('create.html')



@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    new_music = request.form['music']   # <input name="new_music"/>
    new_artist = request.form['artist']       # <input name="new_artist"/>
    id_gender = request.form['gender']       # <input name="new_gender"/>
    new_add = { "musica": new_music, "artista": new_artist, "genero": id_gender}
    lista_musicas.append(new_add)
    
    return redirect(URL)



@app.route('/delete')
def delete():
    return render_template('delete.html')
   


@app.route('/remove', methods=['POST'])  # <form action="/save" method="POST">
def remove():
    new_music = request.form['music']   # <input name="new_music"/>
    new_artist = request.form['artist']       # <input name="new_artist"/>
    id_gender = request.form['gender']       # <input name="new_gender"/>
    new_del = { "musica": new_music, "artista": new_artist, "genero": id_gender}
    lista_musicas.remove(new_del) #deleta o dicionário que o usuário escolher
    #tentar implementar a exclusão da lista toda de uma vez       
    return redirect(URL)



@app.route('/search')
def pesquisar():
    return render_template('search.html', lista=lista_musicas)






app.run(debug=True)

# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)