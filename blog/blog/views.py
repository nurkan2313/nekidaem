from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.urls import reverse
from django.shortcuts import redirect
from blog.models import Post, Blog
from .forms import PostForm


class IndexView(ListView):
    model = Post
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_posts'] = self.get_queryset()
        # context['subs'] = self.get_users()
        context['all_users'] = self.get_all()
        return context

    def get_queryset(self):
        subscribers = Blog.objects.get(author=self.request.user).subscriber.all()
        s = []
        for i in subscribers:
            posts = Post.objects.filter(blog__author=i)
            for j in posts:
                s.append(j)
        return s

    def get_all(self):
        blog = Blog.objects.all()
        return blog


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = 'post_list.html'

    def get_queryset(self):
        user = self.request.user
        s = self.model.objects.filter(blog__author=user).order_by('-created_date')
        return s


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"



class PostCreateView(FormView):
    form_class = PostForm
    template_name = 'post_edit.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        user = self.request.user
        blog = Blog.objects.get(author=user)
        obj.blog = blog
        obj.save()
        return HttpResponseRedirect(reverse('post_list'))


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text', 'created_date']
    template_name = 'post_edit.html'


def add_subscribers(request):
    name = request.POST.get('action')
    if request.POST:
        user_blog = request.user.author
        user_blog.subscriber.add(name)
    return redirect(reverse('all_posts'))
