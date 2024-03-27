from django.shortcuts import render

def movie_list(request):
    return render(request, 'movie_list.html')

def movie_details(request, movie_id):
    return render(request, 'movie_details.html', {'movie_id': movie_id})

def movie_add(request):
    return render(request, 'movie_add.html')

def movie_update(request, movie_id):
    return render(request, 'movie_update.html', {'movie_id': movie_id})

def movie_delete(request, movie_id):
    return render(request, 'movie_delete.html', {'movie_id': movie_id})
