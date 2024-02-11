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

        fake_msg = "Hello world"
        fake_var = {
            "foo": "bar",
            "invalid": InvalidCast()
        }

        timber.info(fake_msg, var=fake_var)

        captured = capfd.readouterr()
        console_content = loads(captured.out)

        location = console_content.pop("location")
        assert re.match(r"\w+>\w+>\d+", location)

        assert console_content == {
            "message": "Hello world",
            "correlation_id": "fake_correlation_id",
            "timestamp": "1970-01-01T00:00:00.000+00:00",
            "var": {"foo": "bar", "invalid": "<non-serializable: InvalidCast>"},
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
