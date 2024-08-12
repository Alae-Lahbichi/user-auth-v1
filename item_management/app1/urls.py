from django.urls import path 
from .views import main_page , login_page , signup_page , logout_page ,add_product
from django.conf import settings
from django.conf.urls.static import static

app_name = "projet"

urlpatterns = [
    path('main/',main_page,name="main"),
    path('login/',login_page,name="login"),
    path('signup/',signup_page,name="signup"),
    path('logout/',logout_page,name='logout'),
    path('',add_product,name='add'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
