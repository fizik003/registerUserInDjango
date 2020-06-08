from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account.views import dashboard, register
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'account'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uid64>/<token>/', PasswordResetConfirmView.as_view, name='password_reset_confirm'),
    # path('reset/done', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)