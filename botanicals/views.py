from django.shortcuts import render

def post_list(request):
	return render(request, 'botanicals/post_list.html', {})
