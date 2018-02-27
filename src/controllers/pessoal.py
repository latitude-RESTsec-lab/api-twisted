from twisted.web import server, resource, client
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


class EmployeeRoot(resource.Resource):
    """Serve one employee operations.

       Using this link as example: https://twistedmatrix.com/documents/current/web/howto/web-in-60/dynamic-dispatch.html

       Look this too: http://twistedmatrix.com/documents/current/web/howto/using-twistedweb.html
    """

    def __init__(self):
        print("inicializou Employee.")
        pass

    def  getChildWithDefault(self, name, request):
        print("executou o getChild do Employee.")
        if name == '':
            return self
        if not isinstance(name, int):
            print("o child entendeu que nao eh INT.")
            return self
        return EmployeeResource(int(name))

    def render_GET(self, request):
        print("passou pelo GET do base")
        return "obs: nao atender GET de employee: {}".format(request)

    def render_DELETE(self, request):
        return "obs: nao atender DELETE de employee: {}".format(request)


class EmployeeResource(resource.Resource):
    def __init__(self, employee_id):
        resource.Resource.__init__(self)
        print ("employee_id={}".format(employee_id))
        self.employee_id = employee_id

    def render_GET(self, request):
        print ("GET request={}".format(request))
        return "<html><body><pre>%s</pre></body></html>" % self.employee_id

    def render_DELETE(self, request):
        print ("DELETE request={}".format(request))
        return "hello DELETE world from the employee: {}".format(request)
