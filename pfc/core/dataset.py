# pfc/core/dataset.py
import pandas as pd

class Dataset:
    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(path)

    def head(self, n=5):
        return self.df.head(n).copy()

    def tail(self, n=5):
        return self.df.tail(n)

    def columns(self):
        return list(self.df.columns)

    def describe(self):
        return self.df.describe

    def size(self):
        return self.df.size

    def index(self):
        return self.df.index
