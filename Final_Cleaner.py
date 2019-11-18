'''
Created on Nov 7, 2019
@author: Manchang Jin (eigenvector@tju.edu)
version: python3.7
'''


import os
path = os.path.abspath('.') + '\\final_track1_train_front100000.txt'
f_finish = open(os.path.abspath('.') + '\\finish_pre.txt', 'w')
f_like = open(os.path.abspath('.') + '\\like_pre.txt', 'w')

user_list_like = open(os.path.abspath('.') + '\\user_list_like.txt', 'w')
user_list_finish = open(os.path.abspath('.') + '\\user_list_finish.txt', 'w')

like_list = []
finish_list = []
with open(path) as f:
    for l in f.readlines():
        if len(l) > 0:
            l = l.strip('\n').split('	')
        if l[7] ==  '1':
            l_like = l[0] + ' ' + l[2]
            like_list.append(l_like)
            # f_like.write(l_like + '\n')
        if l[6] == '1':
            l_finish = l[0] + ' ' + l[2]
            finish_list.append(l_finish)
            # f_finish.write(l_finish + '\n')


    like_dict = dict()
    finish_dict = dict()

    for l_like in like_list:
        if l_like.split(' ')[0] not in like_dict.keys():
            like_dict[l_like.split(' ')[0]] = [l_like.split(' ')[1]]
        else:
            like_dict[l_like.split(' ')[0]].append(l_like.split(' ')[1])



    for l_finish in finish_list:
        if l_finish.split(' ')[0] not in finish_dict.keys():
            finish_dict[l_finish.split(' ')[0]] = [l_finish.split(' ')[1]]
        else:
            finish_dict[l_finish.split(' ')[0]].append(l_finish.split(' ')[1])

    for uid, user in enumerate([str(y) for y in sorted([int(x) for x in sorted(like_dict)])]):
        # 第一个 sorted 只是为了返回 dict 的键组成的 list, 然后转成 int 再进行排序, 再转成 str
        user_list_like.write(str(uid) + ' ' + user + '\n')
        f_like.write(str(uid) + ' ' + ' '.join([str(x) for x in like_dict[user]]) + '\n')


    
    for uid, user in enumerate([str(y) for y in sorted([int(x) for x in sorted(finish_dict)])]):
        user_list_finish.write(str(uid) + ' ' + user + '\n')
        f_finish.write(str(uid) + ' ' + ' '.join([str(x) for x in finish_dict[user]]) + '\n')



    f_like.close()
    f_finish.close()
    user_list_like.close()
    user_list_finish.close()


    
