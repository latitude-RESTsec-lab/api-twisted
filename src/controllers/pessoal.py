from twisted.web import server, resource
#from twisted.internet import reactor, endpoints

class Employees(resource.Resource):
    """Serve serveral employees operations.
    """
    isLeaf = True
    numberRequests = 0

    def render_GET(self, request):
        print("get ==> {}".format(request))
        self.numberRequests += 1
        request.setHeader(b"content-type", b"text/plain")
        content = u"I am get request #{}\n".format(self.numberRequests)
        return content.encode("utf-8")

    def render_POST(self, request):
        print("post ==> {}".format(request))
        self.numberRequests += 1
        request.setHeader(b"content-type", b"text/plain")
        content = u"I am post request #{}\n".format(self.numberRequests)
        return content.encode("utf-8")


class Employee(resource.Resource):
    """Serve one employee operations.
    """
    def render_GET(self, request):
        return "hello world from the employee: {}".format(request)
