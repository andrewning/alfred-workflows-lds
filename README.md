alfred-workflows-lds
====================

A collection of [Alfred v2](http://www.alfredapp.com) workflows using resources from The Church of Jesus Christ of Latter-day Saints (Mormons).  Use of workflows requires the Alfred PowerPack.

- [LDS Scripture Search](#lds-scripture-search): find a verse(s) by reference or keyword, then copy to clipboard.
- [Mormon Channel](#mormon-channel): Stream Mormon Channel radio through iTunes (Mormon Channel, Music channel, or Canal Mormón).  Allows you to use keyboard buttons (or Alfred keywords) to play/pause rather than navigating through a browser.


LDS Scripture Search
--------------------

![](screenshots/scripture.tiff)

**verse "reference"**

Lookup a verse(s) by reference using [LDS Scriptures](http://www.lds.org/scriptures?lang=eng).  Includes any scripture in the Old Testament, New Testament, Book of Mormon, Doctrine & Covenants, or Pearl of Great Price.  You can even given a range of verses (e.g., "verse d&c 121:39-43").  Action the item to copy it to the clipboard, it also pastes it automatically into the front most app although you can deselect that option if you like.  I like to use this workflow when writing a talk or taking notes in a journal.  The clipboard copy is careful to remove footnote markers or other markup that you get when copy/pasting from the actual website so that you just get the verse.

**verse "keyword"**

Lookup matching verses by keyword (or phrase).  For example "verse patience" will find scriptures with the word patience in it.

**verse "reference" [cmd]**

For both cases you can hold down cmd to open the verse in your browser rather than copy it to the clipboard.


#### [[Download LDS Scripture Search Workflow](https://github.com/andrewning/alfred-workflows-lds/raw/master/lds-scripture-search/LDS%20Scripture%20Search.alfredworkflow)]


Mormon Channel
--------------

![](screenshots/mormonchnl.tiff)

**mormonchnl**

This is a simple workflow that allows you to stream the [Mormon Channel](http://www.mormonchannel.org) radio using iTunes.  I like listening to the music stream at work sometimes when I'm tired of Pandora and I find it a pain to switch over to the browser and navigate through your tabs just to play/pause the stream.  Because the workflow uses iTunes, the Play/Pause buttons on your keyboard work to play/pause the stream (can also use play/pause keywords in Alfred if you like).  The workflow allows you to choose between the normal Mormon Channel, the Music channel, and Canal Mormón.

#### [[Download Mormon Channel Workflow](https://github.com/andrewning/alfred-workflows-lds/raw/master/lds-mormon-channel/Mormon%20Channel.alfredworkflow)]


Acknowledgments
---------------

The following packages/modules are used within these workflows:

- [Requests](http://docs.python-requests.org/en/latest/), an HTTP library written in Python.
- [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/), a Python library for parsing HTML
- [alfred-python](https://github.com/nikipore/alfred-python), a lightweight wrapper to Alfred's workflow API

License
-------

This repository is not sponsored by nor endorsed by The Church of Jesus Christ of Latter-day Saints.

Copyright (c) 2013, S. Andrew Ning.  All rights reserved.

All code is licensed under [The MIT License](http://opensource.org/licenses/mit-license.php).
