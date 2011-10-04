"""Definition of the Review content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.configuration import zconf
from archetypes.referencebrowserwidget import ReferenceBrowserWidget

from szcz.policy import policyMessageFactory as _
from szcz.policy.interfaces import IReview
from szcz.policy.config import PROJECTNAME

ReviewSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.TextField('text',
              required=False,
              searchable=True,
              primary=True,
              storage = atapi.AnnotationStorage(migrate=True),
              validators = ('isTidyHtmlWithCleanup',),
              default_output_type = 'text/x-html-safe',
              widget = atapi.RichWidget(
                        description = '',
                        label = _(u'label_body_text', default=u'Body Text'),
                        rows = 25,
                        allow_file_upload = zconf.ATDocument.allow_document_upload),
    ),
    atapi.ReferenceField('author',
            relationship = 'review_author',
            multiValued = False,
            isMetadata = True,
            index = 'KeywordIndex',
            allowed_types= 'Person',
            widget = ReferenceBrowserWidget(
                allow_search = True,
                allow_browse = True,
                allow_sorting = True,
                show_indexes = False,
                force_close_on_insert = True,
                label = _(u'label_review_author', default=u'Review author'),
                description = '',
                visible = {'edit' : 'visible', 'view' : 'invisible' }
                )
            ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ReviewSchema['title'].storage = atapi.AnnotationStorage()
ReviewSchema['description'].storage = atapi.AnnotationStorage()
ReviewSchema['description'].widget.visible = {'edit': 'hidden', 'view': 'invisible'}

schemata.finalizeATCTSchema(ReviewSchema, moveDiscussion=False)


class Review(base.ATCTContent):
    """Book review"""
    implements(IReview)

    meta_type = "Review"
    schema = ReviewSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Review, PROJECTNAME)
