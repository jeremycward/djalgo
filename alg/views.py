from django.views import generic
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import  AlgoIndex
from django.http import  HttpResponse
from  alg.domain.monitor import Monitor
from django.views.generic.list import ListView
from neomodel.match import Traversal

def idx(request):
    # getting our template
    return render(request, 'alg/index.html', {})

def definitions(request):
    return render(request, 'alg/definitions/definition_home.html', {'indexes' :AlgoIndex.nodes.all()})


def monitor(request):
    # getting our template
    template = loader.get_template('alg/monitor/monitor_home.html')
    monitor = Monitor()

    context = {
          'monitor_report': monitor.report()
    }

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))




class AlgoIndexListView(ListView):
    model = AlgoIndex
    paginate_by = 10
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        if 'selected_idx' in self.request.resolver_match.kwargs:

            idx = self.request.resolver_match.kwargs['selected_idx']
            selected_algo_index = self.object_list[idx-1]
            context['selected_algo_index'] = selected_algo_index
            context['members'] = selected_algo_index.members.all()


        return context

    def get_template_names(self):
        return "alg/definitions/definition_home.html"


