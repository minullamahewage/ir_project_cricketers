# IR CS4642 Project - Sri Lankan ODI Cricketers Search
- M.H. Lamahewage
- 170342N

## Running elastic search
- `.\bin\elasticsearch.bat`
- Run indexing.py to create the index in elastic search

## Getting Started

- Tested on python 3.9.7 and elasticsearch 7.15

```commandline
git clone https://github.com/minullamahewage/ir_project_cricketers.git

cd ir_project_cricketers

pip install -r requirements.txt

python indexing.py

python app.py
```

### Web scraper included in the `cricket-scraper.ipynb` python notebook

### Supported Search queries
- Search by name(English/Sinhala) E.g ලසිත් මාලිංග
- Search by school E.g. ආනන්ද විද්‍යාලය
- Search by year born
- Search player bio(playing role, batting style, bowling style) E.g දකුණත් පිතිකරු, දකුණත් වේග පන්දු යවන
- වැඩිම ලකුණු ලබාගත් ක්‍රීඩකයන් [number] E.g වැඩිම ලකුණු ලබාගත් ක්‍රීඩකයන් 10
- වැඩිම කඩුලු ලබාගත් ක්‍රීඩකයන් [number] E.g වැඩිම කඩුලු ලබාගත් ක්‍රීඩකයන් 15
- වැඩිම තරඟ ක්‍රීඩා කළ ක්‍රීඩකයන් [number] E.g වැඩිම තරඟ ක්‍රීඩා කළ ක්‍රීඩකයන් 20


### Additional Notes
- Fuzzy string matching done using FuzzyWuzzy package which uses Levenshtein Distance.
- BeautifulSoup4 used for scraping.
- Data source: ESPNCricnfo - https://stats.espncricinfo.com/ci/engine/records/index.html
- Corpus includes the top 100 Sri Lankan ODI cricketers that have played the most matches.