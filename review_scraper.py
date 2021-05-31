from selenium import webdriver

website_url = 'https://www.amazon.in/'
driver = webdriver.Chrome('C:\\Users\\visha\\OneDrive\\Documents\\automation\\webdriver\\chromedriver.exe')
driver.get('https://www.amazon.in/Amazon-Brand-Shockproof-Cushioned-Transparent/product-reviews/B08511K5ZN/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')
alldetailsdict = {}

pageElements= driver.find_element_by_css_selector("div[class='a-form-actions a-spacing-top-extra-large']").find_element_by_css_selector("a")
pageLinks = pageElements.get_attribute('href') 

print(pageLinks)

#singlePageReviews=[]
#singlePageReviews = driver.find_elements_by_css_selector("div[class='a-section review aok-relative']")
#print(singlePageReviews)
#loopSinglePageReviews = [singlePageReview.get_attribute('id') for singlePageReview in singlePageReviews]

#print(len(loopSinglePageReviews))
#print(loopSinglePageReviews)
while pageLinks != None:
    singlePageReviews=[]
    singlePageReviews = driver.find_elements_by_css_selector("div[class='a-section review aok-relative']")
    #print(singlePageReviews)
    loopSinglePageReviews = [singlePageReview.get_attribute('id') for singlePageReview in singlePageReviews]
    for i in loopSinglePageReviews:

        ratingVal = ''
        rating = driver.find_element_by_id(i).find_element_by_class_name('a-icon-alt') 
        ratingVal = rating.get_attribute("innerHTML")
        rvalue=ratingVal[0]
        #print(rvalue)

        VP=''
        try:
            verifiedPurchase = driver.find_element_by_id(i).find_element_by_css_selector("span[data-hook='avp-badge']")
            VP = verifiedPurchase.get_attribute("innerHTML")
        except:
            VP = 0
        if VP =='Verified Purchase':
            VP_value=1
        else:
            VP_value=0
        #print(VP_value)

        reviewText=''
        text= driver.find_element_by_id(i).find_element_by_css_selector("span[data-hook='review-body']").find_element_by_css_selector('span')
        reviewText = text.get_attribute("innerHTML")
        #print(reviewText)

    alldetailsdict[i]={
        'R':rvalue,
        'VP': VP_value,
        'text':reviewText
    }
    try:
        pageElements= driver.find_element_by_css_selector("div[class='a-form-actions a-spacing-top-extra-large']").find_element_by_class_name('a-last').find_element_by_css_selector("a")
        pageLinks = pageElements.get_attribute('href')
    except:
        pageLinks=None
    try: 
        driver.get(pageLinks)
    except:
        pass
print(alldetailsdict)
with open('outputfile.txt', 'w') as f:
	f.write(str(alldetailsdict))
#driver.quit()





#for pageLink in pageLinks:
 #   driver.get(pageLink)
