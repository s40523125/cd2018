import re
with open("2a.txt") as ml:
    #�N2a.txt�ɮ׶}��, �R�W��ml��"�C��".
    mushroom = ml.readlines()
    #�v��Ū�Jml��"�C��",�N��R�W��mushroom
    mushroom = [(re.findall('405\d\d\d\d\d', mushroom[i])) for i in range(len(mushroom))]
    #�ϥ�re��"�M��"(findall)�bmushroom"�C��"����X�}�Y��405xxxxx��"�r��".
    #�ϥ�len��Xmushroom��"����""�d��",�ϥ�for"�j��"�ƥXmushroom��"�C��"�éR�W���N��"i".

num = 0
#�Nnum�q�s�}�l
for a in range(len(mushroom)):
#�ϥ�len��Xmushroom��"����""�d��",�ϥ�for"�j��"�ƥXmushroom��"�C��"�éR�W���N��"a".
    row = mushroom[a]
    #�Nmushroom[a]�R�W��row
    for b in range(len(row)):
    #�ϥ�for"�j��"�ƥXrow��"�C��"�éR�W���N��"b".
        if b%3 == 0:
        #���]�N��"b"(row������)��Q�T�㰣.
            num += 1
            #�����H�W�����, num�[�@.
            print('��' + str(num) +'��:' + str(row[b:b+3]))
            #"���"�X���G��('��' + "�r��"num + '��:' + "�r��"row��"����"�qb�}�l��b+3.