from django.urls import path
from api_basic import views

urlpatterns = [
    path('', views.article_list, name='article-list'),
    path('detail/<int:pk>/', views.article_detail, name='article-detail'),
    # path('', views.ArticleAPIView.as_view(), name='article-list'),
    # path('detail/<int:pk>/', views.ArticleDetail.as_view(), name='article-detail'),
    # path('', views.ArticleListGenericAPIView.as_view(), name='article-list'),
    # path('detail/<int:pk>/', views.ArticleDetailGenericAPIView.as_view(), name='article-detail'),
]