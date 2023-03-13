import feedparser
from helpers import *

def extract_news(config_df, category="all", source="all")->DataFrame:
    '''
    Extract news from the given category and source
    :param config_df: DataFrame containing the configuration of the news sources
    :param category: Category of the news to extract
    :param source: Source of the news to extract
    :return: DataFrame containing the extracted news
    '''
    if category != "all":
        if type(category) is not list:
            config_df = config_df[config_df["category"] == category]
            config_df = config_df.reset_index(drop=True)
        else:
            config_df = config_df[config_df["category"].isin(category)]
            config_df = config_df.reset_index(drop=True)
    if source != "all":
        if type(source) is not list:
            config_df = config_df[config_df["source"] == source]
            config_df = config_df.reset_index(drop=True)
        else:
            config_df = config_df[config_df["source"].isin(source)]
            config_df = config_df.reset_index(drop=True)

    news_df = pd.DataFrame()

    for index, row in config_df.iterrows():
        data = feedparser.parse(row["url"])
        data_df = pd.DataFrame.from_dict(data.entries)
        configured_df = configure_extracted_data(data_df, row["source"], row["category"])
        news_df = pd.concat([news_df, configured_df], ignore_index=True)

    return news_df
