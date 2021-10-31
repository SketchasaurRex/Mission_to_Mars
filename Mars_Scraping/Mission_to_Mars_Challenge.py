# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# %%
# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# %%
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# %%
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# %%
slide_elem.find('div', class_='content_title')


# %%
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# %%
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# %%
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# %%
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# %%
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# %%
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# %%
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# %%
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# %%
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# %%
df.to_html()


# %%
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# %%
# 2. Create a list to hold the images and titles.

html = browser.html
Mars_soup = soup(html, "html.parser")
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

mars_html = Mars_soup.find_all(class_="description")

for info in mars_html:
    imglink = info.a["href"]
    mars_link = url + imglink

    browser.visit(mars_link)
    mars_pic = soup(browser.html, "html.parser")

    img_ext = mars_pic.find("a", text="Sample")["href"]
    mars_pic_url = f"{url}{img_ext}"

    title = mars_pic.find("h2", class_="title").text

    mars_dict = {"Img URL": mars_pic_url,
                "title": title}

    hemisphere_image_urls.append(mars_dict)


mars_html


# %%



# %%
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# %%
# 5. Quit the browser
browser.quit()


# %%



# %%



# %%



# %%



