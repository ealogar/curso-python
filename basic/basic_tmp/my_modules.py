print "'__name__' value:", __name__

def func():
    print "Called func in", __name__

print "'func.__module__' value:", func.__module__


if __name__ == "__main__":
    print "Inside if. This is evaluated only when the module is executed."

print "Outside if. This is evaluated always."
