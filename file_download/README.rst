.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=============
File Download
=============

Let's you call a wizard to download any file.

Configuration
=============

Install the module.

Usage
=====

Create a model that inherits from file.download.model.
Override the following functions:
    "get_filename" to make it return the desired file name.
    "get_content" to return the binary string file to download. For example:
	    output = StringIO()
	    file.save(output)
	    output.seek(0)
	    return output.read()
After this, create a wizard with a button that calls the function set_file.
This function will open a new wizard with the downloadable file.



Credits
=======

Contributors
------------

* Valentin Vinagre <valentin.vinagre@qubiq.es>
* Oscar Navarro <oscar.navarro@qubiq.es>

Maintainer
----------

This module is maintained by Qubiq.
