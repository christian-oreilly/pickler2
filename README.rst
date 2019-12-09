.. -*- mode: rst -*-

Pickler2
===================================

Small package allowing to decorate a function so that it automatically pickle its results
and load it the next time it is called.

Example of usage
===================================

With the following code, the first time long_function() will be called, it will execute and
save the pickle processed_data. Next time it is run, it will load the pickled object without
running the function.

.. code-block:: python

    from pickler2 import pickled

    @pickled("some_file_name.pck")
    def long_function():
        ... long time to process data ...
        return processed_data

To explicitly re-run the function, you can call

.. code-block:: python

    long_function(run=True)

When using this functionality at different places, within a project, you might want to save
all the pickles at a same place. This can be done by given full name to the decorator

.. code-block:: python

    @pickled("/some/long/path/some_file_name.pck")
    def long_function():
        ... long time to process data ...
        return processed_data

Alternatively, the project pickling path can be registered as follow

.. code-block:: python

    from pickler2 import register_project_path

    register_project_path("my_project", "/some/long/path/")

and then use provide the project name to the constructor:

.. code-block:: python

    @pickled("some_file_name.pck", project_name="my_project")
    def long_function():
        ... long time to process data ...
        return processed_data

The registered pickled path are saved in "~/.pickler_conf.yaml". This allow to run the same code
on different systems with differents path, as long as the corresponding path have been registered
in their respective configuration path.


Why the 2 in Pickler2?
===================================
Because Pickler was already taken on PyPi!

Licensing
^^^^^^^^^

Pickler2 is **BSD-licenced** (3 clause):

    This software is OSI Certified Open Source Software.
    OSI Certified is a certification mark of the Open Source Initiative.

    Copyright (c) 2011-2019, authors of MNE-Python.
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.

    * Neither the names of MNE-Python authors nor the names of any
      contributors may be used to endorse or promote products derived from
      this software without specific prior written permission.

    **This software is provided by the copyright holders and contributors
    "as is" and any express or implied warranties, including, but not
    limited to, the implied warranties of merchantability and fitness for
    a particular purpose are disclaimed. In no event shall the copyright
    owner or contributors be liable for any direct, indirect, incidental,
    special, exemplary, or consequential damages (including, but not
    limited to, procurement of substitute goods or services; loss of use,
    data, or profits; or business interruption) however caused and on any
    theory of liability, whether in contract, strict liability, or tort
    (including negligence or otherwise) arising in any way out of the use
    of this software, even if advised of the possibility of such
    damage.**
