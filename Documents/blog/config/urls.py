
from django.contrib import admin
from django.urls import path
from app.views import home,project_detail,blog_detail,blog,about,portfolio
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('project_detail/<int:pk>/',project_detail, name='project_detail'),  #<int:pk>/  #,project_detail, name='project_detail'
    path('blog_detail/<int:pk>/',blog_detail,name='blog_detail'),
    path('about',about),
    path('blog',blog,name='blog'),
    path('portfolio',portfolio)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
