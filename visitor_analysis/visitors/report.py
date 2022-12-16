from .resources import VisitorResource
import pandas as pd
import io

data = ""

def data_to_df():
    visitor_resource = VisitorResource()
    dataset = visitor_resource.export()
    global data
    data = dataset.csv
    string_data = data
    df = pd.read_csv(io.StringIO(string_data), sep=",")
    return df
