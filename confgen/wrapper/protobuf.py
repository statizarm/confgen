from google.protobuf.message import (
    Message,
)

from google.protobuf.reflection import (
    GeneratedProtocolMessageType,
)

from confgen.registry.protobuf import (
    register_wrapper,
)


class WrapperMeta(type):
    def __call__(cls, *args, **kwargs):
        message_cls = getattr(cls, 'MESSAGE', None)
        if message_cls is None:
            raise ValueError(
                'No MESSAGE in message wrapper',
            )
        elif issubclass(message_cls, Message):
            register_wrapper(message_cls.DESCRIPTOR, cls)
        else:
            raise ValueError(
                'WrapperMeta requires Message in MESSAGE field',
            )

        return super(WrapperMeta, cls).__call__(*args, **kwargs)


class Wrapper(metaclass=WrapperMeta):
    def __init__(self):
        pass

    @property
    def _message_cls(self):
        return getattr(self, 'MESSAGE', None)

    def __call__(self, **kwargs):
        if self._message_cls is None:
            return None
        msg = self._message_cls()

        return msg
