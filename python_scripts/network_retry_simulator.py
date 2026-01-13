import random
urls = ["google.com", "facebook.com", "twitter.com", "amazon.com", "bing.com"]
responses = [501,200,305,404]
passed_tests = 0
failed_tests = 0
for url in urls:
    attempts = 0
    is_successful = False
    while attempts <= 2:
        response = random.choice(responses)
        attempts += 1
        if response == 200:
            print ("URL available")
            is_successful = True
            break
        else:
            print ("URL unavailable")
            is_successful = False
    if is_successful == True:
        passed_tests += 1
    else:
        failed_tests += 1
print (f"Testing complete. Passed: {passed_tests}, Failed: {failed_tests}")




