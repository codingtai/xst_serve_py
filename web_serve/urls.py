from django.urls import path
from web_serve.views.home import register, home_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/register/", register.send_sms, name='send_sms'),
    path("home/reglogin/", register.reg_login, name='reg_login'),
    path("home/pwdlogin/", register.login, name='login'),
    path("home/loginout/", register.login_out, name='login_out'),

    path("home/banner/", home_page.get_banner, name='banner'),
    path("home/rank/", home_page.get_rank, name='rank'),
    path("home/category/", home_page.get_category, name='category'),
    path("home/serve/", home_page.get_serve, name='serve'),
    path("home/land/", home_page.get_land, name='land'),
    path("home/local/", home_page.get_local, name='local'),
    path("home/water/", home_page.get_water, name='water'),
    path("home/sea/", home_page.get_sea, name='sea'),
    path("home/detail/", home_page.get_detail, name='detail'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
