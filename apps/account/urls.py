from django.conf.urls import url

from apps.account import views

urlpatterns = [
    url(r'^$', views.user_list, name='account_user_list'),
    url(r'^(\d+)$', views.user_detail, name='account_user_detail'),
    url(r'^(\d+)/delete$', views.user_delete, name='account_user_delete'),
    url(r'^new$', views.user_new, name='account_user_new'),
    url(r'^download$', views.user_list_download, name='account_user_list_download'),
]
