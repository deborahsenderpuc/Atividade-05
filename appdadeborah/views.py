from django.shortcuts import render
from .models import Musicas, Albums
from django.shortcuts import redirect

# Create your views here.
def home(request):
  musicas = Musicas.objects.all()
  albums = Albums.objects.all()
  
  return render(request, "home.html", context={
    "mscs": musicas,
    "albms": albums
  })
  
def create_songs(request):
  if request.method == "POST":
    #criar uma nova musica usando valores do form
    Musicas.objects.create(
      title = request.POST['title'],
      album = request.POST['album'],
      artista = request.POST['artista'],
      release = request.POST['release']
    )

    return redirect("home")
  return render(request, "forms.html", context={"action":"Adicionar"})

def update_songs(request, id):
  song = Musicas.objects.get(id = id)
  if request.method == "POST":
    #atualizar uma musica usando valores do form
    song.title = request.POST['title']
    song.album = request.POST['album']
    song.artista = request.POST['artista']
    song.release = request.POST['release']
    song.save()

    return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar", "song": song})

def delete_songs(request, id):
  song = Musicas.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      song.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context={"action": "Remover", "song": song})

def create_albums(request):
  if request.method == "POST":
    #criar um novo album usando valores do form
    Albums.objects.create(
      title = request.POST['title'],
      year = request.POST['year'],
      musician = request.POST['musician'],
      tipo = request.POST['tipo']
    )

    return redirect("home")
  return render(request, "fAlbums.html", {"action": "Adicionar"})

def update_albums(request, id):
  album = Albums.objects.get(id = id)
  if request.method == "POST":
    #atualizar um album usando valores do form
    album.title = request.POST['title']
    album.year = request.POST['year']
    album.musician = request.POST['musician']
    album.tipo = request.POST['tipo']
    album.save()

    return redirect("home")
  return render(request, "fAlbums.html", context={"action": "Atualizar", "album": album})

def delete_albums(request, id):
  album = Albums.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      album.delete()

    return redirect("home")
  return render(request, "are_you_album.html", context={"action": "Remover", "album": album})