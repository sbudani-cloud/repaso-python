def hacer_album(artista, titulo):
    album = {
        "Artista" : artista,
        "Título" : titulo
    }
    print(f"Título: {album["Título"]}\nArtista: {album["Artista"]}\n")

titulito = input("Ingrese título del album: ")
artistita = input("Ingrese artista del album: ")
hacer_album(artistita, titulito)