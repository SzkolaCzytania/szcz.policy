"""Definition of the Person content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.configuration import zconf

from szcz.policy import policyMessageFactory as _
from szcz.policy.interfaces import IPerson
from szcz.policy.config import PROJECTNAME

PersonSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.TextField('biography',
                    required=True,
                    searchable=True,
                    storage = atapi.AnnotationStorage(migrate=True),
                    validators = ('isTidyHtmlWithCleanup',),
                    default_output_type = 'text/x-html-safe',
                    widget = atapi.RichWidget(
                                 description = '',
                                 label = _(u'label_biography', default=u'Biography'),
                                 rows = 25,
                                 allow_file_upload = zconf.ATDocument.allow_document_upload),
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PersonSchema['title'].storage = atapi.AnnotationStorage()
PersonSchema['title'].widget.label = _(u'label_fullname', default=u'Fullname')
PersonSchema['description'].storage = atapi.AnnotationStorage()
PersonSchema['description'].widget.visible = {'edit': 'hidden', 'view': 'invisible'}

schemata.finalizeATCTSchema(PersonSchema, moveDiscussion=False)


class Person(base.ATCTContent):
    """Person that could be either Author or Person"""
    implements(IPerson)

    meta_type = "Person"
    schema = PersonSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

atapi.registerType(Person, PROJECTNAME)
