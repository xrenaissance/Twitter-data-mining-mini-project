#coding: utf-8

import sys
import time
import linecache

start_time = time.time()

# Tuple for database attributes
data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 
    'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 
    'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 
    'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 
    'rt_ats', 'v_url', 'rt_v_url')

keys = {data_keys[k] : k for k in range(0, data_keys.__len__()) }
f = linecache.getlines("t.txt")
lines = [ line[1:-1].split('","') for line in f]

"""
@ author Egbert
Output total number of username 
"""

#1
users = set( [ element[keys['username']] for element in lines ] )
user_total = users.__len__()
#print (user_total)


#2 Output username List
user_list = list(users)
#print (user_list)
assert type(user_list) == list


#3 Output total number of twetts that sent in 11/2012
lines_from_2012_11 = list ( filter(lambda line:line[keys['created_at']].startswith('2012-11'), lines) )
lines_total_from_2012_11 = len(lines_from_2012_11)
#print (lines_from_2012_11[0])
#print (lines_total_from_2012_11)


#4 In this database, what days in this dataset
user_by_date = [ line[keys['created_at']].split(' ')[0] for line in lines]
user_by_date_list = sorted( list (  set(user_by_date) ) )
#print (  user_by_date_list[0:10] )
#print (len ( user_by_date_list))
#print (user_by_date[0:2]) just for test 


#5 In this database, output which period sent twitter most
# 2012-11-03 03:02:06"
# user_by_hour =[ int( line[keys['created_at']].split(' ')[1].split(':')[0] )for line in lines]
# user_by_hour_dict = dict ( [ (x, user_by_hour.count(x) ) for x in range(0,24) ] )
# user_by_hour_dict_sorted = sorted (user_by_hour_dict.items() ,key = lambda x : x[1], reverse = True)
# print (user_by_hour_dict_sorted[0])
# print (time.time() - start_time)

hours = [int(line[keys['created_at']][11:13]) for line in lines]

total_by_hour = [(h,hours.count(h)) for h in range(0,24) ]

total_by_hour.sort(key=lambda k:k[1],reverse=True)

max_hour = total_by_hour[0][0]
#print( max_hour )
#print (time.time() - start_time)


#6 read the dataset, output the user that send twieets most in a day
date_user_num_dict = { date : dict() for date in user_by_date_list } 
for line in lines: 
    date_in_line = line[keys['created_at']].split(' ')[0]
    user_in_line = line[keys['username']]
    if date_user_num_dict[date_in_line].__contains__(user_in_line):
       date_user_num_dict[date_in_line][user_in_line] += 1 
    else:
        date_user_num_dict[date_in_line][user_in_line] = 1 

for k,v in date_user_num_dict.items():
    v = sorted(v.items(), key = lambda k : k[1], reverse = True)
    date_user_num_dict[k] = { v[0][0] : v[0][1] } 
date_user_num_dict = sorted(date_user_num_dict.items(), key = lambda k : k[0])

#print (date_user_num_dict)
#print (time.time() - start_time)

#7 Output most frequency hour that sent twitter in 2012-11-03 
lines_for_2012_11_03 = list ( filter(lambda line : line[keys['created_at']].startswith('2012-11-03')  , lines_from_2012_11) )
lines_for_2012_11_03 = [ int (line[keys['created_at']].split(' ')[1][0:2]) for line in lines_for_2012_11_03]
#print (lines_for_2012_11_03[0:14])
frequency_dict_2012_11_03 = { hour : lines_for_2012_11_03.count(hour) for hour in range(0,24)} 
frequency_dict_2012_11_03 = sorted( frequency_dict_2012_11_03.items(), key = lambda k : k[1], reverse = True )
#print (frequency_dict_2012_11_03[0][0], frequency_dict_2012_11_03[0][1])
#print ("The time is %d, and the frequency is %d" % (frequency_dict_2012_11_03[0][0],  frequency_dict_2012_11_03[0][1]))
#print (time.time() - start_time)
#print "{time_in}, {number_in}".format(time_in = frequency_dict_2012_11_03[0][0], number_in = frequency_dict_2012_11_03[0][1])

#8 In the dataset, Output all of infomation of source and frequency
source_list = [ line[keys['source']] for line in lines]
# source_list_catagory = list( set(source_list) )
# frequency_source_list = {src : source_list.count(src) for src in source_list_catagory}
# frequency_source_list = sorted(frequency_source_list.items(), key = lambda k : k[1], reverse = True)
#print (frequency_source_list[0:11])
frequency_source_dict = dict()
for src in source_list:
    if frequency_source_dict.__contains__(src):
        frequency_source_dict[src] += 1
    else:
        frequency_source_dict[src] = 1
frequency_source_dict = sorted( frequency_source_dict.items(), key = lambda k : k[1], reverse = True )
#print ( frequency_source_dict[0:11])
#print ( time.time() - start_time )

