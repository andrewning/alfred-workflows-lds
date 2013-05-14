#!/usr/bin/env python
# encoding: utf-8
"""
verse.py

Created by Andrew Ning on 4/27/2013.
"""

import sys
import requests
from bs4 import BeautifulSoup
import alfred
import re

# get query from user
query = sys.argv[1]
query = query.replace('&', '%26')
titles = []
subtitles = []
args = []

# if ':' not in query or query.endswith(':'):
#     results = [alfred.Item(title="Find a Scripture Verse",
#                            subtitle="searching ...",
#                            attributes={'uid': 'none'},
#                            icon='icon.png')]

#     sys.stdout.write(alfred.xml(results))
#     exit()





# search scriptures
params = {'query': query}
r = requests.get('http://www.lds.org/scriptures/search', params=params)
soup = BeautifulSoup(r.text)

# get versus
verses = soup('p', 'highlight')

if len(verses) == 0:  # keyword search

    list_container = soup.find('ul', 'results-list')

    if list_container is None:  # bad reference
        exit()
    matches = list_container('li')


    for match in matches:
        link = match.h3.a
        name = link.contents[0]
        href = link['href']
        text = u''.join(match.p.snippet.getText())

        # get rid of verse number
        parts = re.split('[0-9]+\s', text, flags=re.UNICODE)
        if len(parts) > 1:
            text = parts[1]

        titles.append(name)
        subtitles.append(text)
        args.append(text + ' (' + name + ')' + '***' + href)



else:  # verses search

    fulltext = ''
    for verse in verses:

        # if multiple verses separate by newline
        if fulltext != '':
            fulltext += '\n'

        # remove study note markers
        [tag.extract() for tag in verse('sup', class_='studyNoteMarker')]

        # extract text
        text = u''.join(verse.getText())

        # clean-up
        text = text.lstrip().rstrip()

        # get rid of verse number
        parts = re.split('[0-9]+\s', text, flags=re.UNICODE)
        if len(parts) > 1:
            text = parts[1]

        # remove paragraph markers
        text = text.replace(u'¶', '')

        # append verses
        fulltext += text


    title = soup.title.string.lstrip().rstrip()

    titles.append(title)
    subtitles.append(fulltext)
    args.append(fulltext + ' (' + title + ')' + '***' + r.url)



# write results in XML format for Alfred
results = []
for title, subtitle, arg in zip(titles, subtitles, args):
    results.append(alfred.Item(title=title,
                               subtitle=subtitle,
                               attributes={'uid': arg.split('***')[-1], 'arg': arg},
                               icon='icon.png'))

sys.stdout.write(alfred.xml(results))



