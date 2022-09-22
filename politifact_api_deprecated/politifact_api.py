from politifact import Politifact
#by thundergolfer
# https://github.com/thundergolfer/politifact-py
#Somewhat outdated - Scraper set-up for PolitiFact.com using the a rest API that doesn't seem to exist anymore.

#Trying to test out the script and work by thundergolfer. However it seems the API link is outdated. It continues to run without getting the results.
p = Politifact()
obama_related = p.statements().people('Barack Obama')

for statement in obama_related:
  print(statement.ruling)