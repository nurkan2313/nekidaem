from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="all_posts"),
    url(r'^post/$', views.PostListView.as_view(), name="post_list"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name="post_detail"),
    url(r'^post/edit/(?P<pk>[0-9]+)/$', views.PostUpdateView.as_view(), name="post_edit"),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
    url(r'^post/add/$', views.add_subscribers, name='add'),

]
