from twisted.web import server, resource
#from twisted.internet import reactor, endpoints

class Employee(resource.Resource):
    isLeaf = True
    numberRequests = 0

    def render_GET(self, request):
        print("get ==> {}".format(request))
        self.numberRequests += 1
        request.setHeader(b"content-type", b"text/plain")
        content = u"I am request #{}\n".format(self.numberRequests)
        return content.encode("utf-8")
