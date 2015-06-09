# xmlsitemap
### installation steps

Add to settings.py
```js
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
```
Add to url.py
```js  
urlpatterns = patterns('',
    #other urls
    url(r'^', include('xmlsitemap.urls')),

)
```
You can see the available sitemaps in the url http://yourdomain/sitemap.xml
You can add more sitemaps in the settings variable "XML_OTHER_SITEMAPS"

Example in your settings.py file
```js
from ***.sitemaps import TagSitemap,EntrySitemap
from cms.sitemaps import CMSSitemap
XML_OTHER_SITEMAPS = {
 'blog':EntrySitemap,
 'blog_tags':TagSitemap,
 'cms_tags':CMSSitemap, # for cms sitemap
}
```
To add more static site map entries goto admin section http://yourdomain/admin/xmlsitemap/xmlsitemap/.
