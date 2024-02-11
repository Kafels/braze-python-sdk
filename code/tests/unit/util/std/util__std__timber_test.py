import re
import uuid
from json import loads

import pytest
from freezegun import freeze_time


class PrepareEnvironment:
    MODULES = [
        "util",
        "util.std",
        "util.std.timber"
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


class InvalidCast:
    def __str__(self):
        raise Exception()


class TestTimber(PrepareEnvironment):

    @freeze_time("1970-01-01")
    def test_console(self, capfd):
        from util.std.timber import Timber

        timber = Timber()

        # Python has an annoying cache, the clear_state() call will remove any appended key created by other unit test
        timber.registered_formatter.clear_state()

        fake_correlation_id = "fake_correlation_id"
        timber.set_correlation_id(fake_correlation_id)

        fake_msg = "An email fake@hotmail.com"
        fake_var = {
            "email": "fake@hotmail.com",
            "invalid": InvalidCast()
        }

        timber.info(fake_msg, var=fake_var)

        captured = capfd.readouterr()
        console_content = loads(captured.out)

        location = console_content.pop("location")
        assert re.match(r"\w+>\w+>\d+", location)

        assert console_content == {
            "message": "An email *e-mail*masked*@hotmail.com",
            "correlation_id": "fake_correlation_id",
            "timestamp": "1970-01-01T00:00:00.000+00:00",
            "var": {"email": "*e-mail*masked*@hotmail.com", "invalid": "<non-serializable: InvalidCast>"},
            "level": "INFO"
        }

    @pytest.mark.parametrize("value, expected_msg", [
        (uuid.uuid5(uuid.NAMESPACE_URL, "hello-world"), "62e71b4a-dc1e-5b38-96f7-7d398968d40b"),
        (b"Binary value", "Binary value"),
        (InvalidCast(), "<non-serializable: InvalidCast>")
    ])
    def test_formatter_deserializer(self, value: object, expected_msg: str):
        from util.std.timber import Formatter
        assert Formatter.json_serializer_default(value) == expected_msg

    @pytest.mark.parametrize("value, expected_msg", [
        (
                {
                    "message": "foo@bar.com"
                },
                {
                    "message": "*e-mail*masked*@bar.com"
                }
        ),
        (
                {
                    "message": "foo@bar.com",
                    "var": {
                        "email": "foo@bar.com"
                    }
                },
                {
                    "message": "*e-mail*masked*@bar.com",
                    "var": {
                        "email": "*e-mail*masked*@bar.com"
                    }
                }
        ),
        (
                {
                    "var": {
                        "address_post_code": "Scranton",
                        "email": "fake@hotmail.com",
                        "first_name": "Mr Pickles",
                        "last_name": "The good boy"
                    }
                },
                {
                    "var": {
                        "address_post_code": "*address*masked*",
                        "email": "*e-mail*masked*@hotmail.com",
                        "first_name": "*name*masked*",
                        "last_name": "*name*masked*"
                    }
                }
        )
    ])
    def test_formatter_mask(self, value: dict, expected_msg: str):
        from util.std.timber import Formatter

        formatter = Formatter()
        formatter.mask(value)

        assert value == expected_msg
