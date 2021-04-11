import pywikibot
from pywikibot import pagegenerators
import numpy as np

# Connect to ptwiki
enwiki = pywikibot.Site('en', 'wikipedia')
# and then to wikidata
enwiki_repo = enwiki.data_repository()


## function to add sometihng in the page
def editarticle(page):
    text = page.get()
    text = text + "\n hello, i am pushpanjali"
    page.text = text
    try:
        page.save("Saving test edit")
        return ("Save worked")
    except:
        print ("That didn't work!")
        return ("Error")

        
#get the information about article from Q-value assigned in wikidata

def printwikidata(wd_item):
    qid = wd_item.title()
    print (qid)

    item_dict = wd_item.get()

    try:
        print ('Name: ' + item_dict['labels']['en'])
    except:
        print ('No English label!')
    try:
        print (item_dict['claims']['P31'])
    except:
        print ('No P31')

    try:
        for claim in item_dict['claims']['P31']:
            p31_value = claim.getTarget()
            p31_item_dict = p31_value.get()
            print ('P31 value: ' + p31_value.title())
            print ('P31 label: ' + p31_item_dict['labels']['en'])
    except:
        print ("That didn't work!")
    return ("function work is done")

def editwikidata(wd_item, propertyid, value):
    qid = wd_item.title()
    print (qid)
    item_dict = wd_item.get()

    claim_target = pywikibot.ItemPage(enwiki_repo, value)
    newclaim = pywikibot.Claim(enwiki_repo, propertyid)
    newclaim.setTarget(claim_target)

    print (newclaim)
    text = input("Save? ")
    if text == 'y':
        wd_item.addClaim(newclaim, summary=u'Adding test claim')

    return ("editing done")



# accessing page made for task1 

page = pywikibot.Page(enwiki_repo, 'User:Pushp24/Outreachy 1')
test = editarticle(page)
print(page.text)
#print the atricle with added text
print (test)
# test = editarticle2(page)
test1=input("please enter data item for which you want to see details?")
wd_item = pywikibot.ItemPage(enwiki_repo, test1)
printwikidata(wd_item)
print('\n')


# Assigning Q-value in the code
testqid = 'Q4115189' # Wikidata sandbox
testproperty = 'P31' # instance of
testvalue = 'Q3938'  # Sandbox

wd_item = pywikibot.ItemPage(enwiki_repo, testqid)
printwikidata(wd_item)
dictionary = wd_item.get()
print(dictionary)


editwikidata(wd_item, testproperty, testvalue)
