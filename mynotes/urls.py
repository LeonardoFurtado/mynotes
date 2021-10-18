from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from api.urls import router as notes_router

routes = []
routes.extend(notes_router.urls)


urlpatterns = [
    path(r'api/', include((routes, 'mynotes'))),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'))
]
