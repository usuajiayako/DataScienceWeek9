from .resources import VisitorResource
import pandas as pd
import io
from IPython.display import HTML
from django.http import HttpResponse

data = ""

def data_to_df(selected):
    visitor_resource = VisitorResource()
    dataset = visitor_resource.export(selected)
    global data
    data = dataset.csv
    string_data = data
    df = pd.read_csv(io.StringIO(string_data), sep=",")
    df = df.to_html()
    return df
