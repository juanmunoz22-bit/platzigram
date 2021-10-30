"""Post forms"""

#Django
from django import forms

#Models
from posts.models import Post

class PostForm(forms.ModelForm):
    """Post form."""

    class Meta:
        """Meta class."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')
