from helpers import configure_resources
from news_extraction import extract_news


config_df = configure_resources()
df = extract_news(config_df, category="global", source="france24")

print(df.shape)
print(df)