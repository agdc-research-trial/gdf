# coding=utf-8
"""
User configuration.
"""
from __future__ import absolute_import

import os

from . import compat

ENVIRONMENT_VARNAME = 'DATACUBE_CONFIG_PATH'
#: Config locations in order. Properties found in latter locations override
#: earlier ones.
#:
#: - `/etc/datacube.conf`
#: - file at `$DATACUBE_CONFIG_PATH` environment variable
#: - `~/.datacube.conf`
#: - `datacube.conf`
DEFAULT_CONF_PATHS = (
    '/etc/datacube.conf',
    os.environ.get(ENVIRONMENT_VARNAME),
    os.path.expanduser("~/.datacube.conf"),
    'datacube.conf'
)

DEFAULT_ENV = 'default'

# Default configuration options.
_DEFAULT_CONF = u"""
[DEFAULT]
# Blank implies localhost
db_hostname:
db_database: datacube
# If a connection is unused for this length of time, expect it to be invalidated.
db_connection_timeout: 60

[user]
# Which environment to use when none is specified explicitly.
# 'datacube' was the config section name before we had environments; it's used here to be backwards compatible.
default_environment: datacube
"""

#: Used in place of None as a default, when None is a valid but not default parameter to a function
_UNSET = object()


class LocalConfig(object):
    """
    System configuration for the user.

    This loads from a set of possible configuration files which define the available environments.
    An environment contains connection details for a Data Cube Index, which provides access to
    available data.

    """

    def __init__(self, config, files_loaded=None, env=None):
        self._config = config  # type: configparser.ConfigParser
        self.files_loaded = []
        if files_loaded:
            self.files_loaded = files_loaded  # type: list[str]

        # If the user specifies a particular env, we either want to use it or Fail
        if env:
            if config.has_section(env):
                self._env = env
                # All is good
                return
            else:
                raise ValueError('No config section found for environment %r' % (env,))
        else:
            # If an env hasn't been specifically selected, we can fall back to an env var or a default
            fallbacks = [os.environ.get('DATACUBE_ENVIRONMENT'), DEFAULT_ENV, 'datacube']
            for fallback_env in fallbacks:
                if config.has_section(fallback_env):
                    self._env = fallback_env
                    return
            raise ValueError('No ODC environment, checked configurations for %s' % fallbacks)

    @classmethod
    def find(cls, paths=DEFAULT_CONF_PATHS, env=None):
        """
        Find config from possible filesystem locations.

        'env' is which environment to use from the config: it corresponds to the name of a
        config section

        :type paths: str|list[str]
        :type env: str
        :rtype: LocalConfig
        """
        if isinstance(paths, str) or hasattr(paths, '__fspath__'):  # Use os.PathLike in 3.6+
            paths = [paths]
        config = compat.read_config(_DEFAULT_CONF)
        files_loaded = config.read(str(p) for p in paths if p)

        return LocalConfig(
            config,
            files_loaded=files_loaded,
            env=env,
        )

    def get(self, item, fallback=_UNSET):
        if fallback == _UNSET:
            return self._config.get(self._env, item)
        else:
            return self._config.get(self._env, item, fallback=fallback)

    def __getitem__(self, item):
        return self._config.get(self._env, item, fallback=None)

    def __str__(self):
        return "LocalConfig<loaded_from={}, environment={!r}, config={}>".format(
            self.files_loaded or 'defaults',
            self._env,
            dict(self._config[self.env]),
        )

    def __repr__(self):
        return str(self)


OPTIONS = {'reproject_threads': 4}


#: pylint: disable=invalid-name
class set_options(object):
    """Set global state within a controlled context

    Currently, the only supported options are:
    * reproject_threads: The number of threads to use when reprojecting

    You can use ``set_options`` either as a context manager::

        with datacube.set_options(reproject_threads=16):
            ...

    Or to set global options::

        datacube.set_options(reproject_threads=16)
    """

    def __init__(self, **kwargs):
        self.old = OPTIONS.copy()
        OPTIONS.update(kwargs)

    def __enter__(self):
        return

    def __exit__(self, exc_type, value, traceback):
        OPTIONS.clear()
        OPTIONS.update(self.old)
