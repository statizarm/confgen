from unittest import (
    TestCase,
)

from confgen.wrapper.protobuf import Wrapper
from .proto.test_create_pb2 import TestMessage


class TestCreateWrapper(TestCase):
    @classmethod
    def create_message_wrapper(cls, message_cls):
        class TestMessageWrapper(Wrapper):
            MESSAGE = message_cls

        return TestMessageWrapper

    @classmethod
    def setUp(cls):
        cls.wrapper_cls = cls.create_message_wrapper(TestMessage)

    def test_crate_empty(self):
        msg = self.wrapper_cls()()

        assert getattr(msg, 'name', None) is not None
        assert getattr(msg, 'id', None) is not None
