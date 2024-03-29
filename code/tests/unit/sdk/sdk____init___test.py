from mock import (
    patch
)

BRAZE_HOST = "http://localhost:80"
BRAZE_TOKEN = "token_value"


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


class TestBraze(PrepareEnvironment):

    def test_instance(self):
        from sdk import Braze

        braze = Braze(
            host=BRAZE_HOST,
            token=BRAZE_TOKEN
        )

        assert getattr(braze, "token") == BRAZE_TOKEN
        assert getattr(braze, "host") == BRAZE_HOST

    @patch("sdk.Users")
    def test_user(self, users):
        from sdk import Braze

        braze = Braze(
            host=BRAZE_HOST,
            token=BRAZE_TOKEN
        )

        assert braze.users == users.return_value
        assert braze.users == users.return_value

        users.assert_called_once_with(braze)
