"""BlogRealTimeProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from BlogApp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add/', views.Postview),

    path('<tag_slug>/comment', views.post_list_view, name='post_list_by_tag_name'),

    path('<year>/<month>\<day>\<post>', views.post_detail_view, name='post_detail'),

    path("<id>/share/", views.mail_send_view),
    path('signup/', views.signup_view),
    path('logout/', views.logout_view),
    path('delete/<pk>', views.PostDeleteView.as_view(), name='delete'),
    path('succ/,', views.Postsuccview, name='succ'),
    path('^mail/', views.mail_send_view),
    # path("bssample/",views.bs_smaple_view),

    # use-in-lasts
    re_path('^.*$', views.post_list_view),

]
