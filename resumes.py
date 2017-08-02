from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
import os.path
import time

t = 0.5
pixels = 0
increment = 100

signin_email = raw_input("Email Id: ")
signin_password = raw_input("Password: ")
position = raw_input("Position/Role: ")
location = raw_input("Location: ")

while 1: 
	try:
		# Create a new instance of the Firefox driver
		driver = webdriver.Chrome()

		# go to the google home page
		driver.get("https://secure.indeed.com/account/login?service=my&hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F")

		# Page 1
		tag = driver.find_element_by_id("signin_email")
		tag.send_keys(signin_email)
		tag = driver.find_element_by_id("signin_password")
		tag.send_keys(signin_password)
		tag.submit()

		# After logging in, find the resume link
		tag = driver.find_element_by_id("rezLink")
		tag.click()

		# Selecting the job title/position
		tag = driver.find_element_by_id("query")
		tag.send_keys(position)
		tag = driver.find_element_by_id("location")
		tag.clear()
		tag.send_keys(location)
		tag.submit()

		# On the list of resumes page

		number = 0
		while 1:
			pixels = 0
			tag = driver.find_element_by_id("results")
			people = tag.find_elements_by_tag_name("li")
			for i in people:
				
				time.sleep(t)
				driver.switch_to.window(driver.window_handles[-1])
				time.sleep(t)
				driver.execute_script("window.scrollTo(0, " + str(pixels) + ");")
				pixels = pixels + increment
				time.sleep(t)
				i.find_elements_by_tag_name("div")[0].find_elements_by_tag_name("div")[1].find_elements_by_tag_name("div")[0].find_elements_by_tag_name("a")[0].click()
				time.sleep(t)
				driver.switch_to.window(driver.window_handles[-1])
				time.sleep(t)
				name = driver.find_element_by_id("resume-contact").text
				time.sleep(t)
				if os.path.isfile(name.replace(" ", "-") + ".pdf"):
					print "Skipping " + name
					time.sleep(t)
					driver.close()
					continue
				driver.find_element_by_id("download_pdf_button").click()
				time.sleep(t)
				number = number + 1
				print str(number) + ". " + name
				driver.close()
				

			driver.switch_to.window(driver.window_handles[-1])
			driver.find_element_by_class_name("next").click()
	except:
		print "Exception caught"
		driver.close()
		print "Sleeping for 200 seconds"
		time.sleep(200)
		continue

	
	



# the page is ajaxy so the title is originally this:


# # find the element that's name attribute is q (the google search box)
# inputElement = driver.find_element_by_name("confirm-nav next")

# # type in the search
# inputElement.send_keys("cheese!")

# # submit the form (although google automatically searches now without submitting)
# inputElement.submit()

# try:
#     # we have to wait for the page to refresh, the last thing that seems to be updated is the title
#     WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

#     # You should see "cheese! - Google Search"
#     print driver.title

# finally:
#     driver.quit()