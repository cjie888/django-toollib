from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.home'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'image/(?P<key>\w+)/$','captcha.views.captcha_image',name='captcha-image'),
    url(r'new/key/$','toollib.verificationcode.captcha_new_key',name='captcha-new-key'),
    # Examples:
    # url(r'^$', 'verifycode.views.home', name='home'),
    # url(r'^verifycode/', include('verifycode.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
