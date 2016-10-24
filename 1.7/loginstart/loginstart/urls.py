from django.conf.urls import patterns, include, url
from django.contrib import admin
from principal.views import IndexView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loginstart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('', include('social.apps.django_app.urls', namespace = 'social')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', IndexView.as_view()),
)
