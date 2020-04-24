print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# any of this should not be used
# in python all created variable are public
# you don't want to overwrite a name

# you can also learn more about the module like this
# import shelve
# help(shelve)

# you can be more specific
import random
help(random.randint)