from django import forms
from tinymce import TinyMCE
from .models import Post, Comment

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget = TinyMCEWidget(
            attrs = {'required':False, 'cols':30, 'rows':10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'description', 'content', 'thumbnail','category','featured')

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id' : "usercomment",
        'placeholder' : "Type your comment",
        'rows': '3'
    }))
    class Meta:
        model = Comment
        fields = ('content', )