# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


class TopicSliderView(BrowserView):
    """Custom topic view"""

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.translation_service=getToolByName(self.context,'translation_service')

    def createResultsStruct(self,items):
        projects_dict=[]
        if len(items) <= 6:
            projects_dict.append(items)
            return projects_dict
        return [items[x:x+6] for x in range(0, len(items), 6)]

