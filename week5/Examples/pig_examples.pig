-- pig examples

-- word count example
a = load './pg1268.txt';
b = FOREACH a GENERATE flatten(TOKENIZE((chararray)$0)) AS word;
c = GROUP b BY word;
d = FOREACH c GENERATE group, COUNT(b) AS freq;
sorted = ORDER d BY freq DESC;

t = LIMIT sorted 10;
DUMP t;

STORE sorted into './pig_wordcount';