#9 Calculate the the number of  Repost which starts with "https://twitter.com/umiushi_no_uta"
repost_list =list ( filter(lambda line : line[keys['rt_v_url']].startswith("https://twitter.com/umiushi_no_uta"), lines) ) 
print (len(repost_list))
# url_total = 0
# for line in lines:
#     if line[keys['rt_v_url']].startswith("https://twitter.com/umiushi_no_uta"):
#         url_total += 1
# print (url_total)
#print (time.time() - start_time)

#10 UID = 573638104, how many tweetts did this user send
user_5736_list = list ( filter(lambda line : line[keys['uid']] == '573638104' ,lines) )
print (len(user_5736_list))
#print (time.time() - start_time)

"""
### * means tuple,  ** means dict
11 Define a function, input uid could be any number of uid, if doesn't exit return null
otherwise return to uid that send twette most
"""
user_twetnum_dict = dict()
for line in lines:
    userid = line[keys['uid']]
    if user_twetnum_dict.__contains__(userid):
        user_twetnum_dict[userid] += 1
    else:
        user_twetnum_dict[userid] = 1
uid_list = list ( set( user_twetnum_dict.keys() ) )

def get_user_by_max_tweets(*uids):
    if len(uids) == 0:
        return 0
    else:
        uids = list( filter(lambda k : type(k) == int or k.isdigit(), uids ) ) 
        uids_dict = dict()
        for uid in uids:
            if uid_list.__contains__(uid):
                uids_dict[uid] = user_twetnum_dict[uid]
        uids_dict = sorted(uids_dict.items(), key = lambda k : k[1], reverse = True)
        if len(uids_dict) > 0:
            print (uids_dict[0][0], uids_dict[0][1])
        else:
            print ("null")


get_user_by_max_tweets()
get_user_by_max_tweets('ab', 'cds')
get_user_by_max_tweets('ab', 'cds', '123b')
get_user_by_max_tweets('12342', 'cd')
get_user_by_max_tweets('28803555',28803555)
get_user_by_max_tweets('28803555',28803555,'96165754')
get_user_by_max_tweets('96165754')
#print(time.time() - start_time)



#12 in this dataset, who sent longest twitter
twitter_user_length_dict = dict()
for line in lines:
    uid = line[keys['uid']] 
    twitt_length = len( line[keys['content']] )
    if twitter_user_length_dict.__contains__(uid): 
        if twitter_user_length_dict[uid] < twitt_length:
            twitter_user_length_dict[uid] = twitt_length
    else:
        twitter_user_length_dict[uid] = twitt_length
twitter_user_length_dict = sorted(twitter_user_length_dict.items(), key = lambda k : k[1], reverse = True)
#print (twitter_user_length_dict[0], twitter_user_length_dict[1], twitter_user_length_dict[2])
#print ( time.time() - start_time )
# list_user_by_content_length = [ ( line[keys['uid']], len(line[keys['content']])) for line in lines]
# list_user_by_content_length.sort(key = lambda k : k[1], reverse = True)
# print( list_user_by_content_length[0], list_user_by_content_length[1], list_user_by_content_length[2] )
# print (time.time() - start_time)


#13 in the dataset, who has most rp_url 
twiiter_user_repost_dict = dict()
for line in lines:
    uid = line[keys['uid']] 
    if line[keys['rt_num']] != "":
       repost_num = int ( line[keys['rt_num']] ) 
    else:
        continue
    if twiiter_user_repost_dict.__contains__(uid):
        if twiiter_user_repost_dict[uid] < repost_num:
            twiiter_user_repost_dict[uid] = repost_num
    else:
        twiiter_user_repost_dict[uid]  = repost_num
twiiter_user_repost_dict = sorted( twiiter_user_repost_dict.items(), key = lambda k : k[1], reverse = True )
#print ( twiiter_user_repost_dict[0])
#print ( time.time() - start_time)

#14 in the dataset, who sent twitter most at 11 o'clock
twiter_user_at_11 = dict()
for line in lines:
    user_name = line[keys['uid']]
    if int( line[keys['created_at']][11:13] ) == 11:
        if twiter_user_at_11.__contains__(user_name):
            twiter_user_at_11[user_name] += 1
        else:
            twiter_user_at_11[user_name] = 1
twiter_user_at_11 = sorted(twiter_user_at_11.items(), key = lambda k : k[1], reverse = True ) 
#print( twiter_user_at_11[0] )
#print( time.time() - start_time )

#15 in this dataset, which user has repost url most(output: uid: )

user_vurl_dict = dict()
for line in lines:
    uid = line[keys['uid']]
    if line[keys['v_url']] == "":
        continue
    else:
        if user_vurl_dict.__contains__(uid):
            user_vurl_dict[uid] += 1
        else:
            user_vurl_dict[uid] = 1
user_vurl_dict = sorted( user_vurl_dict.items(), key = lambda k : k[1], reverse = True)
print( user_vurl_dict[0], user_vurl_dict[1], user_vurl_dict[2] )
print( time.time() - start_time)
































