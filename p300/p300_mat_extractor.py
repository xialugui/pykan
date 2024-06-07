from scipy import io


class P300MatExtractor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.mat_dict = io.loadmat(file_path)
        self.data = self.mat_dict['data']
