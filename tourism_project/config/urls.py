from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

# schema از فایل config/schema.py وارد می‌شود
from config.schema import schema

urlpatterns = [
    path('api/token/', obtain_auth_token),
    path('admin/', admin.site.urls),
    path('api/', include('destinations.urls')),
    path('api/', include('plans.urls')),
    path('api/', include('accounts.urls')),

    # مسیر GraphQL واحد
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
