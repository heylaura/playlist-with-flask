from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

URL = "http://127.0.0.1:5000/"


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
   


#página que irá receber os valores que o usuário deseja inserir na lista
@app.route('/create')
def create():
    return render_template('create.html')


#redireciona os campos preenchidos do formulário
@app.route('/save', methods=['POST'])  #recebe parâmetros para a inserção de novos valores na lista
def save():
    #lista para armazenar eventuais músicas repetidas
    lista_repetidos = [] 
    
    new_music = request.form['music']   # <input name="new_music"/>
    new_artist = request.form['artist']       # <input name="new_artist"/>
    id_gender = request.form['gender']       # <input name="new_gender"/>
    new_add = { "musica": new_music, "artista": new_artist, "genero": id_gender}
       
    
    #redirecionar para a página de erro
    #if len(new_music) == 0 or new_music >= '':
        #return render_template('notfound.html')


    #evita que o usuário adicione músicas repetidas
    #exceto se os valores contidos nas chaves "artista" e "genero" forem distintas (funcionalidade ainda não implementada)
    for parametro in lista_musicas:
        if new_music.lower() in parametro["musica"].lower():
            lista_repetidos.append(parametro)

    #se não houver parâmetro repetido o novo dicionário é adicionado à lista
    if len(lista_repetidos) == 0:
        lista_musicas.append(new_add)
        
    #se o valor constante na chave música já pertencer à lista não será possível adicioná-lo
    else:  
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

    
    #redireciona para a página de erro se o usuário clica no ícone de pesquisa e não informa valor ou apenas pressiona espaço(s) na barra de pesquisa
    if len(item) == 0 or item >= '':
        return render_template('notfound.html')
           
    #habilita a pesquisa por chave nos dicionários presentes na lista de músicas
    for objeto in lista_musicas:
            
        if item.lower() in objeto["musica"].lower():
            lista_busca.append(objeto)

        if item.lower() in objeto["artista"].lower():
            lista_busca.append(objeto)

        if item.lower() in objeto["genero"].lower():
            lista_busca.append(objeto)

     
    #se a lista de busca não contiver elementos o usuário será redirecionado à página de erro
    if len(lista_busca) == 0:
        return render_template('notfound.html')

    #retorna os parâmetros de pesquisa informados com base nos elementos da lista de busca
    return render_template('search.html', lista_busca=lista_busca)  

  

app.run(debug=True)

