from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from avexado.apps.wiki.models import Page

import re


def view_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
        pattern = r'\_(.*?)\_'
        rep = u'<a href="/wiki/\\1">\\1</a>'
        content = re.sub(pattern, rep, content)
        last_edited_at = page.last_edited_at
    except Page.DoesNotExist:
        return render_to_response('create.html', {'page_name': page_name})

    return render_to_response('view.html', {'page_name': page_name,
                                            'content': content,
                                            'last_edit_time': last_edited_at})


def edit_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
    except Page.DoesNotExist:
        content = ''

    if request.method == 'POST':
        content = request.POST['content']
        page = Page(name=page_name, content=content)
        page.save()

        return HttpResponseRedirect('/wiki/' + page_name + '/')

    return render(request, 'edit.html', {'page_name': page_name,
                                         'content': content})
