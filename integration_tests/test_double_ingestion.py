from pathlib import Path

import pytest

from integration_tests.data_utils import generate_test_scenes
from integration_tests.utils import prepare_test_ingestion_configuration

PROJECT_ROOT = Path(__file__).parents[1]

INGESTER_CONFIGS = PROJECT_ROOT / 'docs/config_samples/' / 'ingester'


@pytest.mark.parametrize('datacube_env_name', ('datacube',), indirect=True)
@pytest.mark.usefixtures('default_metadata_type',
                         'indexed_ls5_scene_products')
def test_double_ingestion(clirunner, index, tmpdir, ingest_configs):
    """
    Test for the case where ingestor does not need to create a new product,
    but should re-use an existing target product.

    """
    # Make a test ingestor configuration
    config = INGESTER_CONFIGS / ingest_configs['ls5_nbar_albers']
    config_path, config = prepare_test_ingestion_configuration(tmpdir, None,
                                                               config, mode='fast_ingest')

    index_dataset = lambda path: clirunner(['dataset', 'add', str(path)])

    # Create and Index some example scene datasets
    dataset_paths = generate_test_scenes(tmpdir)
    for path in dataset_paths:
        index_dataset(path)

    # Ingest them
    clirunner([
        'ingest',
        '--config-file',
        str(config_path)
    ])

    # Create and Index some more scene datasets
    dataset_paths = generate_test_scenes(tmpdir)
    for path in dataset_paths:
        index_dataset(path)

    # Make sure that we can ingest the new scenes
    clirunner([
        'ingest',
        '--config-file',
        str(config_path)
    ])
