from django.conf.urls import patterns, include, url
from rest_framework import routers
from twibit_app import views

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/groups', views.GroupViewSet)
router.register(r'api/twibits', views.TwibitViewSet)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twibit.views.home', name='home'),
    # url(r'^twibit/', include('twibit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #twibit app urls
    url(r'^$', 'twibit_app.views.index'), # root
    url(r'^login$', 'twibit_app.views.login_view'), # login
    url(r'^logout$', 'twibit_app.views.logout_view'), # logout
    url(r'^signup$', 'twibit_app.views.signup'), # signup
	url(r'^twibits$', 'twibit_app.views.public'), #public twibits
	url(r'^submit$', 'twibit_app.views.submit'), #submit new twibit
    url(r'^users/$', 'twibit_app.views.users'),
    url(r'^users/(?P<username>\w{0,20})/$', 'twibit_app.views.users'),
    url(r'^follows$', 'twibit_app.views.follow'),
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
