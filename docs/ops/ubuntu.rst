======
Ubuntu
======

Required software
-----------------

HDF5, and netCDF4::

   apt-get install libhdf5-serial-dev libnetcdf-dev

GDAL::

    apt-get install libgdal1-dev

Optional packages (useful utilities, docs)::

    apt-get install postgresql-doc-9.5 libhdf5-doc netcdf-doc libgdal1-doc
    apt-get install hdf5-tools netcdf-bin gdal-bin pgadmin3



Python and packages
-------------------

Python 2.7 and 3.5+ are supported.

Download the latest version of the software from the `repository <https://github.com/opendatacube/datacube-core>`_ and install it::

    git clone https://github.com/opendatacube/datacube-core
    cd datacube-core
    git checkout develop
    python setup.py install


It may be useful to use conda to install binary packages::

    conda install psycopg2 gdal libgdal hdf5 rasterio netcdf4 libnetcdf pandas

.. note::

    Usage of virtual environments is recommended
