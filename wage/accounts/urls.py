from django.urls import re_path
from accounts import views
from django.conf.urls import url

urlpatterns = [
    re_path('^signup/$', views.signup_view),
    re_path('^login/$', views.LoginView.as_view(), name='nurse_login'),
    re_path('^login/refresh/$', views.AccessRefreshView.as_view(), name='login_refresh'),
    # re_path('^reset_password/$', views.ResetPasswordView.as_view()),
    # re_path('^change_password/$', views.ChangePasswordView.as_view()),
    # re_path('^approve_user/$', views.ApproveUserView.as_view()),
    # re_path('^block_user/$', views.BlockUserView.as_view()),
    # re_path('^user_profile/$', views.UserProfileView.as_view()),
    # url(r'^profile_photo/$', views.ProfilePhotoUpdate.as_view(), name='update_photo'),
]