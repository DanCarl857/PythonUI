from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Table1

# Create your views here.
class HomePageView(TemplateView):
	
	def get(self, request, **kwargs):
		query_results = Table1.objects.all()
		data = Table1._meta.get_fields()

		fields = []
		for dat in data:
			fields.append(dat.name)

		paginator = Paginator(query_results, 10)

		page = request.GET.get('page')
		try: 
			query_results = paginator.page(page)
		except PageNotAnInteger:
			query_results = paginator.page(1)
		except EmptyPage: 
			query_results = paginator.page(paginator.num_pages)

		return render_to_response('index.html', locals())

def processing_view(request):
	chosen_vals = request.POST.getlist('accepted_values')
	print chosen_vals

	
class AboutPageView(TemplateView):
	template_name = "about.html"