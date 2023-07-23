from django import forms
from .models import Apply


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('job', 'candidate', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Cover letter'
        })
