from datacube import Datacube
from datacube.api.query import query_group_by
import numpy as np
from collections import Sequence
from types import SimpleNamespace

from pathlib import Path
from datacube.testutils import (
    mk_sample_dataset,
    mk_test_image,
)
from datacube.testutils.io import write_gtiff, rio_slurp


def gen_tiff_dataset(bands,
                     base_folder,
                     prefix='',
                     timestamp='2018-07-19',
                     **kwargs):
    """
       each band:
         .name    - string
         .values  - ndarray
         .nodata  - numeric|None

    :returns:  (Dataset, GeoBox)
    """
    if not isinstance(bands, Sequence):
        bands = (bands,)

    # write arrays to disk and construct compatible measurement definitions
    gbox = None
    mm = []
    for band in bands:
        name = band.name
        fname = prefix + name + '.tiff'
        meta = write_gtiff(base_folder/fname, band.values,
                           nodata=band.nodata,
                           overwrite=True,
                           **kwargs)

        gbox = meta['gbox']

        mm.append(dict(name=name,
                       path=fname,
                       layer=1,
                       dtype=meta['dtype']))

    uri = Path(base_folder/'metadata.yaml').absolute().as_uri()
    ds = mk_sample_dataset(mm, uri=uri, timestamp=timestamp)
    return ds, gbox


def test_load_data(tmpdir):
    tmpdir = Path(str(tmpdir))

    group_by = query_group_by('time')
    spatial = dict(resolution=(15, -15),
                   offset=(11230, 1381110),)

    nodata = -999
    aa = mk_test_image(96, 64, 'int16', nodata=nodata)

    ds, gbox = gen_tiff_dataset([SimpleNamespace(name='aa', values=aa, nodata=nodata)],
                                tmpdir,
                                prefix='ds1-',
                                timestamp='2018-07-19',
                                **spatial)
    assert ds.time is not None

    ds2, _ = gen_tiff_dataset([SimpleNamespace(name='aa', values=aa, nodata=nodata)],
                              tmpdir,
                              prefix='ds2-',
                              timestamp='2018-07-19',
                              **spatial)
    assert ds.time is not None
    assert ds.time == ds2.time

    sources = Datacube.group_datasets([ds], group_by)
    sources2 = Datacube.group_datasets([ds, ds2], group_by)

    mm = ['aa']
    mm = [ds.type.measurements[k] for k in mm]

    ds_data = Datacube.load_data(sources, gbox, mm)
    assert ds_data.aa.nodata == nodata
    np.testing.assert_array_equal(aa, ds_data.aa.values[0])

    custom_fuser_call_count = 0

    def custom_fuser(dest, delta):
        nonlocal custom_fuser_call_count
        custom_fuser_call_count += 1
        dest[:] += delta

    ds_data = Datacube.load_data(sources2, gbox, mm, fuse_func=custom_fuser)
    assert ds_data.aa.nodata == nodata
    assert custom_fuser_call_count > 0
    np.testing.assert_array_equal(nodata + aa + aa, ds_data.aa.values[0])


def test_rio_slurp(tmpdir):
    w, h, dtype, nodata, ndw = 96, 64, 'int16', -999, 7

    pp = Path(str(tmpdir))

    aa = mk_test_image(w, h, dtype, nodata, nodata_width=ndw)

    assert aa.shape == (h, w)
    assert aa.dtype.name == dtype
    assert aa[10, 30] == (30 << 8) | 10
    assert aa[10, 11] == nodata

    aa0 = aa.copy()
    mm = write_gtiff(pp/"rio-slurp-aa.tif", aa, nodata=-999, overwrite=True)
    mm = SimpleNamespace(**mm)

    aa, _ = rio_slurp(mm.path)
    np.testing.assert_array_equal(aa, aa0)

    aa, _ = rio_slurp(mm.path, aa0.shape)
    np.testing.assert_array_equal(aa, aa0)

    aa, _ = rio_slurp(mm.path, mm.gbox)
    np.testing.assert_array_equal(aa, aa0)

    aa, _ = rio_slurp(mm.path, gbox=mm.gbox, dtype='float32')
    assert aa.dtype == 'float32'
    np.testing.assert_array_equal(aa, aa0.astype('float32'))

    aa, _ = rio_slurp(mm.path, mm.gbox, dst_nodata=-33)
    np.testing.assert_array_equal(aa == -33, aa0 == -999)
