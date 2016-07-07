from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='landingpage1.html')),
    
    url(r'^landingpage/$', TemplateView.as_view(template_name='landingpage1.html'), name='landingpage'),
    url(r'^email_submission/$','main.views.email_submission'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

