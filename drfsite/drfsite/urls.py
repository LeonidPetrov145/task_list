
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView


from project.views import ProjectViewList, ProjectViewUpdate, ProjectViewDestroy
from task.views import *


router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'categories', TaskViewSetСategories, basename='categories')
router.register(r'items', TaskViewSetTitle, basename='item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/tasklist/', TaskAPIList.as_view()),
    path('api/v1/projectlist/', ProjectViewList.as_view()),
    path('api/v1/task/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/project/<int:pk>/', ProjectViewUpdate.as_view()),
    path('api/v1/taskdelate/<int:pk>/', TaskAPIDestroy.as_view()),
    path('api/v1/projectdelate/<int:pk>/', ProjectViewDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),

]




