from django.shortcuts import render,get_object_or_404
from BlogApp1.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all();
    return render(request,'BlogApp1/post_list.html',{"post_list":post_list})


def post_detail_view(request, year,month,day,post):
    post=get_object_or_404(Post,slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day);
    return render(request, "BlogApp1/post_detail.html",{'post':post})


#post-list-view with paginator-codes...
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from BlogApp1.models import Post
from taggit.models import Tag
# Create your views here.
def post_list_view(request,tag_slug=None):
    print("post_list_view with paginator")
    post_list=Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])


    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'BlogApp1/post_list.html',{"post_list":post_list,'tag':tag})



#Listview with pagination
from django.views.generic import ListView
class PostListView(ListView):
    model=Post
    paginate_by=1

#from django.core.mail import send_mail
#send_mail('Hello', 'V ery imp msg....','swamytirumani13@gmail.com',['sorraharikrishna55@gmail.com','b.jagadeesh311@gmail.com'])

from django.shortcuts import render
from django.contrib.auth.decorators import login_required




from BlogApp1.forms import SignUpForm
from django.http import HttpResponseRedirect
def signup_view(request):
    formobj=SignUpForm
    if request.method == 'POST':
        formobj = SignUpForm(request.POST)
        user = formobj.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/account/login')
    return render(request,'BlogApp1/signup.html',{'formobj':formobj})

#views for email
from django.core.mail import send_mail
from BlogApp1.forms import EmailSendForm
def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id, status='published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject='{}({}) recommends you to read "{}"'.format(cd['name'],cd['email'],	post.title)
            message="Read Post At: \n{}\n\n{} 'Comments:\n{}".format(post_url,cd['name'],cd['comments'])
            send_mail(subject, message, 'swamytirumani13@gmail.com', [cd['to']])
            sent=True;
    else:
	    form=EmailSendForm()
    return render(request,'BlogApp1/sharebymail.html', {'post':post,'form':form,'sent':sent})


#bootstarp-sample.html-view
def bs_smaple_view(request):
    return render(request,"BlogApp1/Sample.html")


# comment form-view
from BlogApp1.models import Comment
from BlogApp1.forms import CommentForm
from django.db.models import Count


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day);
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', 'publish')[:4]

    comments = post.comments.filter(active=True)
    csubmit = False
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            csubmit = True
    else:
        form = CommentForm()
    return render(request, 'BlogApp1/post_detail.html',{"post": post, 'form': form, 'comments': comments, 'csubmit': csubmit,'similar_posts':similar_posts})

from django.http import HttpResponseRedirect
from BlogApp1.forms import PostForm
from BlogApp1.models import Post
def Postview(request):
    form = PostForm()
    print('welcome')
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            print('hello')
            user = form.save(commit=True)
            return HttpResponseRedirect('/thanks/')
    return render(request,'BlogApp1/postmain.html',{'form':form})
#create your views here
def home_page_view(request):
    return render(request,'BlogApp1/home.html')

def logout_view(request):
    return render(request,'BlogApp1/logout.html')
def login_page_view(request):
    return render(request,'BlogApp1/login.html')

#Deleteview
#from django.core.urlresolvers import reverse_lazy
from django.views.generic import DeleteView
from django.urls import reverse_lazy
class PostDeleteView(DeleteView):
    model=Post
    success_url=reverse_lazy('succ')

def Postsuccview(request):
   return render(request,'BlogApp1/succ.html')




