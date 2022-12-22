from .resources import VisitorResource
import pandas as pd
import io
from IPython.display import HTML
from django.http import HttpResponse

data = ""

def data_to_df(selected_date):
    visitor_resource = VisitorResource()
    dataset = visitor_resource.export(selected_date)
    global data
    data = dataset.csv
    string_data = data
    df_csv = pd.read_csv(io.StringIO(string_data), sep=",")
    df = df_csv.to_html()
    return df, df_csv
