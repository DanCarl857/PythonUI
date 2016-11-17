from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Table1

# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		# query_results = Table1.objects.all()
		# print query_results
		return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
	template_name = "about.html"