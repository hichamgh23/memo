from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Show, Artist
from .forms import VideoForm


def show_list(request):
    artists = Artist.objects.all()
    selected_artist_id = request.GET.get('artist')  # récupère ?artist=1 dans l'URL

    if selected_artist_id:
        shows = Show.objects.filter(artist_id=selected_artist_id)
    else:
        shows = Show.objects.all()

    return render(request, 'reservations/show_list.html', {
        'shows': shows,
        'artists': artists,
        'selected_artist_id': selected_artist_id,
    })


def show_detail(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    videos = show.videos.all()
    form = None

    # Le formulaire n'est visible que par l'administrateur
    if request.user.is_authenticated and request.user.is_staff:
        form = VideoForm()

    return render(request, 'reservations/show_detail.html', {
        'show': show,
        'videos': videos,
        'form': form,
    })


def add_video(request, show_id):
    # Seul l'admin peut ajouter une vidéo
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("Accès interdit : vous devez être administrateur.")

    show = get_object_or_404(Show, id=show_id)

    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)  # Ne pas sauvegarder tout de suite
            video.show = show               # Associer le spectacle manuellement
            video.save()
            return redirect('show_detail', show_id=show.id)

    return redirect('show_detail', show_id=show.id)


def videos_by_artist(request, artist_name):
    # Cherche l'artiste dont le nom correspond (insensible à la casse)
    artist = get_object_or_404(Artist, name__iexact=artist_name)
    # Récupère tous les spectacles de cet artiste avec leurs vidéos
    shows = artist.shows.prefetch_related('videos').all()

    return render(request, 'reservations/videos_by_artist.html', {
        'artist': artist,
        'shows': shows,
    })
