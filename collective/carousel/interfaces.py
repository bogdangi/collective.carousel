from Products.ATContentTypes.interface import IATContentType
from Products.ATContentTypes.interface import IATNewsItem
from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.carousel')

try:
    from collective.contentleadimage.interfaces import ILeadImageable
except:
    ILeadImageable = None


class ICollectiveCarouselLayer(Interface):
    """ A layer specific to collective.carousel
    """


class ICarouselProvider(Interface):
    """ We should be able to mark objects that can be used in carousel with
        the special marker. For now this marks Collections only.
    """


if ILeadImageable is not None:
    # Need to make sure we come up top
    class IATWithLeadImage(ILeadImageable, IATContentType):
        """ More specific interface """

    class IATNewsItemWithLeadImage(ILeadImageable, IATNewsItem):
        """ More specific interface """


class ICarouselSettings(Interface):
    """Global Carousel settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    carousel_viewlet_max_size = schema.Int(
        title=_(u"Carousel viewlet max size"),
        default=7,
    )
