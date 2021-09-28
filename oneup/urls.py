from django.urls import path

from . import views

app_name = 'oneup'

urlpatterns = [
    path('outsourcing/', views.index, name='outsourcing'),
    path('manufacture/', views.manufacturer, name='manufacture'),
    path('logistics/', views.logistics, name='logistics'),
    path('as/', views.after, name='after'),
    path('main/', views.main, name='main'),
    path('deny/', views.deny, name='deny'),
    path('as_service/', views.as_create, name='as_create'),
    path('export1/', views.export1, name='out_export'),
    path('export2/', views.export2, name='make_export'),
    path('export3/', views.export3, name='log_export'),
    path('export4/', views.export4, name='as_export'),
    ]