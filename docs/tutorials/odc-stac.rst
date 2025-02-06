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

- Specify our data search in terms of:
  
  - what (data provider and satellite)
  - where (area of interest)
  - when (date range)
- Use `pystac-client` to connect to a Spatio-Temporal Asset Catalog (STAC) 
  endpoint and search for data matching our what, where, and when
- Use `odc-stac` to load the matching data into memory
- Visualise and export the data

Prepare the tutorial environment
================================

.. note::
   At this time, you will need working knowledge of git and Conda to run this tutorial
   on your own computer. 
   In future, this may be replaced with an online environment where you can run the 
   tutorial without needing to install anything.

To run this tutorial on your computer, you will need:

- `git`_: Software for version control.
- `Conda`_: Software for managing Python packages and environments. 
  We recommend `Miniconda`_.

Check out tutorial materials
----------------------------

The tutorial materials are available on `GitHub`_



.. _git: https://git-scm.com/
.. _Conda: https://docs.conda.io/projects/conda/en/latest/index.html
.. _Miniconda: https://docs.anaconda.com/miniconda/
.. _GitHub: https://github.com/opendatacube/tutorial-odc-stac/tree/main
