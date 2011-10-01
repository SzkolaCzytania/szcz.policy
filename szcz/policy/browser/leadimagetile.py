from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.contentleadimage.config import IMAGE_FIELD_NAME
from collective.carousel.browser.leadimagetile import LeadImageTile

class BookLeadImageTile(LeadImageTile):

    template = ViewPageTemplateFile('book_carousel_tile.pt')

    def tag(self, css_class='tileImage'):
        """ return a tag for the leadimage"""
        context = aq_inner(self.context)
        field = context.getField(IMAGE_FIELD_NAME)
        if field is not None:
            if field.get_size(context) != 0:
                #scale = self.prefs.body_scale_name
                scale = 'carousel'
                return field.tag(context, scale=scale, css_class=css_class)

        if getattr(context,'tag', None) is not None:
            return context.tag(scale='mini', css_class=css_class)

        return ''

    def __call__(self):
        return self.template()
