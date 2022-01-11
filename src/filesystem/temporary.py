import typing

import basement.temporary as temp_global
import filesystem


class TempFile(temp_global.TemporaryObject):
    def __init__(self, adapter, path):
        """
        :type adapter: filesystem.Adapter
        :type path: filesystem.Path
        """
        pass

    @property
    def adapter(self):
        """Returns adapter instance.
        :rtype: filesystem.Adapter
        """
        pass

    @property
    def path(self):
        """Returns path instance.
        :rtype: filesystem.Path
        """
        pass

    @property
    def handle(self):
        """Returns opened file handle.
        :rtype: typing.IO
        """
        pass

    @property
    def is_opened(self):
        """Returns true is current file is opened.
        :rtype: bool
        """
        pass

    def open(self, **kwargs):
        """Opens file for I/O purposes.
        Returns opened file descriptor.
        
        Supported `kwargs`:
            – mode: str
            – buffering: int
            – encoding: str
            – errors: str
            – newline: str
            – closefd: str
        :rtype: typing.IO
        """
        pass

    def close(self):
        """Closes opened file handle.
                
        """
        pass

    def rollback_temp(self):
        """Eliminates temporary object.
                
        """
        pass
