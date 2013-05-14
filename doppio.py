import urllib2

class InvalidMintpressoTokenError(Exception):
    pass

class Doppio(object):
    def __init__(self, token):
        splited = token.split("::")
        if len(splited) <= 1 or len(splited) >= 3:
            raise UnvalidMintpressoTokenError()

        self.token = splited[0]
        self.access_id = splited[1]

    def get(self, *args, **kwards):
        print args
        print kwards
        return {}

    def set(self, *args, **kwards):
        print args
        print kwards
        return {}

    def get_point(self, d):
        return d

    def set_point(self, d):
        return d

    def get_edge(self, d):
        return d

    def set_edge(self, d):
        return d
