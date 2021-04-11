# import requests

# # You may need to enforce the use of utf-8
# import sys
# reload(sys)
# sys.setdefaultencoding('UTF8')
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
        return 1
    except:
        print ("That didn't work!")
        return 0

# def editarticle2(page):
    # text = page.get()
    # text = text.replace('This is a test edit','Isto é uma edição de teste')
    # page.text = text
    # try:
        # page.save("Saving test edit")
        # return 1
    # except:
        # print "That didn't work!"
        # return 0
        
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
    return 0

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

    return 0

# def parsesite(url):
    # try:
        # r = requests.get(url)
        # websitetext = r.text
    # except:
        # print ('Problem fetching page!')
        # return 0
    # # print websitetext
    # split = websitetext.split("<h1 style='display:none'>")
    # i = 0
    # for item in split:
        # i+=1
        # # Skip the top part
        # if i > 2:
            # # print item
            # print ('Title: ' + item.split('</h1>')[0].strip() + '\n')
            # print ('Museum: ' + item.split("strong>Museu:</strong><span itemprop='publisher'>")[1].split("</span>")[0].strip() + "\n")
    # return 0

# From https://gist.github.com/ettorerizza/7eaebbd731781b6007d9bdd9ddd22713
# def search_entities(site, itemtitle):
     # params = { 'action' :'wbsearchentities', 
                # 'format' : 'json',
                # 'language' : 'en',
                # 'type' : 'item',
                # 'search': itemtitle}
     # request = api.Request(site=site, parameters=params)
     # return request.submit()

# accessping page made for task1 

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

# page = pywikibot.ItemPage(ptwiki_repo, 'Q511405')
# test = printwikidata(page)

# sparql = "SELECT ?item WHERE { ?item wdt:P31 wd:Q184356 } LIMIT 10"
# generator = pagegenerators.WikidataSPARQLPageGenerator(sparql, site=ptwiki_repo)
# for page in generator:
    # printwikidata(page)

# targetcat = 'Categoria:Telescópios'
# cat = pywikibot.Category(ptwiki, targetcat)
# subcats = pagegenerators.SubCategoriesPageGenerator(cat, recurse=False);
# for subcat in subcats:
    # print subcat.title()

# pages = pagegenerators.CategorizedPageGenerator(cat, recurse=False);
# for page in pages:
    # print page.title()

# template = pywikibot.Page(ptwiki, 'Predefinição:Info/Telescópio')
# targets = template.embeddedin()
# for target in targets:
    # print target.title()

# targets = pagegenerators.RandomPageGenerator(total=10, site=ptwiki, namespaces='14')
# for target in targets:
    # print target.title()

# wikidataEntries = search_entities(ptwiki_repo, "Neuromat")
# if wikidataEntries['search'] != []:
    # results = wikidataEntries['search']
    # numresults = len(results)
    # for i in range(0,numresults):
        # qid = results[i]['id']
        # label = results[i]['label']
        # print qid + " - " + label

# Assigning     Q-value in the code
testqid = 'Q4115189' # Wikidata sandbox
testproperty = 'P31' # instance of
testvalue = 'Q3938'  # Sandbox

wd_item = pywikibot.ItemPage(enwiki_repo, testqid)
printwikidata(wd_item)
dictionary = wd_item.get()
print(dictionary)


editwikidata(wd_item, testproperty, testvalue)