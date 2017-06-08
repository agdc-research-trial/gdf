from __future__ import absolute_import

import os
import base64
import logging
import click

from datacube.config import LocalConfig
from datacube.index._api import Index
from datacube.ui import click as ui
from datacube.ui.click import cli


_LOG = logging.getLogger('datacube-user')
USER_ROLES = ('user', 'ingest', 'manage', 'admin')


@cli.group(name='user', help='User management commands')
def user_cmd():
    pass


@user_cmd.command('list')
@ui.pass_driver_manager()
def list_users(driver_manager):
    """
    List users
    """
    index = driver_manager.index
    for role, user, description in index.users.list_users():
        click.echo('{0:6}\t{1:15}\t{2}'.format(role, user, description if description else ''))
    driver_manager.close()


@user_cmd.command('grant')
@click.argument('role',
                type=click.Choice(USER_ROLES),
                nargs=1)
@click.argument('users', nargs=-1)
@ui.pass_driver_manager()
def grant(driver_manager, role, users):
    """
    Grant a role to users
    """
    index = driver_manager.index
    index.users.grant_role(role, *users)
    driver_manager.close()


@user_cmd.command('create')
@click.argument('role',
                type=click.Choice(USER_ROLES), nargs=1)
@click.argument('user', nargs=1)
@click.option('--description')
@ui.pass_driver_manager()
@ui.pass_config
def create_user(config, driver_manager, role, user, description):
    # type: (LocalConfig, Index, str, str, str) -> None
    """
    Create a User
    """
    index = driver_manager.index
    password = base64.urlsafe_b64encode(os.urandom(12)).decode('utf-8')
    index.users.create_user(user, password, role, description=description)

    click.echo('{host}:{port}:*:{username}:{password}'.format(
        host=config.db_hostname or 'localhost',
        port=config.db_port,
        username=user,
        password=password
    ))
    driver_manager.close()


@user_cmd.command('delete')
@click.argument('users', nargs=-1)
@ui.pass_driver_manager()
@ui.pass_config
def delete_user(config, driver_manager, users):
    """
    Delete a User
    """
    index = driver_manager.index
    index.users.delete_user(*users)
    driver_manager.close()
