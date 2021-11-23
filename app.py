from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

URL = "https://5000-lavender-crocodile-t24jf8jj.ws-us18.gitpod.io/"


lista_musicas = [
    {"musica": "Wish you were here", "artista": "Pink Floyd", "genero": "Rock"},
    {"musica": "Feel Good Inc.", "artista": "Gorillaz", "genero": "Rap"},
    {"musica": "Born to die", "artista": "Lana Del Rey", "genero": "Indie"},
    {"musica": "Como os nossos pais", "artista": "Elis Regina", "genero": "MPB"},
    {"musica": "Rindo à toa", "artista": "Falamansa", "genero": "Forró"},
    {"musica": "Black", "artista": "Pearl Jam", "genero": "Rock"},
    {"musica": "Runaway", "artista": "Aurora", "genero": "Indie"},
    {"musica": "Save your tears", "artista": "The Weeknd", "genero": "Pop"},
    {"musica": "Sorri, Sou Rei", "artista": "Natiruts", "genero": "Reggae"},
    {"musica": "Don't let me down", "artista": "The Chainsmokers", "genero": "Eletrônica"},
    {"musica": "Bohemian Rhapsody", "artista": "Queen", "genero": "Rock"},
    {"musica": "Livin' on a Prayer", "artista": "Bon Jovi", "genero": "Rock"},
    {"musica": "Cheia de manias", "artista": "Raça Negra", "genero": "Samba"},
    {"musica": "Love in the dark", "artista": "Adele", "genero": "Pop"}
]


@app.route('/')
def index():
   return render_template('index.html', lista=lista_musicas)
   



@app.route('/create')
def create():
    return render_template('create.html')



@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    
    lista_repetidos = []
    
    new_music = request.form['music']   # <input name="new_music"/>
    new_artist = request.form['artist']       # <input name="new_artist"/>
    id_gender = request.form['gender']       # <input name="new_gender"/>
    new_add = { "musica": new_music, "artista": new_artist, "genero": id_gender}
    lista_musicas.append(new_add)
    
    
    for parametro in lista_musicas:
        if new_music.lower() in parametro["musica"].lower():
            lista_repetidos.append(parametro)


            if len(lista_repetidos) == 1:
                lista_musicas.remove(new_add)  
                return render_template('resultsfound.html', lista_repetidos=lista_repetidos)   
            
            
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
          
    return redirect(URL)



@app.route('/search', methods=["POST"])
def pesquisar():

    lista_busca = []
    item = request.form["pesquisar"]

    

    for objeto in lista_musicas:
            
        if item.lower() in objeto["musica"].lower():
            lista_busca.append(objeto)

        if item.lower() in objeto["artista"].lower():
            lista_busca.append(objeto)

        if item.lower() in objeto["genero"].lower():
            lista_busca.append(objeto)

     
    
    
    if len(lista_busca) == 0:
        return render_template('notfound.html')


    return render_template('search.html', lista_busca=lista_busca) 

  

app.run(debug=True)

