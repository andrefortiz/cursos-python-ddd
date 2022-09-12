from functools import wraps

from utils.responses.Responses import ResponseError


def validator_interceptor(validator, request):
    """
    Decorator for views that checks that the users passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the users object and returns True if the users passes.
    """

    def decorator(f):
        @wraps(f)
        def wrapped_validator_interceptor(*args, **kwargs):
            domain_class = validator.validate(request)
            if validator.is_valid():
                return f(domain_class, *args, **kwargs)

            return ResponseError(message="Erro ao validar a requisição", error=validator.errors)
        return wrapped_validator_interceptor
    return decorator