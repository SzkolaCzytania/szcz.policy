import sys;sys.stdout=file('/dev/stdout','w')

#Patch stupid collective.dancing composer which cannot be change with z3c.jbot!
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from collective.dancing import composer
composer.HTMLComposer.confirm_template = ViewPageTemplateFile('browser/composer-html-confirm.pt')
composer.HTMLComposer.forgot_template = ViewPageTemplateFile('browser/composer-html-forgot.pt')
