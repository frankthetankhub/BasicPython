import re

article = """High-Tech Degrees and the Price of an Avocado: The Data New York Gave to Amazon\n\n
The city and state sent loads of data to Amazon during its search for a new headquarters, offering a peek into the valuable information the company collected during the process.
\n\nKaren Weise\n\n
By Karen Weise\n\n
\tDec. 12, 2018\n\n
[Updated Feb. 14: Amazon said it was canceling plans to build a corporate campus in New York City, after the deal had run into fierce opposition from local lawmakers who criticized providing subsidies to one of the world’s most valuable companies.]\n\nAn avocado at Whole Foods costs 1.25. \nColumbia University handed out 724 graduate degrees in computer science over the past three years. \nAnd 10 potential land parcels in Long Island City are zoned M1-4, for light manufacturing.\n\nNew York provided all of these data points, and thousands more, to Amazon as part of its successful bid to woo the tech giant to town.\n\nOn Monday, New York City posted online the 253-page proposal it submitted, along with New York State, to Amazon in March. \nThe city quickly took the file down, saying it should have checked with its partners before posting it, because the document included proprietary information. \nBut The New York Times downloaded the document before it was taken off the public website.\n\nThe proposal shows the types of data, some rarely available publicly, that the company amassed from cities across the country as part of its search for a second headquarters.
"""

def make_nice(article):
    ls = article.split("\n")
    ls = [line for line in ls if line]
    third = ls.pop(3)
    sixth = ls.pop(4)
    ls[2] = ls[2]+" - " +ls[3][1:]
    ls.pop(3)
    ls1 = ["############################################ START OF TEXT ############################################"]
    for idx, line in enumerate(ls):
        if idx >3:
            ls1.append(str(idx-2)+": "+ line)
        else:
            ls1.append(line)
    ls1.append("\n")
    ls1.append("############################################ END OF TEXT ############################################")
    text = ""
    for i in range(5):
        ls1[i] += "\n"
    for idx in range(len(ls1)):
        ls1[idx] = ls1[idx] + "\n"
        text = text + ls1[idx]
    return text

article_nice = make_nice(article)

my_regex1 = "[0-9]"
my_regex2 = "[1-5|t]"
my_regex3 = "A[a-z]*n\s"

compiled1 = re.compile(my_regex1)
compiled2 = re.compile(my_regex2)
compiled3 = re.compile(my_regex3)

print(f"replacing with regex: {my_regex1}")
replaced = compiled1.sub("FOUND IT!", article_nice)
print(replaced)
print("-------------")
print(f"replacing with regex: {my_regex2}")
replaced = compiled2.sub("FOUND IT!", article_nice)
print(replaced)
print("-------------")
print(f"replacing with regex: {my_regex3}")
replaced = compiled3.sub("FOUND IT!", article_nice)
print(replaced)
