from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentapi',views.StudentModelViewSet, basename='student')


# this is only for read data
router2 = DefaultRouter()
router2.register('studentapi',views.StudentReadOnlyModelViewSet, basename='student')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('readonly/',include(router2.urls)),
]