Autoloader
==========

Python script to reload (re-make) the latest changes when updates are detected.
It was initially designed to rebuild Eliom project after changes is performed.
The script would call the `Makefile` to perform the build process. 
Thus any project with a `Makefile` would be able to use this script.

Dependencies
------------

Autoloader depends on the following libraries to perform its job:

1. [watchdog](http://pythonhosted.org/watchdog/)
2. Subprocess

Contribute
----------

Found a issue or want a feature to be added? 
You could either fork the repository or file and isssue here.
Feedback and question are welcome!
