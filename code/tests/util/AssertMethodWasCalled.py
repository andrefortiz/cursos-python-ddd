from util.AssertMethodsWereCalled import AssertMethodsWereCalled
from util.MethodIsCalled import MethodIsCalled


class AssertMethodWasCalled(AssertMethodsWereCalled):
    def __init__(self, obj, method, has_return=False):
        self.list = [MethodIsCalled(obj, method, has_return)]

    def __enter__(self):
        super().__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
