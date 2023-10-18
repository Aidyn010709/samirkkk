from django.urls import path, include
from . import views
from applications.apartment.views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

router.register('category', CategoryModelViewSet)
router.register('comments', CommentModelViewSet)
router.register('image', ImageModelViewSet)
router.register('', ApartmentAPIVIew, basename='apartment')

urlpatterns = [
    path('get/<str:name>/', UserActionHistoryAPIView.as_view(), name='user-action-history'),
    path('recommendations/', views.ApartmentAPIVIew.as_view({'get': 'get_recommendations'}),
         name='apartment-recommendations'),
]

urlpatterns += router.urls


"""
  GNU nano 4.8                             /etc/supervisor/conf.d/samirkkk.conf                                       
[program: celery]
command=/home/sassassas107/samirkkk/venv/bin/celery A config worker
directory=/home/sassassas107/samirkkk/
user=www-data
autostart=true
autorestart=true
startsecs=0
stdout_logfile=/home/sassassas107/samirkkk/logs/celeryd.log
redirect_stderr=true

[program:celery_beat]
command=/home/sassassas107/samirkkk/venv/bin/celery -A config beat
directory=/home/sassassas107/samirkkk/
user=www-data
autostart=true
autorestart=true
startsecs=0
stdout_logfile=/home/sassassas107/samirkkk/logs/celeryb.log
redirect_stderr=true

"""
"""
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sassassas107/samirkkk;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/sassassas107/samirkkk/config.sock;
    }
}

"""
"""
  GNU nano 4.8                             /etc/systemd/system/gunicorn.service                                       
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=sassassas107
Group=www-data
WorkingDirectory=/home/sassassas107/samirkkk
ExecStart=/home/sassassas107/samirkkk/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sassassas107>

[Install]
WantedBy=multi-user.target
"""