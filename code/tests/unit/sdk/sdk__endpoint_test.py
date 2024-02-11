import datetime
from json import dumps

import pytest
from mock import (
    MagicMock,
    patch
)

BRAZE_TOKEN = "token_value"
BRAZE_HOST = "http://localhost:80"
BRAZE_TIMEOUT = 10.0

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

    @patch("sdk.endpoint.requests.request", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_alias_new(self,
                             bearer_auth: MagicMock,
                             requests__post: MagicMock,
                             braze):
        content = MagicMock()
        braze.users.alias.new(content=content)

        requests__post.assert_called_once_with(
            method="POST",
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/alias/new",
            timeout=BRAZE_TIMEOUT
        )

    @patch("sdk.endpoint.requests.post", return_value=FAKE_RESPONSE)
    @patch("sdk.shared.decorator.BearerAuth")
    def test_users_export_ids(self,
                              bearer_auth: MagicMock,
                              requests__post: MagicMock,
                              braze):
        content = MagicMock()
        braze.users.export.ids(content=content)

        requests__post.assert_called_once_with(
            json=content,
            auth=bearer_auth.return_value,
            url=F"{BRAZE_HOST}/users/export/ids",
            timeout=BRAZE_TIMEOUT
        )

    @pytest.fixture
    def braze(self):
        from sdk import Braze
        return Braze(
            token=BRAZE_TOKEN,
            host=BRAZE_HOST,
            timeout=BRAZE_TIMEOUT
        )
