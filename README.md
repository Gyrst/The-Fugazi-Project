# This Repo explores and Maps out different Fact-checking Websites.

The goal is to find fact-checking websites and resources that can be used to create datasets of Fake News Links and articles.



### How to Scrape
+ Scraping PolitiFact (Documentation) https://randerson112358.medium.com/scrape-a-political-website-for-fake-real-news-using-python-b4f5b2af830b
+ Scraping politifact (not getting the URLs of the fakenews...) https://www.youtube.com/watch?v=Nz1zPkiHcbg


### Resources

+ https://politifact.com
+ https://www.factcheck.org/
+ https://developers.google.com/fact-check/tools/api/
+ https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset/metadata (https://www.uvic.ca/ecs/ece/isot/assets/docs/ISOT_Fake_News_Dataset_ReadMe.pdf?utm_medium=redirect&utm_source=/engineering/ece/isot/assets/docs/ISOT_Fake_News_Dataset_ReadMe.pdf&utm_campaign=redirect-usage
)


### Notes

+ It doesn't seem trivial to get the URLs of Fake News through PolitiFact or factcheck, as they are not highlighted / made easily accesible in a fixed position on the website.
+ Approach could be to search for News Article title "96% of U.S. climate data is corrupted" through browser and then scrape the resulting links to a news article.
+ 