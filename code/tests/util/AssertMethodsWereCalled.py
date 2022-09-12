class AssertMethodsWereCalled(object):

    def __init__(self, list):
        self.list = list

    def __enter__(self):
        for me in self.list:
            me.orig_method = getattr(me.obj, me.method)
            setattr(me.obj, me.method, me.called)
            me.method_called = False

    def __exit__(self, exc_type, exc_value, traceback):
        for me in self.list:
            assert getattr(me.obj, me.method) == me.called, \
                "method %s was modified during AssertMethodIsCalled" % me.method

            setattr(me.obj, me.method, me.orig_method)

            # If an exception was thrown within the block, we've already failed.
            if traceback is None:
                if me.do_not_should_be_call:
                    assert not me.method_called, \
                        "method %s of %s should not be called" % (me.method, me.obj)
                else:
                    assert me.method_called, \
                        "method %s of %s was not called" % (me.method, me.obj)
