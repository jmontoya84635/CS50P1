from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def searchResult(request, title):
    # Checks if there is a result for search
    result = util.get_entry(title)
    isFound = False
    if result is not None:
        isFound = True

    # Returns Title, if it was found, and, metadata
    return render(request, "encyclopedia/searchResult.html", {
        "title": title.capitalize(),
        "isFound": isFound,
        # fixme: fix the the title showing up in information about the topic
        "result": result,
    })


def searchBar(request):
    # Grabs the q parameter from the get request and does the same as previous func
    search = request.GET.get('q')
    result = util.get_entry(search)
    isFound = False
    subStringEntries = []
    if result is not None:
        isFound = True
    else:
        allEntries = util.list_entries()
        for entry in allEntries:
            if search.lower() in entry.lower():
                subStringEntries.append(entry)

    return render(request, "encyclopedia/searchResult.html", {
        "title": search.capitalize(),
        "isFound": isFound,
        # fixme: fix the the title showing up in information about the topic
        "result": result,
        "foundRelated": False if (len(subStringEntries) == 0) else True,
        "relatedEntries": subStringEntries,

    })
