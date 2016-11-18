from django.shortcuts import render_to_response
from django.views.generic import TemplateView

from .models import Table1

# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		query_results = Table1.objects.all()
		print query_results
		return render_to_response('index.html', context=query_results)

class AboutPageView(TemplateView):
	template_name = "about.html"