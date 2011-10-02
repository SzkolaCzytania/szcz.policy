"""Definition of the Canon content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from archetypes.referencebrowserwidget import ReferenceBrowserWidget

from szcz.policy import policyMessageFactory as _
from szcz.policy.interfaces import ICanon
from szcz.policy.config import PROJECTNAME

CanonSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.ReferenceField('authors',
            relationship = 'canon_author',
            multiValued = True,
            isMetadata = True,
            index = 'KeywordIndex',
            allowed_types= 'Person',
            widget = ReferenceBrowserWidget(
                allow_search = True,
                allow_browse = True,
                allow_sorting = True,
                show_indexes = False,
                force_close_on_insert = False,
                label = _(u'label_canon_authors', default=u'Canon authors'),
                description = '',
                visible = {'edit' : 'visible', 'view' : 'invisible' }
                )
            ),

    atapi.ReferenceField('books',
            relationship = 'canon_book',
            multiValued = True,
            isMetadata = True,
            index = 'KeywordIndex',
            allowed_types= 'Book',
            widget = ReferenceBrowserWidget(
                allow_search = True,
                allow_browse = True,
                allow_sorting = True,
                show_indexes = False,
                force_close_on_insert = False,
                label = _(u'label_canon_books', default=u'Canon books'),
                description = '',
                visible = {'edit' : 'visible', 'view' : 'invisible' }
                )
            ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CanonSchema['title'].storage = atapi.AnnotationStorage()
CanonSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(CanonSchema, moveDiscussion=False)


class Canon(base.ATCTContent):
    """Book's Canon"""
    implements(ICanon)

    meta_type = "Canon"
    schema = CanonSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Canon, PROJECTNAME)
