from django.urls import path, include
from django.conf import settings
from django.views.static import serve




urlpatterns = [
    path('<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    
]

# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = [
#     # ... other URL patterns ...
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += Pattern("",
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve',
#             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
#         (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#             {'document_root': settings.STATIC_ROOT, }),)

# # # if settings.DEBUG:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = i18n_patterns(
#     path('', admin.site.urls),
#     path('api/education/', include('education.urls'))
# )
# if settings.SERVE_MEDIA:
# urlpatterns += static(
#     (r'^media/(?P<path>.*)$', 'django.views.static.serve',
#         {'document_root': settings.STATIC_ROOT, 'show_indexes': True }),
#     (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#         {'document_root': settings.STATIC_ROOT, })),ss