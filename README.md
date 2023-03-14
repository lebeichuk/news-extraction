## Parameters for the news extraction tool:
- category (str or list) : the category of the news to be extracted
- news_source(str or list): the news source to be extracted

## Default parameters values:
- category: "all"
- news_source: "all"

## Examples of usage:
```python
df = extract_news(config_df, category="global")
```
Will return a dataframe with all the news sources from the category "global"
``` python
df = extract_news(config_df, category="global", source="france24")
```
Will return a dataframe with all the news from the category "global" and the source "france24"

## Important note:
Source list (or source string) should include source name for category otherwise fuction will return an empty dataframe
``` python
df = extract_news(config_df, category=["global", "politics"], source=["theguardian", "bbc", "nytimes"])
```
Will return a dataframe with all the news from the category "global" and "politics" and the sources "theguardian", "bbc" and "nytimes"
``` python
df = extract_news(config_df)
```
Will return a dataframe with all the news from all the categories and all the sources (it can take up to 5-10 minutes to run)


## Category parameter
Available news category:
All categories - "all" (default)
General news - "general"
Political news - "political"
Financial news - "financial"
Technology news - "technology"

News_source parameter
Available news sources
All sources - "all" (default)
All sources - "all" (default)

| General news | Political news | Financial news | Technology news |
|--------------|----------------|----------------|-----------------|
| globalnews | thenation | marketwatch | techcrunch |
| cbc | npr | reuters | mashable |
| theguardian | fivethirtyeight | thestreet | gizmodo |
| nytimes | thehill | benzinga | engadget |
| bbc | realclearpolitics | gfmag | techhive |
| aljazeera | national_review | financial_samurai | theverge |
| buzzfeed | politico_picks | forbes | feedburner_oreilly |
| defence-blog | nytimes | money_week | findlaw |
| thecipherbrief | thepoliticalinsider | european_financial_review | apple_insider |
| abc_news | frontmoveon | moneymorning | trustedreviews |
| feedburner-global | unz | fortune | computerworld |
| npr | fivethirtyeight | business_financial_post | technologyreview |
| france24 | boingboing | mjbizdaily | feedburnerthenextweb |
| brookings | theintercept | insightssuccess | bgr |
| warontherocks | motherjones | feedburner-finance | datadriveninvestor |
| 247newsaroundtheworld | dailysignal | talkingbiznews | feedburnertechdirt |
| dailyresearchplot | conservativehome | iotbusinessnews | extremetech |
| wan-ifra | politics_uk | businessmole | techmeme |
| headlinesoftoday | washingtonmonthly | smallbiztalks | siliconangle |
| quintdaily | centerforpolitics | guestviral | geekwire |
| worldnewsera | coloradopols | - | gigaom | 
| articleify | sluggerotoole | - | ilounge |
| internewscast | leftfootforward | - | ishir |
| wow_plus | hughhewitt| - | techengage |
| theunionjournal | shadowproof | - | siliconrepublic |
| rightwirereport | yallpolitics | - |  it_worldcanada |
| worldweeklynews | coloradopeakpolitics | - | technewsworld |
| thenexthint | buzzmachine | - | itchronicles |
| forsige | gopillinois | - | pixel-studios |
| newslanes | lawandpoliticsofaltondrew | - | afritechmedia |
| usnn | uncommonthought | - | alicekeeler |
| latimes | crooksandliars | - | justtotaltech |
| - | democracyparadox | - | waftr |
| - | krpoliticaljunkie | - | area19delegate |
| - | eyeonglobalpolitics | - | feedburnerausdroid-technology |
| - | politicsguys | - | techmused |
| - | wingsoverscotland | - | - |
| - | fitzfile | - | - | - |
| - | unpoliticallycorrect | - | - |
| - | garyhasissues | - | - |