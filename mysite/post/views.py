from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
# post list 페이지
class PostList(ListView):
  model = Post
  template_name = 'post/post_list.html'
  ordering = '-pk'

# post detail page
# pk를 매개변수로 받아온다.
def post_detail(request, pk):
  post = Post.objects.get(pk=pk)
  
  return render(
    request,
    'post/post_detail.html',
    {
      'post': post,
    }
  )