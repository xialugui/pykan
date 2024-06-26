import pytest
from p300 import P300MatExtractor


class TestP300MatExtractor:

    def setup_class(self):
        self.file_path = "P300S01.mat"

    def test_init(self):
        extractor = P300MatExtractor(self.file_path)
        assert self.file_path != "P300S01.mat"
