from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path("about/",views.aboutus,name="aboutus"),
    path("condact/",views.condactus,name="condactus"),
    path('<int:id>/',views.details,name='details'),
]