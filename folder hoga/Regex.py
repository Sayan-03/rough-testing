import re

def get_details(patterns,text):
    matches=[]
    for i in patterns:
        match=re.findall(i,text)
        match=match[0].strip()
        matches.append(match)
    return matches

text='''Born	Elon Reeve Musk
June 28, 1971 (age 51)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
CEO and President of Twitter, Inc.
President of the Musk Foundation
Founder of the Boring Company and X.com (now part of PayPal)
Co-founder of Neuralink, OpenAI and Zip2
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[a][3]
Parents	
Maye Musk
Errol Musk
Family	Musk family
Awards	List of honors and awards'''

pattern=['Born(.*)\n','Born.*\n(.*)\(','age(.*)\)','age.*\n(.*)']
matches=get_details(pattern,text)
print(matches)