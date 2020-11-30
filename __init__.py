from flask import Flask, render_template, jsonify, Response
import io, random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

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
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

if __name__ == "__main__":
    app.run(debug=True)