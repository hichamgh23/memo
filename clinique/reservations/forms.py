from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_url']
        widgets = {
            'title':     forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de la vidéo'}),
            'video_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }
