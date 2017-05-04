from django.conf.urls import url
from manager import views

urlpatterns = [
    url(r'^alltasks/$', views.task_list),
    url(r'^task/(?P<pk>[0-9]+)/$', views.task_detail),
    url(r'^login/', views.Login),
    url(r'^register/', views.Register),
    url(r'^getallroads/', views.getAllRoads),
    url(r'^getroad/', views.getRoad),
    url(r'^addroad/', views.addRoad),
    url(r'^updatestatus/', views.updateStatus),
]