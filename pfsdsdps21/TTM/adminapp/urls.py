from django.urls import path
from . import views

urlpatterns = [
    path("ttmhome",views.ttmhome,name="ttmhome"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("checkregistration",views.checkregistration,name="checkregistration"),
    path("checkpackages",views.checkpackages,name="checkpackages"),
    path("viewplaces",views.viewplaces,name="viewplaces"),
    path("changepassword",views.checkChangePassword,name="changepassword")
]
