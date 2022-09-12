import inspect


class MethodIsCalled(object):
    def __init__(self, obj, method, has_return=False, do_not_should_be_call=False):
        self.obj = obj
        self.method = method
        self.has_return = has_return
        self.do_not_should_be_call = do_not_should_be_call

    def called(self, *args, **kwargs):
        self.method_called = True

        assignature = inspect.signature(self.orig_method).parameters
        if "self" in assignature:
            if self.has_return:
                return self.orig_method(self.obj, *args, **kwargs)
            else:
                self.orig_method(self.obj, *args, **kwargs)
        else:
            if self.has_return:
                return self.orig_method(*args, **kwargs)
            else:
                self.orig_method(*args, **kwargs)