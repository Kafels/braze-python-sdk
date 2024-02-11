__all__ = [
    "Formatter",
    "Timber"
]

from aws_lambda_powertools import Logger
from aws_lambda_powertools.logging.formatters.datadog import DatadogLogFormatter


class Formatter(DatadogLogFormatter):
    LOCATION: str = "%(module)s>%(funcName)s>%(lineno)d"
    LOG_RECORD_ORDER: list[str] = [
        "level",
        "service",
        "location",
        "message"
    ]

    def __init__(self,
                 **kwargs):
        super().__init__(
            json_default=kwargs.pop("json_default", self.json_serializer_default),
            location=kwargs.pop("location", self.LOCATION),
            log_record_order=kwargs.pop("log_record_order", self.LOG_RECORD_ORDER),
            utc=kwargs.pop("utc", True),
            **kwargs
        )

    @staticmethod
    def json_serializer_default(value):
        if isinstance(value, bytes):
            return value.decode()

        # noinspection PyBroadException
        try:
            return str(value)
        except Exception:
            return F"<non-serializable: {type(value).__name__}>"


class Timber(Logger):

    def __init__(self, **kwargs):
        super().__init__(
            logger_formatter=kwargs.pop("logger_formatter", Formatter()),
            **kwargs
        )
