from django import forms
from django.contrib.auth.models import User
class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

#model-based-form for comments
from django import forms
from BlogApp1.models import Comment
class CommentForm(forms.ModelForm):
	class Meta:
 		model=Comment
 		fields=('name','email','body')


#model-based-form for comment
from django import forms
from BlogApp1.models import Post
class PostForm(forms.ModelForm):
    class Meta:
            model=Post
            fields=('title','slug','author','body','publish','status','tags')

# Create your forms here.

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name'];




