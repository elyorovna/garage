from django.urls import path

from blog.views import index, contact, detail, category

urlpatterns =[
    path('', index, name = 'index'),
    path('contact/', contact, name = 'contact'),
    path('detail/<int:id>/', detail, name = 'detail'),
    path('category/<int:id>/',category, name= 'category')
]