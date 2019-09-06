import sys
import os
import argparse
import  instagram_scraper.app as ap
from multiprocess import Pool
import multiprocess as mp



path='friends.txt'
with open('friends.txt','r') as a:
    a=a.read()
all_urls=a.split()
##


def data():
    with open("data.txt", 'r') as f:
        r=f.readlines()
        username=r[0].split(':')[1][:-1]
        password=r[1].split(':')[1]
    return username,password



u,p=data()

def message():
    return(int(input( '\n1-Follow users from file\n2-show users have accepted request\n3-scrape users\n Enter:')))
    
    

def get_user_that_accept_you(u,p,path):
    sys.path.append(os.path.join(sys.path[0], '../'))

    from instabot import Bot

    bot = Bot()
    bot.login(username=u, password=p)
    f_users=bot.get_user_following(u)
    f_file =bot.read_list_from_file(path)

    r=[]
    for x in range(len(f_file)):
        if bot.convert_to_user_id(f_file[x]) in f_users:
            r.append(f_file[x])
    return r




def follow_uu(u,p,path):
    sys.path.append(os.path.join(sys.path[0], '../'))
    from instabot import Bot

    bot = Bot(filter_users=False)
    users_to_follow = bot.read_list_from_file(path)
    if not users_to_follow:
        exit()
    else:
        print("Found %d users in file." % len(users_to_follow))

    bot.login(username=u, password=p)

    bot.follow_users(users_to_follow)
    
if __name__=='__main__':
    pp = Pool(95)
    pp.map(ap.main,all_urls)
    pp.terminate()
    pp.join()


    
    
