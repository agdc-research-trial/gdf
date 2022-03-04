Metadata Types
**************

A Metadata Type defines which fields should be searchable in your product or dataset metadata.

Two metadata types are added by default called ``eo`` and ``eo3``.

You would create a new metadata type if you want custom fields to be searchable for your products, or
if you want to structure your metadata documents differently.

You can see the default metadata type in the repository at ``datacube/index/default-metadata-types.yaml``.

To add or alter metadata types, you can use commands like: ``datacube metadata add <path-to-file>``
and to update: ``datacube metadata update <path-to-file>``. Using ``--allow-unsafe`` will allow
you to update metadata types where the changes may have unexpected consequences.
