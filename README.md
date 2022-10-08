#  The Epic Politifact Scraper & Datasets

This Repo comprise a BeautifulSoup Python web scraper designed to fetch fake checked claims from the fact-checking organization politifact.org. Feel free to reach to reach out and use the scraper provided. Make sure to research legal usecases and moral when applying the data.

You are also welcome to reach out to me on Github if you  might have any questions for the scraper.

This repo is part of a serious of repoes related to the Fugazi Project that is Laurenz Aisenpreis and my master thesis project. The Fugazi Project is about understanding the drivers that make people susceptible to sharing and spreading fake news. 

### Guide on how to Scrape data from PolitiFact

The politifact scraper can be run from the src/politifact_scraper.py. You can read about how to make it run in the documentation available in politifact_scraper.py

There also exists good resources online and toturials to create a scraper for PolitiFact. https://randerson112358.medium.com/scrape-a-political-website-for-fake-real-news-using-python-b4f5b2af830b
+ Scraping politifact (not getting the URLs of the fakenews...) https://www.youtube.com/watch?v=Nz1zPkiHcbg


### Existing Resources as of September 2022

+ https://politifact.com
    - Mixed topics
    - Very renowned and appearing in a multitude of studies
+ Fact-Check https://www.factcheck.org/
    - Mostly politics
    - US-based Non-profit renowned by Times. Also found in Research (Way less than politifact)
    - Paper using the site for data (https://journals.sagepub.com/doi/abs/10.1177/1077699017710453) ~130 citations
+ Reuters Fact Checking https://www.reuters.com/fact-check
    - No menu or breakdown of topics
    - Mixed topics
    - UK-based (International Scope)  
+ https://developers.google.com/fact-check/tools/api/
+ https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset/metadata (https://www.uvic.ca/ecs/ece/isot/assets/docs/ISOT_Fake_News_Dataset_ReadMe.pdf?utm_medium=redirect&utm_source=/engineering/ece/isot/assets/docs/ISOT_Fake_News_Dataset_ReadMe.pdf&utm_campaign=redirect-usage
)

### Notes & Learning

+ The first URLS under the fact check sources is the orignal fake news URL link. Many of these have dead links as they have been removed by the blog page or social media page that they where made on etc. 
+ Also, many of the URLS are not present when searching on tweets. From some brief testing it seems that the URLS typically appear with a different format on Twitter.
+ Approach could be to search for News Article title "96% of U.S. climate data is corrupted" through browser and then scrape the resulting links to a news article.


![politifact kaggle scraping flow]('https://i.imgur.com/9MH52Uf.jpg')




### Notes Building Scraper 
+ The scraper uses BeautifulSoup to read the textual material from the HTML.




### Errors from the scrape 071022 off all topics except the original 7 topics (climate-change, environment, covid-19 etc.)

+ See the output file to get full review from the run
+ Error occured at 1 https://www.politifact.com/factchecks/list/?page=1&category=kagan-nomination
+ Error occured at 7 https://www.politifact.com/factchecks/list/?page=7&category=supreme-court



### Existing Resources as of September 2022

+ https://politifact.com
    - Mixed topics
    - Very renowned and appearing in a multitude of studies
+ Fact-Check https://www.factcheck.org/
    - Mostly politics
    - US-based Non-profit renowned by Times. Also found in Research (Way less than politifact)
    - Paper using the site for data (https://journals.sagepub.com/doi/abs/10.1177/1077699017710453) ~130 citations
+ Reuters Fact Checking https://www.reuters.com/fact-check
    - No menu or breakdown of topics
    - Mixed topics
    - UK-based (International Scope)  
+ https://developers.google.com/fact-check/tools/api/
+ https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset/metadata (https://www.uvic.ca/ecs/ece/isot/assets/docs/ISOT_Fake_News_Dataset_ReadMe.pdf?utm_medium=redirect&utm_source=/engineering/ece/isot/assets/docs/ISOT_Fake_News_Dataset_ReadMe.pdf&utm_campaign=redirect-usage
)
