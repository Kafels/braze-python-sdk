from datetime import timedelta

import pytest
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


class TestDecorator(PrepareEnvironment):

    def test_successful_communication(self):
        from sdk.shared.decorator import api

        @api.inject_call(endpoint="/")
        def fake_endpoint(*_, **__):
            def fake_function(*_, **__):
                return MagicMock(ok=True,
                                 status_code=200,
                                 elapsed=timedelta(seconds=1),
                                 content=b'{"hello": "world"}')

            return fake_function

        output = fake_endpoint(MagicMock(braze=MagicMock(host="http://fake.endpoint")))
        assert output == {"hello": "world"}

    def test_failed_connection(self):
        from sdk.shared.decorator import api

        @api.inject_call(endpoint="/")
        def fake_endpoint(*_, **__):
            def fake_function(*_, **__):
                raise Exception("exception msg")

            return fake_function

        with pytest.raises(Exception):
            fake_endpoint(MagicMock(braze=MagicMock(host="http://fake.endpoint")))

    def test_bad_status_code(self):
        from sdk.shared.decorator import api

        response = MagicMock(ok=True,
                             status_code=200,
                             elapsed=timedelta(seconds=1),
                             content=b'{"hello": "world"}')

        response__raise_for_status = response.raise_for_status
        response__raise_for_status.side_effect = [Exception]

        @api.inject_call(endpoint="/")
        def fake_endpoint(*_, **__):
            def fake_function(*_, **__):
                return response

            return fake_function

        with pytest.raises(Exception):
            fake_endpoint(MagicMock(braze=MagicMock(host="http://fake.endpoint")))
