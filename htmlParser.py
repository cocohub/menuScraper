from scraper import Scraper
import re
import datetime

def chooseParser(url):
    '''
    Chooses which parser to execute depending on the URL
    '''
    if url == "http://www.nyaetage.se/veckans-meny":
        nyaEtage(url)
    elif url == "http://www.compass-group.se/restauranger/Sodra-Porten-Molndal-/Dagens-lunch-/":
        porten(url)


def nyaEtage(url):
    '''
    Special parser for Nya Etage HTML
    '''
    soup = Scraper.create_soup(url)
    array = []


    for section in soup.find_all('h4'):
		#print(section.string) # day
        nextNode = section
        while True:
            nextNode = nextNode.nextSibling
            try:
                tag_name = nextNode.name
            except AttributeError:
                tag_name = ""
            
            if tag_name == "li":
                array.append(nextNode.string.lstrip().rstrip())
            else:
                array.append("\n")
                break
                
    #print(array)
    finalArray = []
    today = datetime.datetime.today().weekday()
    counter = 0
    
    # Shorten the array until we're on today's food
    for _ in array:
        if counter == today:
            finalArray = array[:array.index("\n")]
            break
        else:
            array = array[array.index("\n")+1:]
            counter += 1
        
    todaysFood(finalArray)


def porten(url):
    '''
    Special parser for Södra porten HTML
    '''
    soup = Scraper.create_soup(url)
    array = []
    for iframe in soup.find_all('iframe'):
        i_soup = Scraper.create_soup(iframe.attrs['src'])

        for tag in i_soup.find_all('div', class_='container-fluid no-print'):
            array.append(re.sub(' +',' ',tag.text))

        break

    today = datetime.datetime.today().weekday()
    food = array[today]

    # Create a list from the menu of the day
    food = food.split("\n")
    # Remove whatever is not a food string
    food = list(filter(lambda a: len(a) > 20, food))
    # Do some last prettifying
    food = [x.rstrip().lstrip() for x in food]

    todaysFood(food)

def todaysFood(array):
    '''
    Print the array in the desired format
    '''
    print("\n----------")
    print("DAGENS MAT")
    print("----------")
    for line in array:
        print("* " + line)