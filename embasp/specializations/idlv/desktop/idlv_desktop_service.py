from ....base.option_descriptor import OptionDescriptor
from ....platforms.desktop.desktop_service import DesktopService
from ..idlv_minimal_models import IDLVMinimalModels


class IDLVDesktopService(DesktopService):
    """Extention of DesktopService for DLV2."""

    def __init__(self, exe_path):
        super(IDLVDesktopService, self).__init__(exe_path)
        self._load_from_STDIN_option = "--stdin"

    def _get_output(self, output, error):
        """Returns a new IDLVMinimalModels object from given output and error."""
        return IDLVMinimalModels(output, error)

    def start_async(self, callback, programs, options):
        """Calls start_async method of a superclass."""
        super(IDLVDesktopService, self).start_async(
            callback, programs, options)

    def start_sync(self, programs, options):
        """Calls start_sync method of a superclass and returns its output
        object."""

        new_options = list(options)
        new_options.append(OptionDescriptor("--t"))
        return super(IDLVDesktopService, self).start_sync(programs, new_options)
