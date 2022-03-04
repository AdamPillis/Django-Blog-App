from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """X"""
    class Meta:
        """X"""
        model = Comment
        fields = ('body',)
