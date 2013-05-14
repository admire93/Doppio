import json
import urllib2

class InvalidMintpressoTokenError(Exception):
    pass

class InvalidMintpressoPrameterError(Exception):
    pass

class Doppio(object):
    protocol = 'http'
    host = 'api.mintpresso.com'
    port = '9001'
    version = 'v1'
    mint_path = {
      'point': "/account/{0}/point",
      'edge': "/account/{0}/edge",
      'point.id': "/account/{0}/point/{1}"
    }
 
    def __init__(self, token):
        splited = token.split("::")
        if len(splited) <= 1 or len(splited) >= 3:
            raise UnvalidMintpressoTokenError()

        self.token = splited[0]
        self.account_id = splited[1]

    def route(self, k, i=None):
       if i is None:
           p = self.mint_path[k].format(self.account_id)
       else: 
           p = self.mint_path[k].format(self.account_id, i)
       return self.uri(p)
        
    def uri(self, path):
        form = "{protocol}://{host}:{port}/{version}{path}?api_token={token}"
        return form.format(protocol=self.protocol,
                           host=self.host,
                           port=self.port,
                           version=self.version,
                           path=path,
                           token=self.token)


    def arg_validator(self, args, kwards):
        if (len(args) == 0 and len(kwards) == 0) or len(args) > 1:
	    raise TypeError()
        elif len(args) == 1:
            return args
        elif len(kwards) > 0:
            return kwards

    def get(self, *args, **kwards):
        d = self.arg_validator(args, kwards)
        if d.has_key("verb"):
            pass
            # Get Edge to mintpresso
        else:
            # Set Point to mintpresso
            pass

        return {}

    def set(self, *args, **kwards): 
        d = self.arg_validator(args, kwards)
        header = {
            'Content-Type': 'application/json;charset=utf-8',
            'Accepts': 'application/json'
        }
        if d.has_key("verb"):
            pass
            # Set Edge to mintpresso
        else:
            p = self.route('point')
            if not (d.has_key('type') and d.has_key('identifier')):
                raise InvalidMintpressoPrameterError()

            data = json.dumps(d)
            req = urllib2.Request(p, data.encode('utf-8'), header)
            try:
                resp = urllib2.urlopen(req)
            except urllib2.URLError as e:
                print "Error occured, reason: {0}, url: {1}".format(p, e.reason)
                return None
                
        return resp.read()

    def get_point(self, d):
        return d

    def set_point(self, d):
        return d

    def get_edge(self, d):
        return d

    def set_edge(self, d):
        return d
