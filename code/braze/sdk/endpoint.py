from __future__ import annotations

import functools
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from . import Braze

__all__ = [
    "Users"
]

from .shared import (
    api,
    prepare_request
)
from shared.types import DictT


class Endpoint:

    def __init__(self, braze: Braze):
        self.braze = braze


class UsersAlias(Endpoint):

    @api.inject_call(endpoint="/users/alias/new")
    def new(
            self,
            content: DictT,
            **kwargs
    ) -> DictT:
        """Documentation: https://www.braze.com/docs/api/endpoints/user_data/post_user_alias/

        Parameters
        ----------
        content:
        {
          "user_aliases" : (required, array of new user alias object)
        }

        Returns
        -------
        {
          "aliases_processed": 1,
          "message": "success"
        }
        """
        return prepare_request(
            content=content,
            method="POST",
            **kwargs
        )

    @api.inject_call(endpoint="/users/alias/update")
    def update(
            self,
            content: DictT,
            **kwargs
    ):
        """Documentation: https://www.braze.com/docs/api/endpoints/user_data/post_users_alias_update/

        Parameters
        ----------
        content:
        {
          "alias_updates" : (required, array of update user alias object)
        }

        Returns
        -------
        Non-specified in their documentation
        """
        return prepare_request(
            content=content,
            method="POST",
            **kwargs
        )


class UsersExport(Endpoint):

    @api.inject_call(endpoint="/users/export/global_control_group")
    def global_control_group(
            self,
            content: DictT,
            **kwargs
    ) -> DictT:
        """Documentation: https://www.braze.com/docs/api/endpoints/export/user_data/post_users_global_control_group/

        Parameters
        ----------
        content:
        {
          "callback_endpoint" : (optional, string) endpoint to post a download URL to when the export is available,
          "fields_to_export" : (required, array of string) name of user data fields to export, for example, ['first_name', 'email', 'purchases'],
          "output_format" : (optional, string) When using your own S3 bucket, allows to specify file format as 'zip' or 'gzip'. Defaults to zip file format
        }

        Returns
        -------
        {
          "message": (required, string) the status of the export, returns 'success' when completed without errors,
          "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, for example,'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
          "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
        }
        """
        return prepare_request(
            content=content,
            method="POST",
            **kwargs
        )

    @api.inject_call(endpoint="/users/export/ids")
    def ids(
            self,
            content: DictT,
            **kwargs
    ) -> DictT:
        """Documentation: https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier/

        Parameters
        ----------
        content:
        {
          "external_ids": (optional, array of strings) External identifiers for users you wish to export,
          "user_aliases": (optional, array of user alias objects) user aliases for users to export,
          "device_id": (optional, string) Device identifier as returned by various SDK methods such as `getDeviceId`,
          "braze_id": (optional, string) Braze identifier for a particular user,
          "email_address": (optional, string) Email address of user,
          "phone": (optional, string) Phone number of user,
          "fields_to_export": (optional, array of strings) Name of user data fields to export. Defaults to all if not provided
        }

        Returns
        -------
        {
          "message": (required, string) the status of the export, returns 'success' when completed without errors,
          "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
          "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
        }
        """
        return prepare_request(
            content=content,
            method="POST",
            **kwargs
        )

    @api.inject_call(endpoint="/users/export/segment")
    def segment(
            self,
            content: DictT,
            **kwargs
    ) -> DictT:
        """Documentation: https://www.braze.com/docs/api/endpoints/export/user_data/post_users_segment/

        Parameters
        ----------
        content: {
          "segment_id" : (required, string) identifier for the segment to be exported,
          "callback_endpoint" : (optional, string) endpoint to post a download URL when the export is available,
          "fields_to_export" : (required, array of string) name of user data fields to export, you may also export custom attributes. *Beginning April 2021, new accounts must specify specific fields to export.
          "output_format" : (optional, string) when using your own S3 bucket,  specifies file format as 'zip' or 'gzip'. Defaults to ZIP file format
        }

        Returns
        -------
        {
          "message": (required, string) the status of the export, returns 'success' when completed without errors,
          "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, for example, 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
          "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
        }
        """
        return prepare_request(
            content=content,
            method="POST",
            **kwargs
        )


class Users(Endpoint):

    @functools.cached_property
    def alias(self):
        return UsersAlias(self.braze)

    @functools.cached_property
    def export(self):
        return UsersExport(self.braze)

    @api.inject_call(endpoint="/users/delete")
    def delete(
            self,
            content: DictT,
            **kwargs
    ) -> DictT:
        """Documentation: https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/

        Parameters
        ----------
        content: {
          "external_ids" : (optional, array of string) External ids for the users to delete,
          "user_aliases" : (optional, array of user alias objects) User aliases for the users to delete,
          "braze_ids" : (optional, array of string) Braze user identifiers for the users to delete
        }

        Returns
        -------
        {
          "deleted" : (required, integer) number of user ids queued for deletion
        }
        """
        return prepare_request(
            content=content,
            method="POST",
            **kwargs
        )

    @api.inject_call(endpoint="/users/identify")
    def identify(
            self,
            content: DictT,
            **kwargs
    ) -> DictT:
        """Documentation: https://www.braze.com/docs/api/endpoints/user_data/post_user_identify/

        Parameters
        ----------
        content: {
          "aliases_to_identify" : (required, array of alias to identify objects),
          "merge_behavior": (optional, string) one of 'none' or 'merge' is expected
        }

        Returns
        -------
        {
          "aliases_processed": 1,
          "message": "success"
        }
        """
        return prepare_request(
            content=content,
            method="POST",
            **kwargs
        )

    @api.inject_call(endpoint="/users/track")
    def track(
            self,
            content: DictT,
            **kwargs
    ) -> DictT:
        """Documentation: https://www.braze.com/docs/api/endpoints/user_data/post_user_track/

        Parameters
        ----------
        content: {
          "attributes" : (optional, array of attributes object),
          "events" : (optional, array of event object),
          "purchases" : (optional, array of purchase object),
        }

        Returns
        -------
        Successful message with non-fatal errors
        {
          "message" : "success",
          "errors" : [
            {
              <minor error message>
            }
          ]
        }

        Message with fatal errors
        {
          "message" : <fatal error message>,
          "errors" : [
            {
              <fatal error message>
            }
          ]
        }
        """
        return prepare_request(
            content=content,
            method="POST",
            **kwargs
        )
