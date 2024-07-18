from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
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
                "answer": "answer4"}]]
def index(request):
    return render(request, 'tests_app/index.html')


def test(request, test_num):
    
    if request.method != 'POST':
        if test_num <= len(context):
            return render(request, f'tests_app/test/test.html', {'test':context[test_num-1], 'test_num': test_num})
        else:
            raise Http404('hello')

    else:
        
        otveti = request.POST
        result = {'correct': 0, 'count': len(context[test_num-1])}
        for i in range(1, len(context[test_num-1])+1):
            
            if otveti.get(str(i)) == context[test_num-1][i - 1]['answer']:
                result['correct'] += 1
        
        return render(request, f'tests_app/test/result.html', result)


