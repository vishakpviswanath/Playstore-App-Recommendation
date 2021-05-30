from selenium import webdriver

website_url = 'https://www.amazon.in/'
driver = webdriver.Chrome('C:\\Users\\visha\\OneDrive\\Documents\\automation\\webdriver\\chromedriver.exe')
driver.get('https://www.amazon.in/Butterfly-Premium-Vegetable-Chopper-Blue/product-reviews/B085F2HVF9/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&reviewerType=all_reviews&pageNumber=1')
alldetailslist = {}

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
        print(ratingVal)

        VP=''
        verifiedPurchase = driver.find_element_by_id(i).find_element_by_css_selector("span[data-hook='avp-badge']")
        VP = verifiedPurchase.get_attribute("innerHTML")
        print(VP)

        reviewText=''
        text= driver.find_element_by_id(i).find_element_by_css_selector("span[data-hook='review-body']").find_element_by_css_selector('span')
        reviewText = text.get_attribute("innerHTML")
        print(reviewText)

    pageElements= driver.find_element_by_css_selector("div[class='a-form-actions a-spacing-top-extra-large']").find_element_by_class_name('a-last').find_element_by_css_selector("a")
    pageLinks = pageElements.get_attribute('href')
    try: 
        driver.get(pageLinks)
    except:
        pass






#for pageLink in pageLinks:
 #   driver.get(pageLink)
