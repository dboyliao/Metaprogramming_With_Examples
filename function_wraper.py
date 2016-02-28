def wraps(function):
    def decorator(fun):
        def ret_fun(*args, **kwargs):
            fun(*args, **kwargs)
        
        ret_fun.__name__ = function.__name__
        ret_fun.__doc__ = function.__doc__
        return ret_fun
    return decorator