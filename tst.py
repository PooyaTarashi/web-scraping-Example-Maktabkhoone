# I use Genie, a great vscode plugin which helps me use chatGPT in vscode. This code is written by Genie.


from bs4 import BeautifulSoup

# Sample HTML content
html = """
<div class="container">
  <h1>Hello World</h1>
  <div class="inner-div">
    <p>This is some text.</p>
  </div>
</div>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the outer div tag
outer_div = soup.find('div', {'class': 'container'})

# Find the inner div tag inside the outer div tag
inner_div = outer_div.find('div', {'class': 'inner-div'})

# Print the contents of the inner div tag
print(inner_div.prettify())
