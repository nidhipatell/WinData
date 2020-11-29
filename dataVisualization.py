import pandas as pd
import matplotlib.pyplot as plt
import sys

class DataVisualization():
    def __init__(self, filename) -> None:
        self.filepath = "Iteration I\\testing\\" + filename
        self.getData()
        
    def getData(self):
        self.dataframe = pd.read_excel(self.filepath) if self.filepath[-3:] == "xls" else pd.read_csv(self.filepath)
        self.visualizaeData()
        
    def visualizaeData(self):
        self.dataframe.plot()
        plt.show()

        
    
if __name__ == "__main__":
    file = sys.argv[1]
    data = DataVisualization(file)    
    
