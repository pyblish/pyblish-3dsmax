# Import third-party modules
import pyblish.api


class CollectPhotoshopCurrentFile(pyblish.api.ContextPlugin):
    """Inject the current active document file path into context."""

    order = pyblish.api.CollectorOrder - 0.5
    label = "3dsMax Current File."

    hosts = ['3dsmax']
    version = (0, 1, 0)

    def process(self, context):
        """Inject the current working file"""
        import os
        from pymxs import runtime as rt
        current_file = rt.maxFilePath + rt.maxFileName
        normalised = os.path.normpath(current_file)
        self.log.info("Find current working file %s", normalised)
        context.set_data('currentFile', value=normalised)
