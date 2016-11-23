from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

from .models import ModelosResultados

# utility functions
def rudimentaryParser(values):
	real_ids = []
	ids = []

	phr = str(values)
	sent = phr.split(',')
	print len(sent)

	if len(sent) == 1:
		ids.append((sent[0])[1:len(sent[0])-1])
	else:
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

	return real_ids

# Create your views here.
class HomePageView(TemplateView):
	
	def get(self, request, **kwargs):
		# query_results = ModelosResultados.objects.all()
		query_results = ModelosResultados.objects.filter(status='Waiting')
		accepted_results = ModelosResultados.objects.filter(status='Accept')
		rejected_results = ModelosResultados.objects.filter(status='Reject')
		data = ModelosResultados._meta.get_fields()

		# get all column field names
		fields = []
		for dat in data:
			fields.append(dat.name)

		paginator = Paginator(query_results, 10)
		# acc_paginator = Paginator(accepted_results, 10)
		# rej_paginator = Paginator(rejected_results, 10)

		page = request.GET.get('page')
		#page1 = request.GET.get('page')
		#page2 = request.GET.get('page')
		try: 
			query_results = paginator.page(page)
			#accepted_results = acc_paginator.page(page1)
			#rejected_results = rej_paginator.page(page2)
		except PageNotAnInteger:
			query_results = paginator.page(1)
			#accepted_results = acc_paginator.page(1)
			#rejected_results = rej_paginator.page(1)
		except EmptyPage: 
			query_results = paginator.page(paginator.num_pages)
			#accepted_results = acc_paginator.page(acc_paginator.num_pages)
			#rejected_results = rej_paginator.page(rej_paginator.num_pages)

		return render_to_response('index.html', locals())

class AcceptPageView(TemplateView):

	def get(self, request, **kwargs):
		results = []

		accepted_vals = request.GET['vals']
		token = request.GET['id']

		# parse request parameters
		real_ids = rudimentaryParser(accepted_vals)
		print real_ids

		for k in range(len(real_ids)):
			ch = ModelosResultados.objects.get(pk=real_ids[k])
			ch.status = 'Accept'
			ch.save()
		
		for j in range(len(real_ids)):
			results.append(ModelosResultados.objects.get(pk=real_ids[j]))

		return HttpResponseRedirect('/')

class RejectPageView(TemplateView):

	def get(self, request, **kwargs):
		results = []

		rejected_vals = request.GET['vals']
		token = request.GET['id']

		# parse request parameters
		real_ids = rudimentaryParser(rejected_vals)
		print real_ids

		for k in range(len(real_ids)):
			ch = ModelosResultados.objects.get(pk=real_ids[k])
			ch.status = 'Reject'
			ch.save()
		
		for j in range(len(real_ids)):
			results.append(ModelosResultados.objects.get(pk=real_ids[j]))

		print results

		return HttpResponseRedirect('/')

class UndoPageView(TemplateView):

	def get(self, request, **kwargs):

		undo_vals = request.GET['vals']
		
		undo_ids = rudimentaryParser(undo_vals)

		for u in range(len(undo_ids)):
			und = ModelosResultados.objects.get(pk=undo_ids[u])
			und.status = 'Waiting'
			und.save()
		return HttpResponseRedirect('/')

class DeletePageView(TemplateView):

	def get(self, request, **kwargs):

		delete_vals = request.GET['vals']

		delete_ids = rudimentaryParser(delete_vals)

		for d in range(len(delete_ids)):
			delObj = ModelosResultados.objects.get(pk=delete_ids[d])
			delObj.delete()
		return HttpResponseRedirect('/')
		
class AboutPageView(TemplateView):
	template_name = "about.html"