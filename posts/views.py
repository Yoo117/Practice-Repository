from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from taggit.models import Tag
from .models import Post, Category
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 4

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_object(self):
        # 조회수 카운팅
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        # 조회수를 context에 추가
        context = super().get_context_data(**kwargs)
        context['views'] = self.object.views
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        # 저자를 현재 유저로 설정
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def test_func(self):
        post = self.get_object() # 요청한 유저가 작성자 본인인지 확인
        return self.request.user == post.author

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    def handle_no_permission(self):
        return redirect('post_detail', pk=self.get_object().pk)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object() # 요청한 유저가 작성자 본인인지 확인
        return self.request.user == post.author

    def handle_no_permission(self):
        return redirect('post_detail', pk=self.get_object().pk)

class CategoryPostsView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('slug')
        context['category'] = Category.objects.get(slug=category_slug) # context에 category 변수 추가
        context['categories'] = Category.objects.all()

        return context

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        return Post.objects.filter(category__slug=category_slug)

class TagPostsView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs.get('slug')
        context['tag'] = Tag.objects.get(slug=tag_slug) # context에 tag 변수 추가
        context['tags'] = Tag.objects.all()

        return context

    def get_queryset(self):
        tag_slug = self.kwargs.get('slug')
        return Post.objects.filter(tags__slug=tag_slug)

class SearchPostsView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')

        context['query'] = query # 검색을 사용자 쿼리로 입력받음
        context['tags'] = Tag.objects.all() # Tag 검색 변수 추가
        context['categories'] = Category.objects.all() # Category 검색 변수 추가
        
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query).order_by('-created_at')
        return Post.objects.none()  # 검색어가 없으면 빈 쿼리셋 반환
