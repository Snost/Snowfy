from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, UserFavorite
from django.contrib.auth.decorators import login_required


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'albums/album_detail.html', {'album': album})

@login_required
def add_to_favorites(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    UserFavorite.objects.get_or_create(user=request.user, album=album)
    return redirect('album_list')

@login_required
def my_music(request):
    favorites = UserFavorite.objects.filter(user=request.user)
    return render(request, 'albums/my_music.html', {'favorites': favorites})


@login_required
def album_list(request):
    albums = Album.objects.all()
    favorite_album_ids = UserFavorite.objects.filter(user=request.user).values_list('album_id', flat=True)
    return render(request, 'albums/album_list.html', {
        'albums': albums,
        'favorite_album_ids': set(favorite_album_ids)  
    })



@login_required
def remove_from_favorites(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    UserFavorite.objects.filter(user=request.user, album=album).delete()
    return redirect('album_list') 