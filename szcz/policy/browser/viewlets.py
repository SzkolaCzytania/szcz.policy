from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from sc.social.like.browser.viewlets import SocialMetadataViewlet
from collective.contentleadimage.config import IMAGE_FIELD_NAME


class SocialLeadImageMetadataViewlet(SocialMetadataViewlet):
    """Viewlet used to insert metadata into page header
    """
    render = ViewPageTemplateFile("facebook_metadata.pt")

    def getImage(self):
        clfield = self.context.getField(IMAGE_FIELD_NAME)
        if clfield is not None:
            value = clfield.get(self.context)
            if value:
                return '%s/leadImage_tile' % self.context.absolute_url()

        dfield = self.context.getField('image')
        if dfield is not None:
            value = dfield.get(self.context)
            if value:
                return '%s/image_tile' % self.context.absolute_url()

        return '%s/logo.png' % self.context.portal_url()
