""" Url router for the remote blob host module
"""

from django.urls import re_path

from core_module_remote_blob_host_app.views.views import RemoteBlobHostModule

urlpatterns = [
    re_path(
        r"module-remote-blob-host",
        RemoteBlobHostModule.as_view(),
        name="core_module_remote_blob_host_view",
    ),
]
