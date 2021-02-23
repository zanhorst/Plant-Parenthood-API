from django.urls import path
from .views.post_views import Posts, PostDetail, PostFilter
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('posts/', Posts.as_view(), name='post'),
    path('posts-filter/', PostFilter.as_view(), name='post-filter'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
