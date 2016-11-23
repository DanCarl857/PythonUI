from django.conf.urls import url
from ui import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
	url(r'^accept/$', views.AcceptPageView.as_view()),
	url(r'^reject/$', views.RejectPageView.as_view()),
	url(r'^undo/$', views.UndoPageView.as_view()),
	url(r'^delete/$', views.DeletePageView.as_view()),
	url(r'^about/$', views.AboutPageView.as_view()),
]