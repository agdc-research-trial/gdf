*********************
About & Core Concepts
*********************

Overview
========

The Open Data Cube is a collection of software designed to:

* Index large amounts of Earth observation data, which can be stored on a file system or
  a cloud platform
* Provide a :term:`Python` based :term:`API` for high performance querying and data access
* Give scientists and other users easy ability to perform exploratory data analysis
* Allow continental-scale processing of the stored data
* Track the provenance of all the contained data to allow for quality control and updates

The Open Data Cube software is based around the datacube-core_ library. In addition to this
core library, there are a range of tools that can be installed on top to enable
further capabilities, such as open web services or metadata exploration.

All software in the Open Data Cube project family is released under the `Apache 2.0
<https://github.com/opendatacube/datacube-core/blob/develop/LICENSE>`_ license.


.. figure:: ../diagrams/f1.png
   :name: high-level-overview

   High-Level ODC Overview

.. _datacube-core: https://github.com/opendatacube/datacube-core


The Open Data Cube Software Ecosystem
=====================================

The Open Data Cube is a software ecosystem consisting of a number of Python packages.

The most important packages in the ecosystem are described in the `ODC Software Packages`_
section.

Two packages in particular have overlapping functionality and are worthy of early attention:

.. _`ODC Software Packages`: extensions.html

Datacube-core or odc-stac?
--------------------------

`datacube-core`_ provides many powerful tools and services, however the needs of many new users
can be met more easily with `odc-stac`_.

Both `odc-stac`_ and `datacube-core`_ allow searching collections of earth observation data and loading
it into xarray data structures.  The main differences are in the metadata model that each use
(STAC for `odc-stac`_ and `eo3`_ for `datacube-core`),
and in performing search and discovery via STAC-API endpoints (in the case of `odc-stac`_)
or a relational database (in the case of `datacube-core`_).

If you have access to an ODC database that somebody else
maintains, you probably already have access to an environment with datacube-core installed and configured.
If you want to create and maintain your own ODC database, you will need to install `datacube-core`_.  Most
other use case scenarios should look at `odc-stac`_ first.

This diagram illustrates the relationships between, and highlights the differences between `odc-stac`_ and
`datacube-core`_, as of datacube 1.9:

.. figure:: ../diagrams/odc1.9-arch.png
   :name: high-level-overview

   Datacube-core vs odc-stac

.. _eo3: https://github.com/opendatacube/eo3
.. _odc-stac: https://github.com/opendatacube/odc-stac

Use Cases
=========

The Open Data Cube has a range of uses, including the following:

* **Collection Management:** The ODC can be used as an index to assist in managing a collection
  of Earth observation data, including lineage (parent/child relationships).
* **Exploratory Data Analysis:** Interactive analysis of data, such as through a Jupyter Notebook.
* **Publishing Web Services:** Using the :abbr:`ODC (Open Data Cube)` to serve :abbr:`WMS (Web Map Service)`, :abbr:`WCS (Web Coverage Service)`,
  :abbr:`WPS (Web Processing Service)` or custom tools (such as polygon drill time series analysis).
* **Large-scale workflows on Cloud:** Continental or global-scale processing of data on the cloud
  using XArray and Dask on Kubernetes, for example.
* **Large-scale workflows on HPC:** Continental or global-scale processing of data on a High
  Performance Computing supercomputer cluster.
* **Standalone Applications:** Running environmental analysis applications on a laptop,
  suitable for field work, or outreach to a developing region.

.. toctree::
    :caption: About & Core Concepts

    Overview & Use Cases <self>


.. toctree::
    :caption: Core Concepts

    architecture-guide
    datasets
    products
    metadata-types

.. toctree::
    :caption: Ecosystem

    extensions
    existing-deployments
