import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display

page = requests.get('https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D9%85%D9%82%D8%AF%D9%85%D8%A7%D8%AA%DB%8C-mk346/?pricing=true')
soup = BeautifulSoup(page.text, 'lxml')

my_ls = [[]]

# table = soup.find('table', class_ = 'table')
course_title = soup.find('h1')
my_ls[0].append(course_title.text)
print(course_title.text)
# print(soup.title.text.strip())

img_tag = soup.find('img', {'class': 'teacher-card__image'})
prof = img_tag.attrs['title']
my_ls[0].append(prof)
print(prof)

price_tag = soup.find('meta', {'name': 'price'})
price = price_tag.attrs['content']
my_ls[0].append(price)
print(price)

disc_tag = soup.find('div', {'class': 'course-enroll__old-price'})
disc = disc_tag.text
my_ls[0].append(disc)
print(disc)

headers = ['عنوان دوره', 'مدرس', 'قیمت اصلی', 'قیمت با تخفیف']

print(my_ls)

df = pd.DataFrame(my_ls, columns=headers)

display(df)