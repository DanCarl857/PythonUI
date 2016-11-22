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

class ProcessPageview(TemplateView):

	def get(self, request, **kwargs):
		results = []
		ids = []
		real_ids = []

		accepted_vals = request.GET['vals']
		token = request.GET['id']

		# parse request parameters
		phr = str(accepted_vals)
		sent = phr.split(',')
		for send in range(len(sent)):
			if send == 0:
				ids.append((sent[send])[1:])
				continue
			elif send == len(sent) - 1:
				ids.append((sent[send])[:len(sent[send])-1])
				continue
			ids.append(sent[send])
		
		for i in range(len(ids)):
			real_ids.append(eval(ids[i]))
		
		for j in range(len(real_ids)):
			results.append(Table1.objects.get(pk=real_ids[j]))

		print results

		return render_to_response('index.html', {
			'results': results
		})


class AboutPageView(TemplateView):
	template_name = "about.html"