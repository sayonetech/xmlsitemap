from django.conf.urls import patterns,url

from .conf import OTHER_SITEMAPS
from .models import XMLSitemap
from .sitemaps import ModelSitemap

model_sitemaps = {
    'pages': ModelSitemap(XMLSitemap.get_active_siteurls()),
}
model_sitemaps.update(OTHER_SITEMAPS)

urlpatterns = patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'sitemap', {'sitemaps': model_sitemaps}),
)