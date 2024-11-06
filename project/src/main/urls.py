from django.contrib import admin
from django.urls import path, include
from main import views  # تأكد من استيراد العرض (view) للصفحة الرئيسية

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # المسار الفارغ يشير إلى الصفحة الرئيسية
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
]
