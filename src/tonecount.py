import re
import json

def tone_count(the_text):
    if 'regex_list' in tone_count.__dict__:
        regex_list = tone_count.__dict__["regex_list"]
        categories = tone_count.__dict__["categories"]
    else:
        with open("tone.json", "r") as f:
            data = json.load(f)
        categories = list(data.keys())
        categories.remove("category")
        mod_word_list = {}
        for cat in categories:
            file_name = f"{cat}.csv"
            with open(file_name, "r") as f:
                word_list = f.read().splitlines()
            mod_word_list[cat] = [word.lower() for word in word_list]
        # Pre-compile regular expressions.
        regex_list = {}
        for key in mod_word_list.keys():
            regex = '\\b(?:' + '|'.join(mod_word_list[key]) + ')\\b'
            regex_list[key] = re.compile(regex)
        tone_count.__dict__["regex_list"] = regex_list
        tone_count.__dict__["categories"] = categories
 
    # rest of function
    """Function to return number of matches against a LIWC category in a text"""
    text = re.sub(u'\u2019', "'", the_text).lower()
    the_dict = {category: len(re.findall(regex_list[category], text)) for category in categories}
    return json.dumps(the_dict)



with open("/Users/jomarjordas/Documents/MSFIN299/MSFIN299-Research/notebooks/MEG_2017.txt","r") as f:
    the_text = f.read()

tone_count(the_text)