class BaseErr:
    status = 1
    msg = 'Default Error'

    def __init__(status, msg, self):
        self.status = status
        self.msg = msg

    def toDict(self):
        return self.__dict__


class NoResErr(BaseErr):
    def __init__(self):
        BaseErr.__init__(1, 'No Result Found', self)
