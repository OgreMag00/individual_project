from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
from .models import Tests

context = [[{"q_num": '1',
                "q_title": "Что из этого конъюнкция? (Python)", 
                "a1": "==",
                "a2": "!=",
                "a3": "and",
                "a4": "or",
                "answer": "answer3"},
                {"q_num": '2',
                "q_title": "Что из этого дизъюнкция? (Python)", 
                "a1": "maybe",
                "a2": ">=",
                "a3": "and",
                "a4": "or",
                "answer": "answer4"},
                {"q_num": '3',
                "q_title": "Какая функция является инверсией? (Python)", 
                "a1": "not()",
                "a2": "inverse()",
                "a3": "no()",
                "a4": "ne()",
                "answer": "answer1"},
                {"q_num": '4',
                "q_title": "Что является импликацией? (Python)", 
                "a1": "imp()",
                "a2": "<=>",
                "a3": "<=",
                "a4": ">=",
                "answer": "answer3"},
                {"q_num": '5',
                "q_title": "Что является тождеством? (Python)", 
                "a1": "?=",
                "a2": "===",
                "a3": "!=",
                "a4": "==",
                "answer": "answer4"},],[],
                [{"q_num": '1',
                "q_title": "Что из этого конъюнкция? (excel)", 
                "a1": "=И()",
                "a2": "=КОНЬЮН()",
                "a3": "=ИЛИ()",
                "a4": "=ИСКЛИ()",
                "answer": "answer1"},
                {"q_num": '2',
                "q_title": "Что из этого дизъюнкция? (excel)", 
                "a1": "=И()",
                "a2": "=ИЛИ()",
                "a3": "=ВОЗМОЖНО()",
                "a4": "=ДИЗ()",
                "answer": "answer2"},
                {"q_num": '3',
                "q_title": "Какая функция является инверсией? (excel)", 
                "a1": "=Инверсия()",
                "a2": "=НЕТ()",
                "a3": "=НЕ()",
                "a4": "=Нул()",
                "answer": "answer3"},
                {"q_num": '4',
                "q_title": "Какой функцией можно проверить наличие в ячейке значения?", 
                "a1": "=imp()",
                "a2": "=НУЛЕВОЕ",
                "a3": "=ЕПУСТО()",
                "a4": "=Пусто()",
                "answer": "answer3"},
                {"q_num": '5',
                "q_title": "Что является тождеством? (excel)", 
                "a1": "?=",
                "a2": "===",
                "a3": "==",
                "a4": "=",
                "answer": "answer4"}],]
def index(request):
    return render(request, 'tests_app/index.html')


def test(request, test_num):
    
    if request.method != 'POST':
        if test_num <= len(context) and test_num > 0:
            if test_num == 2:
                return render(request, 'tests_app/test/test2.html')
            else:
                return render(request, f'tests_app/test/test.html', {'test':context[test_num-1], 'test_num': test_num})
        else:
            raise Http404()

    else:
        
        otveti = request.POST
        result = {'correct': 0, 'count': len(context[test_num-1])}
        for i in range(1, len(context[test_num-1])+1):
            
            if otveti.get(str(i)) == context[test_num-1][i - 1]['answer']:
                result['correct'] += 1
        correct = result['correct']      
        count = result['count'] 
        if request.user.is_authenticated:
            Tests.objects.create(user=request.user.username, test=test_num, result=f'{correct}/{count}')
            
        return render(request, f'tests_app/test/result.html', result)


