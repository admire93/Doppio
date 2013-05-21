import json
import urllib2

class InvalidMintpressoTokenError(Exception):
    pass

class InvalidMintpressoPrameterError(Exception):
    pass

class Doppio(object):
    protocol = 'http'
    host = 'api.mintpresso.com'
    port = '80'
    version = 'v1'
    mint_path = {
      'point': "/account/{0}/point",
      'edge': "/account/{0}/edge",
      'point.id': "/account/{0}/point/{1}"
    }
 
    def __init__(self, token):
        splited = token.split("::")
        if len(splited) <= 1 or len(splited) >= 3:
            raise InvalidMintpressoTokenError()

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
        result = {}
        if len(args) == 7:
            result = {
                'subjectId': args[0],
                'subjectType': args[1],
                'subjectIdentifer': args[2],
                'verb': args[3],
                'objectId': arg[4],
                'objectType': arg[5],
                'objectIdentifer': arg[6]
            }
        elif len(args) == 5:
            result = {
                'subjectType': args[0],
                'subjectIdentifer': args[1],
                'verb': args[2],
                'objectType': arg[3],
                'objectIdentifer': arg[4]
            }
        elif len(args) == 2:
            result = {
                'type': args[0],
                'identifier': args[1]
            }
        elif len(kwards) > 0 and \
             (kwards.has_key('type') or kwards.has_key('verb')):
            result = kwards
        else:
            raise InvalidMintpressoPrameterError()

        # TODO: Check validate of data in result.
        return result

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
        resp = None
        d = self.arg_validator(args, kwards)
        if d.has_key("verb"):
            pass
            # Set Edge to mintpresso
        else:
            return self.set_point(d)

    def get_point(self, d):
        return d

    def set_point(self, d):
        p = self.route('point')
        data = json.dumps({'point': d})
        header = {'Content-Type': 'application/json;charset=utf-8',
                  'Accepts': 'application/json'}
        req = urllib2.Request(p, data.encode('utf-8'), header)
        try:
            resp = urllib2.urlopen(req)
        except urllib2.URLError, e:
            print "Error occured, reason: {0}, url: {1}".format(e.reason, p)
            return None
        
        res = json.loads(resp.read())
        code = res[u'status'][u'code']
        msg = res[u'status'][u'message']
        if code == 200 or code == 201:
            return res[u'point']
        else:
            print 'Mintpresso set failed. code:{0},message:{1}'.format(code,msg)
            return None

        return d

    def get_edge(self, d):
        return d

    def set_edge(self, d):
        return d
