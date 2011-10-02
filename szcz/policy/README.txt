Introduction
============

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.
We use PloneTestCase to set up this test as well, so we have a full Plone site
to play with. We *can* inspect the state of the portal, e.g. using 
self.portal and self.folder, but it is often frowned upon since you are not
treating the system as a black box. Also, if you, for example, log in or set
roles using calls like self.setRoles(), these are not reflected in the test
browser, which runs as a separate session.

Being a doctest, we can tell a story here.

First, we must perform some setup. We use the testbrowser that is shipped
with Five, as this provides proper Zope 2 integration. Most of the 
documentation, though, is in the underlying zope.testbrower package.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> self.portal.error_log._ignored_exceptions = ()

With that in place, we can go to the portal front page and log in. We will
do this using the default user from PloneTestCase:

    >>> from Products.PloneTestCase.setup import portal_owner, default_password

Because add-on themes or products may remove or hide the login portlet, this test will use the login form that comes with plone.  

    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Here, we set the value of the fields on the login form and then simulate a
submit click.  We then ensure that we get the friendly logged-in message:

    >>> "You are now logged in" in browser.contents
    True

Finally, let's return to the front page of our site before continuing

    >>> browser.open(portal_url)

-*- extra stuff goes here -*-

The Review content type
===============================

In this section we are tesing the Review content type by performing
basic operations like adding, updadating and deleting Review content
items.

Adding a new Review content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Review' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Review').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Review' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Review Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Review' content item to the portal.

Updating an existing Review content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Review Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Review Sample' in browser.contents
    True

Removing a/an Review content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Review
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Review Sample' in browser.contents
    True

Now we are going to delete the 'New Review Sample' object. First we
go to the contents tab and select the 'New Review Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Review Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Review
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Review Sample' in browser.contents
    False

Adding a new Review content item as contributor
------------------------------------------------

Not only site managers are allowed to add Review content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Review' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Review').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Review' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Review Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Review content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Canon content type
===============================

In this section we are tesing the Canon content type by performing
basic operations like adding, updadating and deleting Canon content
items.

Adding a new Canon content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Canon' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Canon').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Canon' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Canon Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Canon' content item to the portal.

Updating an existing Canon content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Canon Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Canon Sample' in browser.contents
    True

Removing a/an Canon content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Canon
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Canon Sample' in browser.contents
    True

Now we are going to delete the 'New Canon Sample' object. First we
go to the contents tab and select the 'New Canon Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Canon Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Canon
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Canon Sample' in browser.contents
    False

Adding a new Canon content item as contributor
------------------------------------------------

Not only site managers are allowed to add Canon content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Canon' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Canon').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Canon' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Canon Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Canon content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Person content type
===============================

In this section we are tesing the Person content type by performing
basic operations like adding, updadating and deleting Person content
items.

Adding a new Person content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Person' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Person').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Person' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Person Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Person' content item to the portal.

Updating an existing Person content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Person Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Person Sample' in browser.contents
    True

Removing a/an Person content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Person
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Person Sample' in browser.contents
    True

Now we are going to delete the 'New Person Sample' object. First we
go to the contents tab and select the 'New Person Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Person Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Person
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Person Sample' in browser.contents
    False

Adding a new Person content item as contributor
------------------------------------------------

Not only site managers are allowed to add Person content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Person' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Person').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Person' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Person Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Person content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Book content type
===============================

In this section we are tesing the Book content type by performing
basic operations like adding, updadating and deleting Book content
items.

Adding a new Book content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Book' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Book').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Book' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Book Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Book' content item to the portal.

Updating an existing Book content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Book Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Book Sample' in browser.contents
    True

Removing a/an Book content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Book
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Book Sample' in browser.contents
    True

Now we are going to delete the 'New Book Sample' object. First we
go to the contents tab and select the 'New Book Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Book Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Book
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Book Sample' in browser.contents
    False

Adding a new Book content item as contributor
------------------------------------------------

Not only site managers are allowed to add Book content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Book' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Book').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Book' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Book Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Book content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)



