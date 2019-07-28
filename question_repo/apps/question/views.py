from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'question/index.html')

def questions(request):
    return render(request, 'question/questions.html')

def detail(request):
    return render(request, 'question/question_detail.html')