import random
import string


def random_string(prefix, maxlen, symbols=None, digits=None):
    if symbols != None:
        symbols = string.ascii_letters + " "*1
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    elif digits !=None:
        digits = string.digits + "-"*3
        return prefix + "".join([random.choice(digits) for i in range(random.randrange(maxlen))])
    else:
        all = string.ascii_letters + string.digits +  string.punctuation + " "*10
        return prefix + "".join([random.choice(all) for i in range(random.randrange(maxlen))])