"""Definition of the Person content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
#from Products.ATContentTypes.configuration import zconf

from szcz.policy import policyMessageFactory as _
from szcz.policy.interfaces import IPerson
from szcz.policy.config import PROJECTNAME

PersonSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.StringField('years',
                required=1,
                widget=atapi.StringWidget(label=_(u'label_years', default=u"Years"),
                    description=_(u'help_years', default=u"Year of birth or range of life (birth-death)"),),
                ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PersonSchema['title'].storage = atapi.AnnotationStorage()
PersonSchema['title'].widget.label = _(u'label_fullname', default=u'Fullname')
PersonSchema['description'].storage = atapi.AnnotationStorage()
PersonSchema['description'].widget.label = _(u'label_biography', default=u'Biography')
PersonSchema['description'].widget.rows = 25


schemata.finalizeATCTSchema(PersonSchema, moveDiscussion=False)


class Person(base.ATCTContent):
    """Person that could be either Author or Person"""
    implements(IPerson)

    meta_type = "Person"
    schema = PersonSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

atapi.registerType(Person, PROJECTNAME)
