import datetime
from json import dumps

import pytest
from mock import (
    MagicMock,
    patch
)

BRAZE_HOST = "http://localhost:80"
BRAZE_TOKEN = "token_value"

FAKE_RESPONSE = MagicMock(
    status_code=200,
    elapsed=datetime.timedelta(60),
    content=dumps(dict())
)


class PrepareEnvironment:
    MODULES = [
        "sdk",
        "sdk.__init__",
        "sdk.endpoint",
        "sdk.shared",
        "sdk.shared.__init__",
        "sdk.shared.auth",
        "sdk.shared.decorator",
        "sdk.shared.functions"
    ]

    def setup_method(self):
        self.clean_resources()

    def teardown_method(self):
        self.clean_resources()

    def clean_resources(self):
        import sys
        for module in self.MODULES:
            if module in sys.modules:
                del sys.modules[module]


class TestEndpoint(PrepareEnvironment):

    @pytest.fixture
    def braze(self):
        from sdk import Braze
        return Braze(
            host=BRAZE_HOST,
            token=BRAZE_TOKEN
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_content_blocks_list(self,
                                 bearer_auth: MagicMock,
                                 requests__request: MagicMock,
                                 braze):
        params = {}
        braze.content_blocks.ls(params=params)

        requests__request.assert_called_once_with(
            method="GET",
            params=params,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/content_blocks/list"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_content_blocks_info(self,
                                 bearer_auth: MagicMock,
                                 requests__request: MagicMock,
                                 braze):
        params = {"content_block_id": "value"}
        braze.content_blocks.info(params=params)

        requests__request.assert_called_once_with(
            method="GET",
            params=params,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/content_blocks/info"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_content_blocks_create(self,
                                   bearer_auth: MagicMock,
                                   requests__request: MagicMock,
                                   braze):
        content = {"name": "foobar", "content": "<span>Hello world</span>"}
        braze.content_blocks.create(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/content_blocks/create"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_content_blocks_update(self,
                                   bearer_auth: MagicMock,
                                   requests__request: MagicMock,
                                   braze):
        content = {"content_block_id": "id"}
        braze.content_blocks.update(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/content_blocks/update"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_alias_new(self,
                             bearer_auth: MagicMock,
                             requests__request: MagicMock,
                             braze):
        content = {"user_aliases": [{}]}
        braze.users.alias.new(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/alias/new"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_alias_update(self,
                                bearer_auth: MagicMock,
                                requests__request: MagicMock,
                                braze):
        content = {"alias_updates": [{}]}
        braze.users.alias.update(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/alias/update"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_export_global_control_group(self,
                                               bearer_auth: MagicMock,
                                               requests__request: MagicMock,
                                               braze):
        content = {"fields_to_export": ["field_name"]}
        braze.users.export.global_control_group(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/export/global_control_group"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_export_ids(self,
                              bearer_auth: MagicMock,
                              requests__request: MagicMock,
                              braze):
        content = {}
        braze.users.export.ids(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/export/ids"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_export_segment(self,
                                  bearer_auth: MagicMock,
                                  requests__request: MagicMock,
                                  braze):
        content = {"segment_id": "value", "fields_to_export": ["field_name"]}
        braze.users.export.segment(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/export/segment"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_delete(self,
                          bearer_auth: MagicMock,
                          requests__request: MagicMock,
                          braze):
        content = {}
        braze.users.delete(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/delete"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_identify(self,
                            bearer_auth: MagicMock,
                            requests__request: MagicMock,
                            braze):
        content = {"aliases_to_identify": [{}]}
        braze.users.identify(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/identify"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_merge(self,
                         bearer_auth: MagicMock,
                         requests__request: MagicMock,
                         braze):
        content = {"merge_updates": [{}]}
        braze.users.merge(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/merge"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_track(self,
                         bearer_auth: MagicMock,
                         requests__request: MagicMock,
                         braze):
        content = {}
        braze.users.track(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/track"
        )
