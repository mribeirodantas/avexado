from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from avexado.apps.wiki.models import Page


def view_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
    except Page.DoesNotExist:
        return render_to_response('create.html', {'page_name': page_name})

    return render_to_response('view.html', {'page_name': page_name,
                                            'content': content})


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
