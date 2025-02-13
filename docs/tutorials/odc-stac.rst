============================
Accessing data with odc-stac
============================

.. note::
   This tutorial is under development

Introduction
============

In this tutorial we will use Python libraries to search for freely available 
Sentinel-2 imagery and load it into memory.

During the tutorial, we will:

* Specify our search in terms of:
  
  * what (data provider and satellite)
  * where (area of interest)
  * when (date range)
* Use `pystac-client`_ to connect to a Spatio-Temporal Asset Catalog (STAC) 
  endpoint and search for data matching our what, where, and when
* Use `odc-stac`_ to load the matching data into memory
* Visualise and export the data

Requirements
------------

.. note::
   At this time, you will need Python 3.9 or higher installed to run this tutorial. 
   In future, this may be replaced with an online environment where you can run the 
   tutorial without needing to install anything.

To run this tutorial on your computer, you will need:

* Python version 3.9 or higher
* A terminal environment to run commands
* A text editor (e.g. VS Code)

We recommend that you use a Python environment manager. 
This tutorial will use `venv`_ which comes with Python, but you may use your preferred 
environment manager. 

Set up
======

Create a virtual environment
----------------------------

#. Open a terminal
#. Create a virtual environment

   .. code-block:: bash

      python -m venv odcstactutorial

#. Activate the virtual environment
  
   * MacOS/Linux

     .. code-block:: bash
  
        source myenv/bin/activate

   * Windows

     .. code-block:: powershell

        myenv\Scripts\activate

#. Install the required packages:

   .. code-block:: bash

      pip install pystac_client
      pip install odc-stac
      pip install ipykernel



.. _pystac-client: https://pystac-client.readthedocs.io/en/stable/
.. _odc-stac: https://odc-stac.readthedocs.io/en/latest/ 
.. _git: https://git-scm.com/
.. _Conda: https://docs.conda.io/projects/conda/en/latest/index.html
.. _Miniconda: https://docs.anaconda.com/miniconda/
.. _GitHub: https://github.com/opendatacube/tutorial-odc-stac/tree/main
