Fuzzy Penguin: Project Design
=============================

**Summary**: Fuzzy Penguin is a simple web fuzzer written in python.

.. contents::
    :depth: 2
    :backlinks: top
    :local:

Quick Start
-----------

* Clone the project (or download a zip archive)
* pip install -r requirements
* Run setup.py develop

Contacts
--------

* Lead developer: David Albone (https://github.com/dpauk)

Specifications
--------------

MVP
* Have a hardcoded string list stored in a file (downloaded from https://github.com/danielmiessler/SecLists)
* Just allow fuzzing of a GET
* Use a special character to specify the fuzzing position
* Present results on a screen

Backlog:
* Fuzzing of POST requests
* Specifying a file containing a list of the strings used for fuzzing
* Display results on a web page
* Allow creation of reports
* Create json with results
* Allow multiple lists and multiple insertion points
* Allow different attack types (e.g. sniper, battering ram, pitchfork, cluster bomb) as in Burp
* Allow rate limiting
* Add logging
* Allow a file of URLs to be specifed
* Allow a directory of POST requests to be specified
* Create a front-end
* Allow an admin who can control the software and allowable endpoints (both whitelists and blacklists)
* Allow for saving of results and reload per user
* Allow the specification of a restriction file to stop production services being attacked (admin only?)
* Add monitoring
* Allow times to be specified for fuzzer to run
* Provide alerting for specific events
* Make it compatible with a CI process (Jenkins plugin?)