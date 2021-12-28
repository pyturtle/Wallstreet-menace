import praw
import bisect 
import datetime
import time
import re

api_key = "QV6C75GFGAKV9QJN"



reddit = praw.Reddit(
    client_id="lUlZOUEW2WJ4Ig",
    client_secret="exoIZ1cApRCHSbxD4AeKs0enyynPTA",
    user_agent="<console:WALLSTREET: 1.0>",
)

def punctuatio_remover(s):
    punc_list = [".",";",":","!","?","/","\\",",","#","@","$",")","(","'s","\""]
    new_s = ''
    for i in s:
        if i not in punc_list:
            new_s += i
        else:
            new_s += ' '
    return new_s

def hasNumbers(inputString):
    return not bool(re.search(r'\d', inputString))

def retreaving_stock_price (ticker,submission_date):
    end_date = datetime.datetime.today()
    start_date = submission_date
    


def determine_grade(scores, breakpoints=[50, 60, 70, 80, 90], grades='FEDCBA'):
    i = bisect.bisect(breakpoints, scores)
    return grades[i]



def bull_or_bear_rating(subreddit, style,amount):
    bull_list = [" bullish ", " up ", " push ", " bought ", " buy ", "calls ", " moon ", " all in ",
                 " bull ", " good ", " got ", " love ", " print ", " with you", " holding", " diamond ",
                  " buying ", " hold ", " higher ", " proud ", "break past", " holy ", " raking ", " smoking ",
                   " got ", " gains ", " in"," hero " , " support "," yolo ", " purchase ", " long ", ' fuckking love '
                   ," best ", " legend ", " solid ", " nice ", " congrats ", " godspeed ", " i like the ", " gang "," solid ", " dd ", " long term ", " doubling "]
    
    bear_list = [" retarded "," shrooms ", " puts ", " bearish ", " retard ", " sold ", " yikes ", " dumb "
    , " dumbest "," idiot ", " dumbass ", " short ", " lost ", "crashing", " retardest ", "sell "] 

    
    term_list = ["YOLO", "DD","SIKE","WSB","SEC","HOLD","FOMO","DFV","RH","I"]
#top("day", limit=100)
    subreddit = reddit.subreddit(subreddit)
    
    A_grade_post = []

    for submission in subreddit.top(style, limit=amount):
        submission_words = submission.title.split()
        ticker_tags = []
        ticker_amount = 0
        for words in submission_words:
            word1 = punctuatio_remover(words)
            if word1.isupper() and hasNumbers(word1):
                if any(upper in word1 for upper in term_list):
                    pass
                else:
                    ticker_tags.append(word1)
                    ticker_amount = ticker_amount+1







        if (ticker_amount>0):
            cashtags = ticker_tags
            print("----------------")
            print(cashtags)
            print(submission.title)
            submission_date = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(submission.created_utc)))
            print(submission_date)
            buy_rating = 0
            sell_rating = 0
            total_ratings = 0
            
            for comment in submission.comments:
                if hasattr(comment, "body"):
                    comment_lower = punctuatio_remover(comment.body).lower()
                    comment_lower = comment_lower.center(len(comment_lower)+2)
                    if any(buys in comment_lower for buys in bull_list):
                        buy_rating += 1
                    if any(sells in comment_lower for sells in bear_list):
                        sell_rating += 1

            
            buy_sell_ratio = (str(buy_rating) + "/" + str(sell_rating))
            total_ratings = sell_rating + buy_rating
            sell_percentage = (sell_rating/total_ratings)*100
            buy_percentage = (buy_rating/total_ratings)*100
            
            print ("The consensus on the post leaves an aproval/buy rating of " + str(round(buy_percentage, 1)) + "%' and sell of " + str(round(sell_percentage,1)) + "%" + 
            "\n" + "With a buy to sell ratio of " + buy_sell_ratio + " and grade of " + determine_grade(buy_percentage) + 
            "\n" + "The post has " + str(submission.score) + " upvotes"+
            "\n" + submission.permalink)
            if determine_grade(buy_percentage) == "A":
                A_grade_post.append(ticker_tags)

    print(A_grade_post)

        

#r/investing        r/wallstreetbets
def main():
    subreddit = ("wallstreetbets")
    bull_or_bear_rating(subreddit, "year",15)
    



if __name__ =="__main__":
    main()
            

        
