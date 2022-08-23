""" Remote BLOB host module views
"""
from core_parser_app.tools.modules.views.builtin.input_module import AbstractInputModule
from xml_utils.xsd_tree.operations.xml_entities import XmlEntities
from core_module_blob_host_app.views.views import BlobHostModule
from core_module_remote_blob_host_app.settings import AUTO_ESCAPE_XML_ENTITIES
from core_module_remote_blob_host_app.views.forms import URLForm


class RemoteBlobHostModule(AbstractInputModule):
    """Remote Blob Host Module"""

    def __init__(self):
        """Initialize the module"""
        AbstractInputModule.__init__(self, label="Enter the URL of a file:")

    def _render_module(self, request):
        """Render module

        Args:
            request:

        Returns:

        """
        return AbstractInputModule._render_module(self, request)

    def _retrieve_data(self, request):
        """Return module's data

        Args:
            request:

        Returns:

        """
        data = ""
        self.error = None
        data_xml_entities = XmlEntities()
        if request.method == "GET":
            if "data" in request.GET:
                if len(request.GET["data"]) > 0:
                    data = request.GET["data"]
        elif request.method == "POST":
            if "data" in request.POST:
                url_form = URLForm({"url": request.POST["data"]})
                if url_form.is_valid():
                    data = url_form.data["url"]
                else:
                    self.error = "Enter a valid URL."

        return (
            data_xml_entities.escape_xml_entities(data)
            if AUTO_ESCAPE_XML_ENTITIES
            else data
        )

    def _render_data(self, request):
        """Return module's data rendering

        Args:
            request:

        Returns:

        """
        return BlobHostModule.render_blob_host_data(self.data, self.error)
