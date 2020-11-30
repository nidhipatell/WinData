from flask import Flask, render_template, jsonify, Response
import io, random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/datasets/')
def datasets():
    return render_template("opendata.html")

@app.route('/datasets/election2010/')
def election2010():
    return render_template("election2010.html")

@app.route('/datasets/election2010/vizualize', methods=['GET'])
def election2020Vizualize():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    print("HI")
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    filepath = "Iteration I\\testing\\OfficialElection2010.xls"
    dataframe = pd.read_excel(filepath) if filepath[-3:] == "xls" else pd.read_csv(filepath)
    candidates = dataframe["Candidate"].unique()
    candidates = dict.fromkeys(candidates, 0)
    for index, row in dataframe.iterrows():
        candidate_name = row["Candidate"]
        candidates[candidate_name] += row["Total"]
    newdf = pd.DataFrame.from_dict(candidates, orient='index')
    # fig = Figure.add_subplot(newdf.plot(kind="bar"))
    fig = newdf.plot(kind="bar", figsize=(20,16)).get_figure()
    #fig.savefig("static\\images\\election2010.png")
    return fig

if __name__ == "__main__":
    app.run(debug=True)