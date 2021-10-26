# IR CS Project - ODI Cricketers Search

## Running elastic search
- `.\bin\elasticsearch.bat`
- Run index.py to create the index in elastic search


### Supported Search queries
- Search by name
- Search by school
- Search player bio(playing role, batting style, bowling style)
- වැඩිම ලකුණු ලබාගත් ක්‍රීඩකයන් [number] E.g වැඩිම ලකුණු ලබාගත් ක්‍රීඩකයන් 10
- වැඩිම කඩුලු ලබාගත් ක්‍රීඩකයන් [number] E.g වැඩිම කඩුලු ලබාගත් ක්‍රීඩකයන් 15
- වැඩිම තරඟ ක්‍රීඩා කළ ක්‍රීඩකයන් [number] E.g වැඩිම තරඟ ක්‍රීඩා කළ ක්‍රීඩකයන් 20


### Additional Notes
- Fuzzy string matching done using FuzzyWuzzy package which uses Levenshtein Distance.
- BeautifulSoup4 used for scraping.
- Data source: ESPNCrinfo
- Corpus includes the top 100 ODI cricketers that have played the most matches.