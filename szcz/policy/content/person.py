"""Definition of the Person content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.Archetypes.utils import getToolByName
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.configuration import zconf

from szcz.policy import policyMessageFactory as _
from szcz.policy.interfaces import IPerson
from szcz.policy.config import PROJECTNAME

PersonSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.TextField('biography',
              required=False,
              searchable=True,
              storage = atapi.AnnotationStorage(migrate=True),
              validators = ('isTidyHtmlWithCleanup',),
              default_output_type = 'text/html',
              widget = atapi.RichWidget(
                        description = '',
                        label = _(u'label_biography', default=u'Biography'),
                        rows = 25,
                        allow_file_upload = zconf.ATDocument.allow_document_upload),
    ),
    atapi.StringField('biography_lead',
                required=True,
                widget=atapi.StringWidget(label=_(u'label_biography_lead', default=u"Biography lead"),
                    description=_(u'help_biography_lead', default=u"Short text lead, best describing the person."),),
                ),

    atapi.StringField('years',
                required=True,
                widget=atapi.StringWidget(label=_(u'label_years', default=u"Years"),
                    description=_(u'help_years', default=u"Year of birth or range of life (birth-death)"),),
                ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PersonSchema['title'].storage = atapi.AnnotationStorage()
PersonSchema['title'].widget.label = _(u'label_fullname', default=u'Fullname')
PersonSchema['description'].storage = atapi.AnnotationStorage()
PersonSchema['description'].widget.visible = {'edit': 'hidden', 'view': 'invisible'}
PersonSchema.moveField('biography', after='title')
PersonSchema.moveField('biography_lead', after='biography')

schemata.finalizeATCTSchema(PersonSchema, moveDiscussion=False)


class Person(base.ATCTContent):
    """Person that could be either Author or Person"""
    implements(IPerson)

    meta_type = "Person"
    schema = PersonSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    def Description(self):
        """ Convert biography to plain text """
        portal_transforms = getToolByName(self, 'portal_transforms')
        data = portal_transforms.convertTo('text/plain', self.getBiography(), mimetype='text/html')
        if data:
            descr = data.getData()
            return '%s...' % (' '.join(descr.split(' ')))

atapi.registerType(Person, PROJECTNAME)
