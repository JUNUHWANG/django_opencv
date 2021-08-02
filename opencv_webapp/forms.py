from django import forms
from .models import ImageUploadModel

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Model 클래스 이름 (@ models.py)
#         fields = ('Model 클래스의 변수명 1', 'Model 클래스의 변수명 2')

class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    # ImageField Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
    # file = forms.FileField()
    image = forms.ImageField()


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document',)
