import abc
import datetime

import helpers


class ResultItem:
    @abc.abstractmethod
    def export_to(self, output):
        """Exports current item's data to specified output dict.
        :type output: dict
        """
        raise NotImplementedError()


class Message(helpers.DictObj):
    def __init__(self, _id, _type, text, stamp, repeat_error=None):
        """
        :type _id: str
        :type _type: str
        :type text: any
        :type stamp: datetime.datetime
        :type repeat_error: any
        """
        self.level = None
        self.identifier = None
        self.repeat_error = None
        self.stamp = None
        self.contents = None


class MessageBag(ResultItem):
    def __init__(self):
        """        
        """
        pass

    def __len__(self):
        """Returns count of messages.
        :rtype: int
        """
        pass

    def append(self, _type, text, _id=None, repeat_error=None):
        """Appends new message.
        :type _type: str
        :type text: any
        :type _id: str
        :type repeat_error: any
        """
        pass

    def message(self, text, _id=None):
        """Appends new message of type `message`.
        :type text: any
        :type _id: str
        """
        pass

    def warning(self, text, _id=None):
        """Appends new message of type `warning`.
        :type text: any
        :type _id: str
        """
        pass

    def error(self, text, _id=None, repeat_error=None):
        """Appends new message of type `error`.
        :type text: any
        :type _id: str
        :type repeat_error: any
        """
        pass

    def exception(self, err, stack, _id=None):
        """Appends new message of type `error`.
        :type err: BaseException
        :type stack: str
        :type _id: str
        """
        pass

    def export_to(self, output):
        """Exports current item's data to specified output dict.
        :type output: dict
        """
        pass


class PostActions(ResultItem):
    def __init__(self):
        """        
        """
        pass

    def file_exported(self, emails, file_id):
        """Adds new `file-exported` post-action.
        :type emails: list
        :type file_id: str
        """
        pass

    def new_config(self, field, value):
        """Adds new `new-config` post-action.
        :type field: str
        :type value: any
        """
        pass

    def export_to(self, output):
        """Exports current item's data to specified output dict.
        :type output: dict
        """
        pass


class Results(ResultItem):
    def __init__(self):
        """        
        """
        pass

    @property
    def messages(self):
        """Returns message bag.
        :rtype: MessageBag
        """
        pass

    @property
    def post_actions(self):
        """Returns post actions.
        :rtype: PostActions
        """
        pass

    def export_to(self, output):
        """Exports current item's data to specified output dict.
        :type output: dict
        """
        pass
