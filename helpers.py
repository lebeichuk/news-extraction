import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup


def configure_resources()->DataFrame:
    """
    This function creates a configuration dataframe with the urls and sources of the news feeds
    :return: config dataframe
    """
    tech_urls = [
        "https://techcrunch.com/feed/",
        "https://mashable.com/feeds/rss/all",
        "https://gizmodo.com/feed/rss",
        "https://www.engadget.com/rss.xml",
        "https://techhive.com/feed",
        "https://www.theverge.com/rss/index.xml",
        "https://feeds.feedburner.com/oreilly/radar/atom",
        "http://feeds.findlaw.com/FLTechnologist",
        "https://appleinsider.com/rss/news/",
        "https://www.trustedreviews.com/feed",
        "http://www.computerworld.com/index.rss",
        "https://www.technologyreview.com/topnews.rss",
        "https://feeds.feedburner.com/thenextweb",
        "https://bgr.com/tech/feed/",
        "https://www.datadriveninvestor.com/feed/",
        "https://feeds.feedburner.com/techdirt/feed",
        "http://www.extremetech.com/feed",
        "https://www.techmeme.com/feed.xml?x=1",
        "https://siliconangle.com/feed/",
        "https://www.geekwire.com/feed/",
        "https://gigaom.com/feed/",
        "https://www.ilounge.com/feed",
        "https://www.ishir.com/feed/",
        "https://techengage.com/feed",
        "https://www.siliconrepublic.com/feed",
        "http://www.itworldcanada.com/feed",
        "http://www.technewsworld.com/perl/syndication/rssfull.pl",
        "https://itchronicles.com/feed/",
        "https://www.pixel-studios.com/blog/feed/",
        "https://www.afritechmedia.com/feed/",
        "https://alicekeeler.com/feed/",
        "https://justtotaltech.com/feed/",
        "https://www.waftr.com/feed/ ",
        "https://www.area19delegate.org/feed/",
        "http://feeds.feedburner.com/ausdroid/feed",
        "https://techmused.com/feed/",
        ]
    tech_sources = [
        "techcrunch",
        "mashable",
        "gizmodo",
        "engadget",
        "techhive",
        "theverge",
        "feedburner_oreilly",
        "findlaw",
        "apple_insider",
        "trustedreviews",
        "computerworld",
        "technologyreview",
        "feedburnerthenextweb",
        "bgr",
        "datadriveninvestor",
        "feedburnertechdirt",
        "extremetech",
        "techmeme",
        "siliconangle",
        "geekwire",
        "gigaom",
        "ilounge",
        "ishir",
        "techengage",
        "siliconrepublic",
        "it_worldcanada",
        "technewsworld",
        "itchronicles",
        "pixel-studios",
        "afritechmedia",
        "alicekeeler",
        "justtotaltech",
        "waftr",
        "area19delegate",
        "feedburnerausdroid-technology",
        "techmused",
        ]
    category_tech = ["technology"] * len(tech_urls)
    tech_urls_sources = list(zip(tech_sources, tech_urls, category_tech))
    tech_config_df = pd.DataFrame(tech_urls_sources, columns =['source', 'url', 'category'])


    finance_urls = ["http://feeds.marketwatch.com/marketwatch/marketpulse/",
                    "https://www.reutersagency.com/feed/?taxonomy=best-sectors&post_type=best",
                    "https://www.thestreet.com/.rss/full/", "http://feeds.benzinga.com/benzinga",
                    "https://www.gfmag.com/feeds/recent_updates/rss.xml",
                    "https://www.financialsamurai.com/feed/",
                    "https://www.forbes.com/money/feed/",
                    "https://moneyweek.com/feed/all",
                    "https://www.europeanfinancialreview.com/feed/",
                    "https://moneymorning.com/feed/",
                    "https://fortune.com/feed",
                    "https://business.financialpost.com/feed/",
                    "https://mjbizdaily.com/feed/",
                    "https://www.insightssuccess.com/feed/",
                    "https://feeds.feedburner.com/ModestMoney",
                    "http://talkingbiznews.com/feed/",
                    "https://iotbusinessnews.com/feed/",
                    "https://www.businessmole.com/feed/",
                    "http://smallbiztalks.com/feed/",
                    "https://www.guestviral.com/business/feed/",
                    ]
    finance_sources = ["marketwatch",
                        "reuters",
                        "thestreet",
                        "benzinga",
                        "gfmag",
                        "financial_samurai",
                        "forbes",
                        "money_week",
                        "european_financial_review",
                        "moneymorning",
                        "fortune",
                        "business_financial_post",
                        "mjbizdaily",
                        "insightssuccess",
                        "feedburner-finance",
                        "talkingbiznews",
                        "iotbusinessnews",
                        "businessmole",
                        "smallbiztalks",
                        "guestviral",
                        ]
    category_finance = ["finance"] * len(finance_urls)
    finance_urls_sources = list(zip(finance_sources, finance_urls, category_finance))
    finance_config_df = pd.DataFrame(finance_urls_sources, columns =['source', 'url', 'category'])


    global_urls = ["https://globalnews.ca/feed",
                    "https://www.cbc.ca/cmlink/rss-world",
                    "https://www.theguardian.com/world/rss",
                    "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml",
                    "https://www.bbc.com/news/world/rss.xml",
                    "https://www.aljazeera.com/xml/rss/all.xml",
                    "https://www.buzzfeed.com/world.xml",
                    "https://defence-blog.com/feed/",
                    "https://www.thecipherbrief.com/feed",
                    "http://abcnews.go.com/abcnews/internationalheadlines",
                    "https://feeds.feedburner.com/ndtvnews-world-news",
                    "http://www.npr.org/rss/rss.php?id=1004",
                    "https://www.france24.com/en/rss",
                    "https://www.brookings.edu/topic/international-affairs/feed/",
                    "https://warontherocks.com/feed/",
                    "https://247newsaroundtheworld.com/feed/",
                    "https://dailyresearchplot.com/feed/",
                    "https://wan-ifra.org/news/feed/",
                    "https://www.headlinesoftoday.com/feed",
                    "https://quintdaily.com/feed/",
                    "https://worldnewsera.com/feed/",
                    "https://articleify.com/feed/",
                    "https://internewscast.com/feed/",
                    "https://wowplus.net/feed/",
                    "https://www.theunionjournal.com/feed/",
                    "https://rightwirereport.com/feed",
                    "https://worldweeklynews.com/feed/",
                    "https://www.thenexthint.com/feed/",
                    "https://www.forsige.com/feed/",
                    "https://newslanes.com/feed/",
                    "https://www.usnn.news/feed/",
                    "https://www.latimes.com/world/rss2.0.xml",
                    ]
    global_sources = ["globalnews",
                        "cbc",
                        "theguardian",
                        "nytimes",
                        "bbc",
                        "aljazeera",
                        "buzzfeed",
                        "defence-blog",
                        "thecipherbrief",
                        "abc_news",
                        "feedburner-global",
                        "npr",
                        "france24",
                        "brookings",
                        "warontherocks",
                        "247newsaroundtheworld",
                        "dailyresearchplot",
                        "wan-ifra",
                        "headlinesoftoday",
                        "quintdaily",
                        "worldnewsera",
                        "articleify",
                        "internewscast",
                        "wow_plus",
                        "theunionjournal",
                        "rightwirereport",
                        "worldweeklynews",
                        "thenexthint",
                        "forsige",
                        "newslanes",
                        "usnn",
                        "latimes",
                        ]
    category_global = ["global"] * len(global_urls)
    global_urls_sources = list(zip(global_sources, global_urls, category_global))
    global_config_df = pd.DataFrame(global_urls_sources, columns =['source', 'url', 'category'])

    politics_urls = ["https://www.thenation.com/subject/politics/feed/",
                    "https://www.npr.org/rss/rss.php?id=1001",
                    "https://fivethirtyeight.com/politics/feed/",
                    "https://thehill.com/feed/",
                    "https://www.realclearpolitics.com/index.xml",
                    "https://www.nationalreview.com/feed/",
                    "https://www.politico.com/rss/politicopicks.xml",
                    "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/politics/rss.xml",
                    "https://thepoliticalinsider.com/feed/",
                    "https://front.moveon.org/feed/",
                    "https://www.unz.com/xfeed/rss/all/",
                    "https://fivethirtyeight.com/politics/feed/",
                    "https://boingboing.net/tag/politics/feed",
                    "https://theintercept.com/feed/?rss",
                    "https://www.motherjones.com/politics/feed/",
                    "http://dailysignal.com/category/politics-topics/feed",
                    "http://www.conservativehome.com/feed",
                    "https://www.politics.co.uk/feed/",
                    "http://washingtonmonthly.com/feed/",
                    "https://centerforpolitics.org/crystalball/feed/",
                    "https://www.coloradopols.com/feed",
                    "https://sluggerotoole.com/feed/",
                    "https://leftfootforward.org/feed/",
                    "https://hughhewitt.com/feed/?cat=1",
                    "https://shadowproof.com/feed/",
                    "https://yallpolitics.com/feed/",
                    "https://coloradopeakpolitics.com/feed/",
                    "https://buzzmachine.com/feed/",
                    "https://gopillinois.com/feed/",
                    "https://lawandpoliticsofaltondrew.com/feed/",
                    "https://www.uncommonthought.com/mtblog/feed",
                    "http://feeds.crooksandliars.com/crooksandliars/YaCP",
                    "https://democracyparadox.com/feed/",
                    "https://www.krpoliticaljunkie.com/feed/",
                    "https://eyeonglobalpolitics.com/feed/",
                    "https://politicsguys.com/feed/?format=xml",
                    "https://wingsoverscotland.com/feed/",
                    "https://fitzfile.com/feed/",
                    "https://www.unpoliticallycorrect.org/feed/",
                    "http://www.garyhasissues.com/feed/",
                    ]
    politics_sources = ["thenation",
                        "npr",
                        "fivethirtyeight",
                        "thehill",
                        "realclearpolitics",
                        "national_review",
                        "politico_picks",
                        "nytimes",
                        "thepoliticalinsider",
                        "frontmoveon",
                        "unz",
                        "fivethirtyeight",
                        "boingboing",
                        "theintercept",
                        "motherjones",
                        "dailysignal",
                        "conservativehome",
                        "politics_uk",
                        "washingtonmonthly",
                        "centerforpolitics",
                        "coloradopols",
                        "sluggerotoole",
                        "leftfootforward",
                        "hughhewitt",
                        "shadowproof",
                        "yallpolitics",
                        "coloradopeakpolitics",
                        "buzzmachine",
                        "gopillinois",
                        "lawandpoliticsofaltondrew",
                        "uncommonthought",
                        "crooksandliars",
                        "democracyparadox",
                        "krpoliticaljunkie",
                        "eyeonglobalpolitics",
                        "politicsguys",
                        "wingsoverscotland",
                        "fitzfile",
                        "unpoliticallycorrect",
                        "garyhasissues",
                        ]
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

