from .prod import *
try:
    from .dev import *
except ModuleNotFoundError as e:
    pass
