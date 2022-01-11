import ftplib

import filesystem
import models


class Adapter(filesystem.Adapter):
    def __init__(self, credential):
        """
        :type credential: models.Credential
        """
        pass

    def session(self):
        """Returns new ftp-session.
        :rtype: ftplib.FTP
        """
        pass

    @property
    def bucket_name(self):
        """Returns current bucket name.
        :rtype: str
        """
        pass

    def file_exists(self, path):
        """Returns true is specified path object exists physically as file.
        :type path: filesystem.Path
        :rtype: bool
        """
        pass

    def directory_exists(self, path):
        """Returns true is specified path object exists physically as directory.
        :type path: filesystem.Path
        :rtype: bool
        """
        pass

    def delete_file(self, path):
        """Deletes path object physically as file.
        Returns true on success.
        :type path: filesystem.Path
        :rtype: bool
        """
        pass

    def delete_directory(self, path):
        """Deletes path object physically as directory.
        Returns true on success.
        :type path: filesystem.Path
        :rtype: bool
        """
        pass

    def stat(self, path):
        """Returns stat of path.
        Returns true on success.
        :type path: filesystem.Path
        :rtype: filesystem.Stat
        """
        pass

    def open(self, path, **kwargs):
        """Opens file for I/O purposes.
        Returns opened file descriptor.
        
        Supported `kwargs`:
            – mode: str
            – buffering: int
            – encoding: str
            – errors: str
            – newline: str
            – closefd: str
        :type path: filesystem.Path
        :rtype: typing.IO
        """
        pass

    def upload(self, src, dst, *args):
        """Uploads from local source to external destination.
        Available `args`:
            *none*
        :type src: filesystem.Path
        :type dst: filesystem.Path
        """
        pass

    def download(self, src, dst, *args):
        """Downloads from external source to local destination.
        Available `args`:
            *none*
        :type src: filesystem.Path
        :type dst: filesystem.Path
        """
        pass

    def list_directory(self, path, recursive=True, files=True, folders=True):
        """Returns list of files in specified directory.
        :type path: filesystem.Path
        :type recursive: bool
        :type files: bool
        :type folders: bool
        :rtype: typing.Generator[filesystem.Path]
        """
        pass
