from pandas import DataFrame
from pandas.io.json import json_normalize


def create_df(json_object: dict) -> DataFrame:
    return json_normalize(json_object)