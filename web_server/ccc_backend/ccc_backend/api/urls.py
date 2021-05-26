from ccc_backend.api.views.yangjing import *
from ccc_backend.api.views.jade import *
from ccc_backend.api.views.yilin import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path


urlpatterns = []

urlpatterns = [path('main/emotion.html/', multi_chart_emotion)]

urlpatterns += [path('main/social_impact.html', multi_chart_social)]

urlpatterns += [path('main/timeline.html', multi_chart_timeline)]

urlpatterns += [path('main/', main_page)]

urlpatterns += [path('main/emotion.html/', emotion)]

urlpatterns += [path('main/timeline.html', timeline)]

urlpatterns += [path('main/live_tweets.html', live_tweets)]

urlpatterns += [path('main/social_impact.html', social_impact)]


