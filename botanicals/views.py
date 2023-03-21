from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_data__lte=timezone.now()).order_by('published_data')
	return render(request, 'botanicals/post_list.html', {'posts':posts})