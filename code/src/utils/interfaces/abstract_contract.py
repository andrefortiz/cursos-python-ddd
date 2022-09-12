
class AbstractContract:

    errors = []

    def __init__(self,  domain_class):
        self.domain_class = domain_class

    def is_valid(self):
        return len(self.errors) == 0




