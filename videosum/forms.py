# forms.py

from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']

        widgets = {
            # 'title': forms.TextInput{attrs={'id': 'title_id', 'class': 'form-control'}},

        }