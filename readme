# xmlsitemap
### installation steps

1. Add to settings.py
```
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sitemaps',#required
    'xmlsitemap',#required

)
```js

2. Add to url.py
  
urlpatterns = patterns('',
    #other urls
    url(r'^', include('xmlsitemap.urls')),

)

3. You can see the available sitemaps in the url http://yourdomain/sitemap.xml.
4. You can add more sitemaps in the settings variable "XML_OTHER_SITEMAPS"
#Example in your settings.py file
from ***.sitemaps import TagSitemap,EntrySitemap
from cms.sitemaps import CMSSitemap
XML_OTHER_SITEMAPS = {
 'blog':EntrySitemap,
 'blog_tags':TagSitemap,
 'cms_tags':CMSSitemap, # for cms sitemap
}

4. To add more static site map entries goto admin section http://yourdomain/admin/xmlsitemap/xmlsitemap/.
