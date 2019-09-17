import sys
import os
import argparse
import  instagram_scraper.app as ap


path='friends.txt'

def data():
    with open("data.txt", 'r') as f:
        r=f.readlines()
        username=r[0].split(':')[1][:-1]
        password=r[1].split(':')[1]
    return username,password



u,p=data()
print(p)

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


x=message()
if x==1:
    follow_uu(u,p,path)
elif x==2:
    p=get_user_that_accept_you(u,p,path)
    os.system('cls')
    print('pepole has accept your request \n')
    print(p)
    print('\n')
elif x==3:
    ap.main(u,p)
else:
    os.system('cls')
