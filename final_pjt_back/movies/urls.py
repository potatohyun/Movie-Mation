from django.urls import path,include
from . import views

urlpatterns = [
    path('movies/', views.movies_list),
    path('movies/<int:movies_pk>/', views.movies_detail),
    # path('comments/', views.comment_list),
    # path('comments/<int:comment_pk>/', views.comment_detail),
    # path('movies/<int:movies_pk>/comments/', views.comment_create),
    # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
