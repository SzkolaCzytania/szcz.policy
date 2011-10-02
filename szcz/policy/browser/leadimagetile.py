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
                scale = self.is_home_page and 'carousel' or 'thumb'
                return field.tag(context, scale=scale, css_class=css_class)

        return ''

    @property
    def is_home_page(self):
        return len(self.request.steps) < 4

    def __call__(self):
        return self.template()
