1.8 Release Process
*******************

Process for 1.8.x releases after the release of datacube 1.9.0

#. Decide to do a release, and check with regular contributors on `Discord <https://discord.com/invite/4hhBQVas5U>`_ that
   they don't have anything pending.

#. Ensure version pins in setup.py and conda-environment.yml are in sync and up to date.

#. Update the release notes in the ``develop-1.8`` branch via a PR.

#. Create a new **Tag** and **Release** using the `GitHub Releases Web UI`_

   - release from develop-1.8 branch
   - be sure to uncheck "set as latest release".

#. Wait for the `GitHub Action`_ to run and publish the new release to PyPI_

#. Wait for the **conda-forge** bot to notice the new PyPI version and create a PR against
   `the conda-forge datacube feedstock <https://github.com/conda-forge/datacube-feedstock/pulls>`_

#. Merge the `PR created by the conda-forge <https://github.com/conda-forge/datacube-feedstock/pulls>`_ bot to create a
   new `conda-forge release <https://anaconda.org/conda-forge/datacube>`_.

#. Manually update the ``stable-1.8`` branch:

   - git checkout <release tag>
   - git push --force origin stable

#. Post release announcements on Slack, Discord, and social media platforms.

#. Kick back, relax, and enjoy a tasty beverage.

.. _GitHub Releases Web UI: https://github.com/opendatacube/datacube-core/releases
.. _GitHub Action: https://github.com/opendatacube/datacube-core/actions
.. _PyPI: https://pypi.org/project/datacube/
