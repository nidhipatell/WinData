import pandas as pd
import matplotlib.pyplot as plt
import sys

class DataVisualization():
    def __init__(self, filename) -> None:
        self.filepath = "Iteration I\\testing\\" + filename
        self.getData()
        
    def getData(self):
        self.dataframe = pd.read_excel(self.filepath) if self.filepath[-3:] == "xls" else pd.read_csv(self.filepath)
        candidates = self.dataframe["Candidate"].unique()
        print(candidates)
        candidates = dict.fromkeys(candidates, 0)
        
        #print(self.dataframe)
        
        for index, row in self.dataframe.iterrows():
            candidate_name = row["Candidate"]
            candidates[candidate_name] += row["Total"]
        
        print(candidates)
            
        self.newdf = pd.DataFrame.from_dict(candidates, orient='index')
        print(self.newdf)
        
        self.visualizaeData()
        
    def visualizaeData(self):
        self.newdf.plot(kind="bar")
        plt.show()

        
    
if __name__ == "__main__":
    file = "OfficialElection2010.xls"
    data = DataVisualization(file)    
    
