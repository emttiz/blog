from django.shortcuts import render
from posts.models import Post, Hashtag, Coments


# Create your views here.


def main(request):
    return render(request, 'layouts/main.html')


def posts_view(request, **kwargs):
    posts = Post.objects.all()
    data = {
        'posts': posts,
    }
    return render(request, 'posts/posts_list.html', context=data)


def hashtags_view(request):
    hashtag = Hashtag.objects.all()
    data = {
        'hashtags': hashtag
    }
    return render(request, 'hashtags/hashtags_list.html', context=data)


def comments_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        comments = Coments.objects.filter(post=post)

        data = {
            'post': post,
            'comments': comments
        }

        return render(request, 'posts/detail.html', context=data)

