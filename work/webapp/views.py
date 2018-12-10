from django.shortcuts import render

def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})
    elif request.method == 'POST':
        act = request.POST.get('action')
        a = int(request.POST.get('first_num'))
        b = int(request.POST.get('second_num'))
        result = None
        if act == 'add':
            result = a + b
            act = '+'
        elif act == 'sub':
            result = a - b
            act = '-'
        elif act == 'mul':
            result = a * b
            act = '*'
        elif act == 'div':
            result = a / b
            act = '/'
        return render(request, 'result.html', {'first_num': a, 'second_num': b, 'act': act, 'result': result})






