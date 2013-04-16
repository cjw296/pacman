print "in package __main__.py"
from . import test
if __name__=='__main__':
    print '__main__.__main__'
    print test
