from mock import (
    MagicMock
)

TOKEN = "token_value"


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


class TestAuth(PrepareEnvironment):

    def test_bearer_auth(self):
        from sdk.shared.auth import BearerAuth

        bearer = BearerAuth(token=TOKEN)

        mock = MagicMock()
        mock.headers = dict()

        output = bearer(mock)

        assert output.headers["authorization"] == F"Bearer {TOKEN}"
