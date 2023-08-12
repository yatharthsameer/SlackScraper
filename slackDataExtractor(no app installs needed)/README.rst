============
Slack Data Extractor
============


To run:

1. Extract Data:

`` ./slackdump``

2. Parse data:

`` python parse.py ``

























Description
===========

Purpose: dump Slack messages, users, files and emojis using browser token and
cookie.

Typical use scenarios:

* archive your private conversations from Slack when the administrator
  does not allow you to install applications OR you don't want to use
  potentially privacy-violating third-party tools,
* archive channels from Slack when you're on a free "no archive" subscription,
  so you don't lose valuable knowledge in those channels,
* create a Slack Export archive without admin access, or
* save your favourite emojis.

There a three modes of operation (more on this in `User Guide`_) :

#. List users/channels
#. Dumping messages and threads
#. Creating a Slack Export in Mattermost or Standard modes.
#. Emoji download mode.

Slackdump accepts two types of input (see `Dumping Conversations`_ section):

#. the URL/link of the channel or thread, OR
#. the ID of the channel.


Quick Start
===========

#. Download the latest release for your operating system from the releases_
   page. (If you're using **macOS**, download **Darwin** executable).
#. Unpack the archive to any directory.
#. Run the ``./slackdump`` or ``slackdump.exe`` executable (see note below).
#. You know the drill:  use arrow keys to select the menu item, and Enter (or
   Return) to confirm.

By default, Slackdump uses the EZ-Login 3000 automatic login, and interactive
mode.

.. NOTE::
  On Windows and macOS you may be presented with "Unknown developer" window,
  this is fine.  Reason for this is that the executable hasn't been signed by
  the developer certificate.

  To work around this:

  - **on Windows**: click "more information", and press "Run
    Anyway" button.
  - **on macOS**: open the folder in Finder, hold Option and double click the
    executable, choose Run.



User Guide
==========

For more advanced features and instructions, please see the `User Guide`_.

Previewing Results
==================

Once the data is dumped, you can use one of the following tools to preview the
results:

- `SlackLogViewer`_ - a fast and powerful Slack Export viewer written in C++.
- `Slackdump2Html`_ - a great Python application that converts Slack Dump to a
  static browsable HTML, works on Dump mode files.
- `slack export viewer`_ - Slack Export Viewer is a well known viewer for
  slack export files.


FAQ
===

:Q: **Do I need to create a Slack application?**

:A: No, you don't.  Just run the application and EZ-Login 3000 will take
    care of the authentication or, alternatively, grab that token and
    cookie from the browser Slack session.  See `User Guide`_.

:Q: **I'm getting "invalid_auth" error**

:A: Go get the new Cookie from the browser and Token as well.

:Q: **Slackdump takes a very long time to cache users**

:A: Disable the user cache with ``-no-user-cache`` flag.

:Q: **How to read the export file?**

:A: For Slack Workspace Export, use SlackLogViewer_ which is extremely fast
    with an advanced search function, or `slack export viewer`_ which is a
    Python application and runs in a browser.  For the generic dump files, see
    `examples`_ directory for some python and shell examples.

:Q: **My Slack Workspace is on the Free plan.  Can I get data older than
    90-days?**

:A: No, unfortunately you can't.  Slack doesn't allow to export data older
    than 90 days for free workspaces, the API does not return any data before 90
    days for workspaces on the Free plan.

