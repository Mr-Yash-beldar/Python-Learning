# import requests
# from bs4 import BeautifulSoup

# url="https://www.rcpit.ac.in"
# req=requests.get(url)
# soup=BeautifulSoup(req.content,"html.parser")

# file_name = "data.html"

# with open(file_name, 'w') as file:
#     file.write(soup)
#     file.write("This is a simple file created in Python.\n")

# print(f"File '{file_name}' has been created and written successfully.")
import requests
from bs4 import BeautifulSoup

url = "https://www.rcpit.ac.in"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

file_name = "data.html"

with open(file_name, 'w', encoding='utf-8') as file:
    file.write(str(soup.prettify))
    file.write("\nThis is a simple file created in Python.\n")

print(f"File '{file_name}' has been created and written successfully.")
