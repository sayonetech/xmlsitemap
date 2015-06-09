from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from datetime import datetime


class BasicSitemap(Sitemap):

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return reverse(obj)


class ModelSitemap(Sitemap):

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return obj.change_frequency

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return obj.url
