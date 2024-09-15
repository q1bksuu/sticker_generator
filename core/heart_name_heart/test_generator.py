import io
from unittest import TestCase

from core.heart_name_heart.generator import generate


class Test(TestCase):
    def test_generate(self):
        for _ in range(100):
            file_io = io.open('./output.jpg', 'wb')
            generate("你好", 5, file_io)
            file_io.close()
