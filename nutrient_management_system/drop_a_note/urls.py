from django.conf.urls import url

from drop_a_note import views

app_name = 'contact'

urlpatterns = [
    url(r'^$', views.contact, name='contact')
]