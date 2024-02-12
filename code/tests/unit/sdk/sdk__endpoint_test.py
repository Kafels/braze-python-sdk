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
    def test_users_alias_new(self,
                             bearer_auth: MagicMock,
                             requests__request: MagicMock,
                             braze):
        content = MagicMock()
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
        content = MagicMock()
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
        content = MagicMock()
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
        content = MagicMock()
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
        content = MagicMock()
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
        content = MagicMock()
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
        content = MagicMock()
        braze.users.identify(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/identify"
        )

    @patch("sdk.shared.functions.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_track(self,
                         bearer_auth: MagicMock,
                         requests__request: MagicMock,
                         braze):
        content = MagicMock()
        braze.users.track(content=content)

        requests__request.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/track"
        )
