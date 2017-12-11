from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index_page'),
    url(r'cadastroDados/$', views.cadastroDados, name='cadastro_dados'),
    url(r'cadastroGource/$', views.cadastroGource, name='cadastro_gource'),
    url(r'videoForm/$', views.showvideo, name='video_form'),
]
