# This Repo explores and Maps out different Fact-checking Websites.


The goal is to find fact-checking websites and resources that can be used to create datasets of Fake News Links and articles.


### Gulde on how to Scrape data from PolitiFact
+ Scraping PolitiFact (Documentation) https://randerson112358.medium.com/scrape-a-political-website-for-fake-real-news-using-python-b4f5b2af830b
+ Scraping politifact (not getting the URLs of the fakenews...) https://www.youtube.com/watch?v=Nz1zPkiHcbg


### Existing Resources as of September 2022

+ https://politifact.com
+ https://www.factcheck.org/
+ https://developers.google.com/fact-check/tools/api/
+ https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset/metadata (https://www.uvic.ca/ecs/ece/isot/assets/docs/ISOT_Fake_News_Dataset_ReadMe.pdf?utm_medium=redirect&utm_source=/engineering/ece/isot/assets/docs/ISOT_Fake_News_Dataset_ReadMe.pdf&utm_campaign=redirect-usage
)


### Notes & Learning

+ The first URLS under the fact check sources is the orignal fake news URL link. Many of these have dead links as they have been removed by the blog page or social media page that they where made on etc. 
+ Also, many of the URLS are not present when searching on tweets. From some brief testing it seems that the URLS typically appear with a different format on Twitter.
+ Approach could be to search for News Article title "96% of U.S. climate data is corrupted" through browser and then scrape the resulting links to a news article.




![politifact kaggle scraping flow]('https://www.kaggle.com/datasets/shivkumarganesh/politifact-factcheck-data?resource=download')



![topics_distr](kaggle_politifact/topics_distribution.pdf)