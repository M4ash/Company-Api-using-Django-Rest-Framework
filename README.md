# Company-Api-using-Django-Rest-Framework
This is a sample of the creation of a Company Api and its employees using Django Rest Framework

Follow these URLs to go and check the APIs in the server:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page, name='home'),
    path('api/v1/', include('api.urls'))
]
