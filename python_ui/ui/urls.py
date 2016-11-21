from django.conf.urls import url
from ui import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
	url(r'^process/$', 'ui.views.processing_view'),
	url(r'^about/$', views.AboutPageView.as_view()),
]