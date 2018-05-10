from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [ path('admin/', admin.site.urls),
    path('',views.idx, name='idexes'),
    # path('definitions',views.definitions, name='definitions_home'),
    path('definitions/<int:selected_idx>',views.AlgoIndexListView.as_view(), name='definitions'),
    path('definitions',views.AlgoIndexListView.as_view(), name='definitions'),
    path('monitor',views.monitor, name='monitor_home'),
    path('snippet/', include('snippets.urls'))

]
