from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm

def post_list(request):
	posts = Post.objects.filter(published_data__lte=timezone.now()).order_by('published_data')
	return render(request, 'botanicals/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'botanicals/post_detail.html', {'post':post})	

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_data = timezone.now()
			post.save()
		return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()		
	return render(request, 'botanicals/post_edit.html', {'form':form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_data = timezone.now()
			post.save()
		return redirect ('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'botanicals/post_edit.html', {'form':form})				