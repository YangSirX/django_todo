from django.shortcuts import render
from django.http import HttpResponse
from .models import content
from django.template import loader
# Create your views here.
app_name = 'polls'
def index(request):
    #
    # content_list = content.objects.all()
    # print(content_list)
    # context = {
    #     'content_list': content_list
    # }
    # return render(request, 'polls/index.html', context)
    latest_question_list = content.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request,id):
    return HttpResponse("You're looking at question %s." % id)

