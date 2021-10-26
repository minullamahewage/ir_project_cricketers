# IR CS4642 Project - ODI Cricketers Search
- M.H. Lamahewage
- 170342N

## Running elastic search
- `.\bin\elasticsearch.bat`
- Run index.py to create the index in elastic search

## Getting Started

```commandline
git clone https://github.com/minullamahewage/ir_project_cricketers.git

cd ir_project_cricketers

pip install -r requirements.txt

python indexing.py

python app.py
```

### Web scraper included in the `cricket-scraper.ipynb` python notebook

### Supported Search queries
- Search by name E.g ලසිත් මාලිංග
- Search by school E.g. ආනන්ද විද්‍යාලය
- Search player bio(playing role, batting style, bowling style) E.g දකුණත් පිතිකරු, දකුණත් වේග පන්දු යවන
- වැඩිම ලකුණු ලබාගත් ක්‍රීඩකයන් [number] E.g වැඩිම ලකුණු ලබාගත් ක්‍රීඩකයන් 10
- වැඩිම කඩුලු ලබාගත් ක්‍රීඩකයන් [number] E.g වැඩිම කඩුලු ලබාගත් ක්‍රීඩකයන් 15
- වැඩිම තරඟ ක්‍රීඩා කළ ක්‍රීඩකයන් [number] E.g වැඩිම තරඟ ක්‍රීඩා කළ ක්‍රීඩකයන් 20


### Additional Notes
- Fuzzy string matching done using FuzzyWuzzy package which uses Levenshtein Distance.
- BeautifulSoup4 used for scraping.
- Data source: ESPNCrinfo
- Corpus includes the top 100 ODI cricketers that have played the most matches.