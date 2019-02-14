punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(string):
    i = 0
    while i<len(punctuation_chars):        
        if punctuation_chars[i] in string:
            string=string.replace(punctuation_chars[i], '')
        i += 1             
    return string
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(string1): 
    string1 = string1.split()
    count = 0
    for p in positive_words:        
        for s in string1:            
            if p == strip_punctuation(s):
                count += 1
            return count
    return count
            
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(st): 
    st = st.split()
    count = 0
    for n in negative_words:        
        for s in st:            
            if n == strip_punctuation(s):
                count += 1
            return count
    return count


file = open('project_twitter_data.csv', 'r')
lines = file.readlines()    
outfile = open("resulting_data.csv", "w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write('\n')
for line in lines[1:]:
    vals = line.strip().split(',')
    positive_score = get_pos(vals[0])
    negative_score = get_neg(vals[0])
    net_score = positive_score - negative_score
    out_line = "{}, {}, {}, {}, {}".format(vals[1], vals[2], positive_score, negative_score, net_score)
    outfile.write(out_line)
    outfile.write('\n')
outfile.close()




