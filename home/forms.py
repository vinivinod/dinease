from django import forms
from .models import PredictedImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = PredictedImage
        fields = ['image']
