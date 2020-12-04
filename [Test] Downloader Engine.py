import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup


# Function for download pdf file from entire Vulnerability URL
def downloader(URL, Counter):
    # get response from requested url
    response = requests.get(URL)
    # create bs4 object
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.select("a[href$='.pdf']"):
        # Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location, link['href'].split('/')[-1])
        print(str(Counter), " Saving ", os.path.basename(str(filename)), " To", folder_location)
        # Write out downloaded file
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(URL, link['href'])).content)
            Counter += 1


# counting downloaded file
counter = 1
# bad option counter
bad = 3
# Vulnerability Webpage = "http://coop-qnform.tni.ac.th/uploads/resume/transcript/"
# Input URL from User
URL = str(input("Enter URL: "))
print("Default Output path is D:\\output\nDo you want to change it?\n")
# Loop for error choice input
while 1:
    if bad == 0:
        print("Too much bad option.")
        quit()
    # Ask for Saving Directory
    Choice = str(input("Select Option (1:YES,2:NO): "))
    if Choice == '1' or Choice.lower() == 'yes':
        folder_location = str(input("Enter new output path: "))
        break
    elif Choice == '2' or Choice.lower() == "no":
        folder_location = r'D:\Output'
        break
    else:
        bad -= 1
        print("Invalid Option, " + str(bad) + "Time remaining")
# If there is no such folder, the script will create one automatically
if not os.path.exists(folder_location):
    os.mkdir(folder_location)
# Call Function using URL and download file counter as parameter
downloader(URL, counter)
# After Function was Finish Executed
print("Download complete!\t")
