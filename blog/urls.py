from django.urls import path
from . import views

urlpatterns = [
    #path('',views.BlogView,name='blogs'),
    #path('detail/<int:id>',views.DetailBlogView,name='detail_blog'),

    path('', views.BlogListView.as_view(), name='blogs'),
    path('detail/<int:id>', views.BlogDetailView.as_view(), name='blogs'),
] 