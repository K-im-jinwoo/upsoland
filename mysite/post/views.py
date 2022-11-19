from django.shortcuts import render
from .models import Post

# Create your views here.
# post list 페이지
def post_list(request):
  posts = Post.objects.all().order_by('-pk')

  return render(
        request,
        'post/post_list.html',
        {
          'posts': posts,
        }
    )

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