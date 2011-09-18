"""Definition of the Book content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from szcz.policy.interfaces import IBook
from szcz.policy.config import PROJECTNAME

BookSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

BookSchema['title'].storage = atapi.AnnotationStorage()
BookSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(BookSchema, moveDiscussion=False)


class Book(base.ATCTContent):
    """Szkola Czytania Book"""
    implements(IBook)

    meta_type = "Book"
    schema = BookSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Book, PROJECTNAME)
