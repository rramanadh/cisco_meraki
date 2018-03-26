from lib.action import CiscoMerakiAction


class GenericRestAction(CiscoMerakiAction):
    def run(self, method, endpointurl, queryString, data):
        try:
            return self.doRequest(method, endpointurl, queryString, data)
        except Exception, e:
            print "Exception:%s" % e
            return False, "Exception"