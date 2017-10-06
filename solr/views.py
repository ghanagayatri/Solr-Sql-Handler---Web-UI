import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import SqlForm
from solr_results import SolrQueryHandler

# # add to your views
# def solrquery(request):
#     form_class = SqlForm
    
#     return render(request, 'solrquery.html', {
#         'form': form_class,
#     })

def solrquery(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SqlForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            query = form.cleaned_data['query']
            model = SolrQueryHandler(query)
            results = model.getResults()
        
            # redirect to a new URL:
            return render(request, 'solrquery.html', {'form': form,'results':results})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SqlForm()

    return render(request, 'solrquery.html', {'form': form})

def index(request):
    return HttpResponse("Hello, world. You're at the solr index.")
