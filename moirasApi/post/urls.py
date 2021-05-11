from django.urls import path,include
# from .views import TasksView,TaskCreatView,TaskDeleteUpdateView
from .views import PostViewSet,ImagePostViewSet,UrlPostViewSet,CommentViewSet,UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('default-posts',PostViewSet)
router.register('image-posts',ImagePostViewSet)
router.register('url-posts',UrlPostViewSet)
router.register('comment',CommentViewSet)
router.register('users',UserViewSet)

urlpatterns = [
    path('',include(router.urls))
]
