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
   We may replace this section with instructions for a GitHub code space or Binder to allow people to 
   run the tutorial without managing their own local environment.

The tutorial materials are available on `GitHub`_ 

To run this tutorial on your computer, you will need:

- Conda: Miniconda or Anaconda: A Python distribution for managing environments.

.. _GitHub: https://github.com/opendatacube/tutorial-odc-stac/tree/main
