.. AssertWT documentation master file, created by sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

AssertWT
~~~~~~~~

Assert that a Python script is run in the Windows Terminal 'wt.exe' instead
of the standard 'conhost.exe' console.

.. code-block:: python

    >>> import assertwt
    >>> assertwt.restart()

By default the script is run with cmd.exe and the window is closed when the
script ends.

.. code-block:: python

    # Default behaviour: cmd.exe and window closes after script:
    assertwt.restart(["wt", "-d", assertwt.CD, "cmd", "/C", assertwt.ARGV])

    # cmd.exe and windows does not close after script:
    assertwt.restart(["wt", "-d", assertwt.CD, "cmd", "/K", assertwt.ARGV])

    # Powershell and window closes after script:
    assertwt.restart(["wt", "-d", assertwt.CD, "powershell", "-Command", assertwt.ARGV])

    # Powershell and windows does not close after script:
    assertwt.restart(["wt", "-d", assertwt.CD, "powershell", "-NoExit", "-Command", assertwt.ARGV])

    # New tab in existing Windows Terminal window:
    assertwt.restart(["wt", "new-tab", "-d", assertwt.CD, "cmd", "/K", assertwt.ARGV])

..

Install
-------

`pip install assertwt`

See: https://pypi.org/project/assertwt/

Functions
=========
.. currentmodule:: assertwt
.. autofunction:: restart
.. autofunction:: ARGV
.. autofunction:: CD

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
