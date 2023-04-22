import zope.interface


class IViewProblema(zope.interface.Interface):
    def viewProblems():
        pass

@zope.interface.implementer(IViewProblema)
class SimpleView:

    def viewProblems():
        return z**3