.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================
Popup notifications mail (Beta)
=========================

This module performs a popup in the download and assignment of emails of each user.
* Each popup is performed every 3 minutes.
* Each popup is independent for each browser window.
* There is a cron that creates the notifications called: Creacion de notificaciones de correo
* In order for the popup to be made, click on "Ok"

Configuration
=============

Install the module and verify that the configuration parameter
(Configuration-> parameters-> system parameters) has
The address: web port followed by/web # eg:
Http://localhost:8069/web#

Known issues / Roadmap
======================

* In some cases it does not allocate well the popups

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/QubiQ/qubiq-addons/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Contributors
------------

* Valentin Vinagre <valentin.vinagre@qubiq.es>

