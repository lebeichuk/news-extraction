from src.helpers import configure_resources, get_parameters
from src.news_extraction import extract_news
import pandas as pd


def handler(event,_):
    params = get_parameters(event)
    config_df = configure_resources()
    if params["category"] == "":
        df = extract_news(config_df, source=params["source"])
    elif params["source"] == "":
        df = extract_news(config_df, category=params["category"])
    else:
        df = extract_news(config_df, category=params["category"], source=params["source"])
    return df.to_json(orient="records")