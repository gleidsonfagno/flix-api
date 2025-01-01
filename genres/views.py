import json 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from genres.models import Genre

# Create your views here.
@csrf_exempt
def genre_create_list_view(request):
    # vai devolver os dados 
    if request.method == "GET":
        genres = Genre.objects.all()
        # data = [{"id": genre.id, "name": genre.name} for genre in genres]
        data = []
        for genre in  genres:
            data.append(
                {"id": genre.id, "name": genre.name}
            )
        return JsonResponse(data,safe=False)
    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        new_genere = Genre(name=data["name"])
        new_genere.save()
        return JsonResponse({"id": new_genere.id, "name": new_genere.name},status=201)

# funçao de busca por id  de cada genero
@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    #Genre.objects.get(pk=pk)

    if request.method == "GET":
        data = {"id":  genre.id, "name": genre.name}
        return JsonResponse(data)
    # atualiza
    elif request.method == "PUT":
        # rece o que o usuario ta mandando e transforma em json
        data = json.loads(request.body.decode("utf-8"))
        genre.name = data["name"]
        genre.save()
        return JsonResponse({"id": genre.id, "name": genre.name},status=201)

    elif request.method == "DELETE":
        genre.delete()
        return JsonResponse(
            {"message": "Gênero excluido com sucesso"}, status=204,
        )
