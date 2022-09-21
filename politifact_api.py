from politifact import Politifact

#Somewhat outdated - but @thundergolfter did a API / Scraper set-up for PolitiFact.com 
# https://github.com/thundergolfer/politifact-py
#Trying to test out the script and work by thundergolfer. However it seems the API link is outdated. It continues to run without getting the results.

p = Politifact()
obama_related = p.statements().people('Barack Obama')

for statement in obama_related:
  print(statement.ruling)