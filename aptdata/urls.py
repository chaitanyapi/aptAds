from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout


app_name='aptdata'
urlpatterns=[
	url(r'^$',views.indexview.as_view(),name='index'),
	url(r'^register/$',views.userformview.as_view(),name='register'),
	# url(r'^register/$',views.userformview, name='register'),
	url(r'login/', views.userloginview.as_view(),name='login'),#''django.contrib.auth.views.login'),
	# url(r'login/', login, {'template_name':'aptdata/login_form.html'}),
	url(r'wrong/',views.loginpage, name='incorrect'),
	url(r'logout/$', views.user_logout, name='logout'),
	#url(r'^login/$', auth_views.login, name='login'),
	#url('^aptdata/', 'django.contrib.auth.urls'),
	#url(r'^logout/$', auth_views.logout, name='logout'),
	#url(r'^admin/', admin.site.urls), 

	#apartment related URLs
	url(r'^(?P<pk>[0-9]+)/$',views.detailview.as_view(),name='detail'),
	url(r'aptdata/add/$',views.addapt.as_view(),name='apt-add'),
	url(r'aptdata/(?P<pk>[0-9]+)/$', views.updateapt.as_view(), name='apt-update'),
	url(r'aptdata/(?P<pk>[0-9]+)/delete/$', views.deleteapt.as_view(), name='apt-delete'),

	#employee related URLs
	url(r'emp/$',views.listemp.as_view(), name='listemp'),
	url(r'emp/(?P<pk>[0-9]+)/$',views.empdetail.as_view(), name = 'empdetail'),
	url(r'emp/update/(?P<pk>[0-9]+)/$',views.updateemp.as_view(), name = 'updateemp'),
	url(r'emp/add/$',views.addemp.as_view(), name='addemp'),

	#Boards related URLs
	url(r'board/(?P<pk>[0-9]+)/$',views.boardlist.as_view(), name= 'boardlist'),
	url(r'board/add/(?P<pk>[0-9]+)/$',views.addboard.as_view(),name='addboard'),
	url(r'board/update/(?P<pk>[0-9]+)/$',views.updateboard.as_view(),name='updateboard'),
	url(r'board/detail/(?P<pk>[0-9]+)/$',views.boarddetail.as_view(), name='boarddetail'),

	#activity related URLs
	url(r'activity/(?P<pk>[0-9]+)/$',views.activitylist.as_view(), name='activitylist'),
	url(r'activity/add/(?P<pk>[0-9]+)/$', views.addactivity.as_view(), name='addactivity'),
	url(r'activity/update/(?P<pk>[0-9]+)/$',views.updateactivity.as_view(), name='updateactivity'),
	url(r'activity/detail/(?P<pk>[0-9]+)/$',views.activitydetail.as_view(), name='activitydetail'),

	#these are the urls for vacant boards
	url(r'vacant/$', views.vacantboarddetail.as_view(), name='vacant'),

	#from here the advertiser relaed urls
	url(r'advt/$', views.advt_list.as_view(), name='advtlist'),
	url(r'advt/add/$', views.add_advt.as_view(), name='addadvt'),
	url(r'advt/(?P<pk>[0-9]+)/$', views.advtdetail.as_view(), name='advtdetail'),
	url(r'advt/update/(?P<pk>[0-9]+)/$', views.advt_updated.as_view(), name='advtupdate'),

	url(r'advt/categoery/(?P<pk>[0-9]+)/$', views.categoery_view.as_view(), name='categoerylist'),
	url(r'advt/categoery/add/$', views.categoery_add.as_view(), name='categoeryadd'),

	#campaign url
	url(r'campaign/(?P<pk>[0-9]+)/$', views.campaign_detail.as_view(), name='campaign_detail'),
	#url(r'campaign/add/$', views.campaign_add.as_view(), name='campaign_add'),
	url(r'usertask/$',views.get_user_page.as_view(), name='get_user_page'),

	]

