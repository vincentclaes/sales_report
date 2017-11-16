import abc


class BaseFunction(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_report_data(self):
        raise NotImplementedError('users should implement get_report_data method.')
