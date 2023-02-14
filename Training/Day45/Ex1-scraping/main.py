from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title) -> <title>Angela's Personal Site</title>
# print(soup.title.name) -> title
# print(soup.title.string) -> Angela's Personal Site
# print(soup.p) -> first p element


all_anchor_tags = soup.find_all(name="a") # all anchor tags
#print(all_anchor_tags)



# for tag in all_anchor_tags:
    # print(tag.getText()) # all text from tags
    # print(tag.get("href")) # all links

heading = soup.find(name="h1", id="name")
# print(heading) -> <h1 id="name">Angela Yu</h1>

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading) -> <h3 class="heading">Books and Teaching</h3>
# print(section_heading.getText()) -> Books and Teaching
# print(section_heading.name) -> h3
# print(section_heading.get("class")) -> ['heading']

company_url = soup.select_one(selector="p a") #css selector
# print(company_url) -> <a href="https://www.appbrewery.co/">The App Brewery</a>
company_url1 = soup.select_one(selector="#name") #css selector

headings = soup.select(selector=".heading")
# print(headings) -> [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>] -> list

form_tag = soup.find("input")
print(form_tag.get("maxlength"))
