from .resources import VisitorResource
import pandas as pd
import io
from IPython.display import HTML
from django.http import HttpResponse

data = ""

def data_to_df():
    visitor_resource = VisitorResource()
    dataset = visitor_resource.export()
    global data
    data = dataset.csv
    print(type(dataset))
    string_data = data
    df = pd.read_csv(io.StringIO(string_data), sep=",")
    df = df.to_html()
    print(df)
    return df
