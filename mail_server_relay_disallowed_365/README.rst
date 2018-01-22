.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License AGPL-3

======================================
Mail server relay disallowed Office365
======================================

Fixes the issue of using a mail client where relaying is disallowed on Office365.

* Office365 server needs to be set up according the following instructions:
	* Enable Relay on Office365 admin panel ((https://advanton.com/guide-office-365-mail-and-odoo-integration/)) or install a postfix relay mail server
	* on Odoo:
		* Set the parameter mail.catchall.alias to the full odoo email address <name@domain.com>
		* set up email-server as usual: smtp.office365.com and set the user login defined in the mail.catchall.alias defiend above
		* remove the parameter mail.catchall.domain



Credits
=======

Contributors
------------

* QubiQ <http://www.qubiq.es>

