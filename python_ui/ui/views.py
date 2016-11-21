from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Table1

# Create your views here.
class HomePageView(TemplateView):
	
	def get(self, request, **kwargs):
		query_results = Table1.objects.all()
		paginator = Paginator(query_results, 10)

		page = request.GET.get('page')
		try: 
			query_results = paginator.page(page)
		except PageNotAnInteger:
			query_results = paginator.page(1)
		except EmptyPage: 
			query_results = paginator.page(paginator.num_pages)

		return render_to_response('index.html', locals())

class AboutPageView(TemplateView):
	template_name = "about.html"