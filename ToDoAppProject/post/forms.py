from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
        ]