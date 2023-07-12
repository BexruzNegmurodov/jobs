from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'image', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Image'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Write Comment'
        })

