def date():
    import datetime
    now=datetime.datetime.now
    return str(now().date())

def time():
    import datetime
    now=datetime.datetime.now
    return str(now().time())
