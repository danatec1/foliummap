"""flask
example.py
  -flask 22folium
  usage
  start the flask server by running
  $ python flask_example.py
  and then head to http://127.0.0.1:5000 in your brower to see the map displayed

"""
from flask import flask
import folium
app = Flask(__name__)

@app.route('/')
def index():
  start_coords = (46.9540700, 142.7360300)
  foilum_map = folium.Map(location=start_coords, zoom_start=14)
  return foilum_map._repr_html_()

  if __name__ == '__name__' :
    app.run(debug=True)
