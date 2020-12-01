
from selenium import webdriver
import pandas as pd

#-----------------------------------------------------------------
#chrome driver path and main url
#-----------------------------------------------------------------

wd_path = r'/Users/toshida/TMO/Learning/Python/chromedriver'
url = 'https://spongebob.fandom.com/wiki/List_of_transcripts'
episodes = pd.DataFrame(columns = ['Link','Transcript'])

#-----------------------------------------------------------------
#Function 
#-----------------------------------------------------------------
def findSponge(wd_path,url,episodes):

    filter = pd.DataFrame(columns = ['Link','Transcript'])
    inputA = 'party'
    inputB = 'hardy'
#-----------------------------------------------------------------
#steps to open chrome
#-----------------------------------------------------------------

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(wd_path,options=options)

#-----------------------------------------------------------------
#Setting up Lists and Data Frame
#-----------------------------------------------------------------

    episode = {}
    id_dic = {}
    episode_link = []
    link = []
    transcript = []
    partyLink = []
    partyTranscript = []

#-----------------------------------------------------------------
#First loop to go through each page
#-----------------------------------------------------------------

    driver.get(url)
    a = "//*[contains(@href,'transcript')]"
    episode_ids_path = driver.find_elements_by_xpath(a)

#----------------------------------------------------------------- 
#Loop to get Episode IDs - 485
#-----------------------------------------------------------------

    for i in episode_ids_path:
        episode_link.append(i.get_attribute('href'))

    link_subset = episode_link[180:185]

#----------------------------------------------------------------- 
#Loop to get Transcripts from the subset list of links - create df
#-----------------------------------------------------------------
    count = 0
    for i in link_subset:
        driver.get(str(i))
        xpath2 = "//*[@id='mw-content-text']/ul"
        content = driver.find_element_by_xpath(xpath2)
        transcripts = content.text
        link.append(i)
        transcript.append(transcripts)
        count = count + 1
        print(count)
        print(i)
    episodes["Link"] = link
    episodes['Transcript'] = transcript

#----------------------------------------------------------------- 
#Filter DF to episodes that includes the word 'party'
#-----------------------------------------------------------------

    filter = episodes[episodes['Transcript'].str.contains(inputA)]
    filter = filter[filter['Transcript'].str.contains(inputB)]

    return filter

 #   party = pd.DataFrame(columns = ['Link','Transcript'])

party = findSponge(wd_path,url,episodes)
