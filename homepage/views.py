from django.shortcuts import render

def home(request):
    template_name = 'homepage/index.html'

    title = 'Привет'
    carrot = 'заяц!'

    context = {
        'title': title,    
        'carrot': carrot 
    }

    return render(request, template_name, context)