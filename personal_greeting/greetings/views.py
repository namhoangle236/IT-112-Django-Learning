from django.shortcuts import render

# Create your views here.
def greeting_view(request):
    user_name = request.GET.get('user_name', None)
    context = {'user_name': user_name,}
    return render(request, 'greeting.html', context)