import json
import traceback
from lib.action import CiscoMerakiAction


class GenericRestAction(CiscoMerakiAction):
    def run(self, method, endpointurl, queryString, data, companyId):
        try:
            if len(companyId):
                companyIdKey = companyId + '_meraki'
                value = self.action_service.get_value(companyIdKey, local=False)
                if value:
                    retrieved_data = json.loads(value)
                    access_token = retrieved_data.get('access_token', '')
                    if access_token:
                        return self.doRequest(method, endpointurl, queryString, data, access_token)
                    else:
                        return False, "Unable to retreive access_token"
                else:
                    return False, "Unable to retreive credentials"
            else:
                return False, "Please provide valid companyId"
        except Exception, e:
            print "Exception:%s TB:%s" % (e, traceback.format_exc())
            return False, "Exception"