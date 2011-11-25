"""Definition of the Book content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata
from Products.Archetypes.utils import getToolByName
from Products.Archetypes.config import REFERENCE_CATALOG
from archetypes.referencebrowserwidget import ReferenceBrowserWidget

from szcz.policy import policyMessageFactory as _
from szcz.policy.interfaces import IBook
from szcz.policy.config import PROJECTNAME

BookSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    atapi.ReferenceField('authors',
            relationship = 'book_author',
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
                label = _(u'label_book_authors', default=u'Book authors'),
                description = '',
                visible = {'edit' : 'visible', 'view' : 'invisible' }
                )
            ),

    atapi.StringField('pages',
                searchable=1,
                required=0,
                is_duplicates_criterion=True,
                widget=atapi.StringWidget(label=_(u'label_pages', default=u"Pages"),
                    description=_(u'help_pages', default=u"A page number or range of numbers such as '42-111'"),),
                ),

    atapi.StringField('publisher',
                searchable=1,
                required=0,
                widget=atapi.StringWidget(label=_(u'label_publisher',default="Publisher"),
                    description=_(u'help_publisher',default="The publisher's name."),
                    size=60,),
                ),

    atapi.StringField('address',
                searchable=1,
                required=0,
                widget=atapi.StringWidget(label=_('label_address',default=u"Address"),
                    description=_(u'help_address',default=u"Publisher's address. For major publishing houses, just the city is given."),
                    size=60,),
                ),

    atapi.StringField('edition',
                searchable=1,
                required=0,
                widget=atapi.StringWidget(label=_(u'label_edition',default=u"Edition"),
                    description=_(u'help_edition',default=u"The edition of a book - for example: 'II', '2' or 'second', depending on your preference."),
                    size=60,),
                ),

    atapi.StringField('isbn',
                searchable=1,
                widget=atapi.StringWidget(
                    label=_(u'label_isbn',default=u"ISBN Number"),
                    description=_(u'help_isbn',default=u"The ISBN number of this publication."),),
                )
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

BookSchema['title'].storage = atapi.AnnotationStorage()
BookSchema['description'].storage = atapi.AnnotationStorage()
BookSchema['description'].widget.label = _(u'Abstrakt', default=u'Abstract')

schemata.finalizeATCTSchema(BookSchema, folderish=True, moveDiscussion=False)



class Book(folder.ATFolder):
    """Szkola Czytania Book"""
    implements(IBook)

    meta_type = "Book"
    schema = BookSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    def related_people(self):
        authors = self.getAuthors()
        if not authors:
            return [u"Autor nieznany"]
        return [a.Title() for a in authors]

    def allCanons(self):
        reference_catalog = getToolByName(self, REFERENCE_CATALOG)
        references = reference_catalog.getBackReferences(self,
                                                         relationship="canon_book")
        return [ ref.getSourceObject() for ref in references ]

    def getRawRelatedItems(self):
        for author in self.getAuthors():
            yield author.UID()
        for canon in self.allCanons():
            yield canon.UID()


atapi.registerType(Book, PROJECTNAME)
