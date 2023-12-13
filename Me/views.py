from django.shortcuts import render
from .form import CommentForm

# Create your views here.

def frontpage(request):
    return render(request, 'core/homepage.html', {})

def contact_view(request):
    message_sent = False

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #print(form)
            form.save()
            message_sent = True
    else:
        form = CommentForm()
    
    context = {'form': form, 'message_sent': message_sent}
    return render(request, 'core/homepage.html', context)