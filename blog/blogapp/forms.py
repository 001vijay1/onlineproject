from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','message')

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-4',
                'placeholder': 'Name',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-4',
                'placeholder': 'Email',
            }
        )
    )
    message = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Message',
            }
        )
    )
