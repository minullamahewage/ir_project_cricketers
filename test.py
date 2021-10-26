from fuzzywuzzy import process,fuzz

choices= [u"වැඩිම ලකුණු ලබාගත් ක්‍රීඩකයන්",u"වැඩිම කඩුලු ලබාගත් ක්‍රීඩකයන්",u"වැඩිම තරඟ ක්‍රීඩා කළ ක්‍රීඩකයන්"]
highest = process.extractOne(u"වැඩිම ලකුණු", choices, scorer=fuzz.ratio)
print(highest)
# You can also select the string with the highest matching percentage
# highest = process.extractOne(str2Match,strOptions)
# print(highest)