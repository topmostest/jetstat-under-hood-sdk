import helpers


class Path(helpers.DictObj):
    def __init__(self, **kwargs):
        """Supported `kwargs`:
            - absolute: bool
            and one of:
            - full: str
            or:
            - path: str
            - name: str
            - extension: str
        """
        pass

    @property
    def full_path(self):
        """Returns full path of file.
        :rtype: str
        """
        pass

    @property
    def directory(self):
        """Returns directory of file.
        :rtype: str
        """
        pass

    @property
    def name(self):
        """Returns name of file without extension.
        :rtype: str
        """
        pass

    @property
    def extension(self):
        """Returns extension of file.
        :rtype: str
        """
        pass

    @property
    def full_name(self):
        """Returns name of file connected with its extension.
        :rtype: str
        """
        pass

    @property
    def is_file_path(self):
        """Returns true if current path represents file path.
        :rtype: bool
        """
        pass
