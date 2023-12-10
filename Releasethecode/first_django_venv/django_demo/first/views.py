from django.shortcuts import render
import datetime


def index_page(request):
    context = {
        'date': datetime.date.today(),
    }
    return render(request, 'index.html', context)


def riddle_page(request):
    context = {
    }
    return render(request, 'riddle.html', context)


def answer_page(request):
    context = {
    }
    return render(request, 'answer.html', context)


def multiply_page(request):
    a = request.GET.get('value', 'Значение для умножения не задано')
    if a == 'Значение для умножения не задано':
        context = {
            'b': a
        }
    else:
        a1 = '1 * ' + a + ' = ' + str(int(a) * 1)
        a2 = '2 * ' + a + ' = ' + str(int(a) * 2)
        a3 = '3 * ' + a + ' = ' + str(int(a) * 3)
        a4 = '4 * ' + a + ' = ' + str(int(a) * 4)
        a5 = '5 * ' + a + ' = ' + str(int(a) * 5)
        a6 = '6 * ' + a + ' = ' + str(int(a) * 6)
        a7 = '7 * ' + a + ' = ' + str(int(a) * 7)
        a8 = '8 * ' + a + ' = ' + str(int(a) * 8)
        a9 = '9 * ' + a + ' = ' + str(int(a) * 9)
        a10 = '10 * ' + a + ' = ' + str(int(a) * 10)
        context = {
            'a': a,
            'a1': a1,
            'a2': a2,
            'a3': a3,
            'a4': a4,
            'a5': a5,
            'a6': a6,
            'a7': a7,
            'a8': a8,
            'a9': a9,
            'a10': a10,

        }
    return render(request, 'multiply.html', context)