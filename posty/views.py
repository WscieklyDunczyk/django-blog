from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib import messages


def post_list(requset):
    # użycie customowego menadżera
    posts = Post.publiczne.all()
    # posts = Post.objects.filter(status='publiczny')
    return render(requset, 'post_list.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    context_object_name = 'posty'
    ordering = ['-data_dodania']
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post


class PostCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Post

    permission_required = 'posty.post_add'
    fields = ['tytul', 'tekst']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, 'Post dodany!')
        return super().form_valid(form)


class PostUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Post

    login_url = 'login'
    permission_required = 'posty.post_change'
    fields = ['tytul', 'tekst']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, 'Post zaktualizowany!')
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False


class PostDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Post
    login_url = 'login'
    permission_required = 'posty.post_delete'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False
