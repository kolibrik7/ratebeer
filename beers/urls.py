from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.zoznam, name="zoznam"),
	url(r'^pridanie_piva/$', views.pridanie_piva, name="pridanie_piva")
]