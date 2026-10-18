from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'user' :'John Doe',
        'title' : 'Главная страница',
        'books' : ['Бесы', 'Идиот', 'Мастер и маргарита', ],
        'book_count' : 12,
    }
    return render(request, 'main_app/index.html', context)