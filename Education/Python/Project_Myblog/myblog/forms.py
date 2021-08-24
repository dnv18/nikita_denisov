from django import forms
from .models import Post, User, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'text', 'image',)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)
        help_texts = {
            'username': None,
            'email': None,
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
