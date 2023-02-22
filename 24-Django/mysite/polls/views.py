from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.urls import reverse

#importar el modelo
from .models import Choice, Question

# Create your views here.
# def index(request):
#     last_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'last_question_list': last_question_list,
#     }
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         select_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice"
#         })
#     else:
#         select_choice.votes +=1
#         select_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

from django.views import generic

from django.utils import timezone
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

    #parte organziada mas detallada
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.