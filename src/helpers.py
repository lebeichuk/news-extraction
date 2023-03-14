import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup
from src.constants import (tech_urls, tech_sources, finance_urls, finance_sources, global_urls, global_sources, politics_urls, politics_sources)

def get_parameters(e) -> dict:
    """Returns parameters from event"""
    parameters = {
        'source': e.get('source'),
        'category': e.get('category'),
    }
    return parameters

def configure_resources()->DataFrame:
    """
    This function creates a configuration dataframe with the urls and sources of the news feeds
    :return: config dataframe
    """
    category_tech = ["technology"] * len(tech_urls)
    tech_urls_sources = list(zip(tech_sources, tech_urls, category_tech))
    tech_config_df = pd.DataFrame(tech_urls_sources, columns =['source', 'url', 'category'])

    category_finance = ["finance"] * len(finance_urls)
    finance_urls_sources = list(zip(finance_sources, finance_urls, category_finance))
    finance_config_df = pd.DataFrame(finance_urls_sources, columns =['source', 'url', 'category'])


    category_global = ["global"] * len(global_urls)
    global_urls_sources = list(zip(global_sources, global_urls, category_global))
    global_config_df = pd.DataFrame(global_urls_sources, columns =['source', 'url', 'category'])

    category_politics = ["politics"] * len(politics_urls)
    politics_urls_sources = list(zip(politics_sources, politics_urls, category_politics))
    politics_config_df = pd.DataFrame(politics_urls_sources, columns =['source', 'url', 'category'])

    config_df = pd.concat([tech_config_df, finance_config_df, global_config_df, politics_config_df], ignore_index=True)

    return config_df

def get_text(value)->str:
    '''
    This function takes in a string and returns the text without html tags
    returns: text string
    '''
    return BeautifulSoup(value, "html.parser").get_text()

def configure_extracted_data(data_df, source, category)->DataFrame:
    '''
    This function configures the extracted data from the rss feed
    parameters:
        data_df: dataframe from the rss feed
        source: source string
        category: category string
    returns: configured dataframe
    '''
    data_df["source"] = source
    data_df["category"] = category
    data_df["summary"] = data_df["summary"].apply(get_text)
    df = data_df[["title", "summary", "published", "source", "category"]]
    return df

