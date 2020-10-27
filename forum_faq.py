
"""
@author: rakeshr
"""

"""
FAQ generator for Kite connect Forum
"""

import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz


class FaqGenerator(object):
    """
    FAQ generator for kite connect Forum
    """
    def __init__(self, pages, match_factor):
        self.pages = pages
        self.match_factor = match_factor
        self.headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        self.forum_URL = 'https://kite.trade/forum/discussions/p'

    def read_forum(self):
        """
        Scrape questions from forum and 
        generate processed data
        """
        question_list = []
        for pageNo in range(1,self.pages):
            request_url = '{}{}'.format(self.forum_URL,pageNo)
            response = requests.get(request_url, headers=self.headers)
            soup = BeautifulSoup(response.text, "lxml")
            result = soup.find_all("div", class_="Title")
            for title in result:
                # Remove all whitespaces at end/start of the sentense, new line notation 
                title_text = title.text.replace('\n', '').rstrip()
                question_list.append(title_text)
        return question_list
    
    def question_match(self):
        """
        Generate list of similar questions using
        fuzzy-wuzzy string matching %
        """
        faq_list = []
        # List of processed data
        pro_data = self.read_forum() 
        pointer = 0
        while pointer < len(pro_data): 
            tmp_list = [pro_data[pointer]]
            # Start comparing string from backward till current pointer
            for j in range(len(pro_data)-1,pointer,-1):
                match_value = fuzz.token_set_ratio(tmp_list[0], pro_data[j])
                if match_value > self.match_factor:
                    tmp_list.append(pro_data[j])
                    # Remove specific element from list once matched to remove duplicacy
                    pro_data.pop(j)
                    continue
            pointer += 1
            # Create list of FAQs
            if len(tmp_list) > 1:
                faq_list.append(tmp_list)
        # Sort sub-list by list size/length
        faq_list.sort(key = len, reverse=True)
        return faq_list

    
    
