import sys
import hashlib
import string
from itertools import chain, product


def bruteforce(charset, maxlength):
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(charset, repeat=i)
                                                 for i in range(1, maxlength + 1)))


# Passwords in memory
with open("passwords.txt", "r") as f:
    passwords = set([line.strip() for line in f])

users = set()
for line in sys.stdin:
    users.add(line.strip())


counter = 0
success = 0
for user in users:
    user = user.lower()
    # user + digit
    for randomDigit in bruteforce(string.digits, 4):
        counter += 1
        attempt = user+randomDigit
        wordDigit_hash = hashlib.md5(attempt.encode('utf-8')).hexdigest()
        for password in passwords:
            if password == wordDigit_hash:
                success += 1
                sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                    attempt, password, counter))
        sys.stdout.write("Attempt : {}, Success : {}\r".format(
            counter, success))
    # digit + user
    for randomDigit in bruteforce(string.digits, 4):
        counter += 1
        attempt = randomDigit + user
        wordDigit_hash = hashlib.md5(attempt.encode('utf-8')).hexdigest()
        for password in passwords:
            if password == wordDigit_hash:
                success += 1
                sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                    attempt, password, counter))
        sys.stdout.write("Attempt : {}, Success : {}\r".format(
            counter, success))

for user in users:
    user = user.lower()
    user = user.capitalize()
    #user + digit
    for randomDigit in bruteforce(string.digits, 4):
        counter += 1
        attempt = user+randomDigit
        wordDigit_hash = hashlib.md5(attempt.encode('utf-8')).hexdigest()
        for password in passwords:
            if password == wordDigit_hash:
                success += 1
                sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                    attempt, password, counter))
        sys.stdout.write("Attempt : {}, Success : {}\r".format(
            counter, success))
    # digit + user
    for randomDigit in bruteforce(string.digits, 4):
        counter += 1
        attempt = randomDigit + user
        wordDigit_hash = hashlib.md5(attempt.encode('utf-8')).hexdigest()
        for password in passwords:
            if password == wordDigit_hash:
                success += 1
                sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                    attempt, password, counter))
        sys.stdout.write("Attempt : {}, Success : {}\r".format(
            counter, success))

# UsEr
new_users = []
for user in users:
    char_list = []
    for i in range(len(user)):
        if i % 2 == 0:
            char_list.append(user[i].upper())
        else:
            char_list.append(user[i].lower())
    new_users.append(''.join(char_list))

for new_user in new_users:
    new_user_hash = hashlib.md5(new_user.encode('utf-8')).hexdigest()
    counter += 1
    for password in passwords:
        if password == new_user_hash:
            success += 1
            sys.stdout.write("The password = {} match hash : {} after {} attempts\n".format(
                new_user, password, counter))
    sys.stdout.write("Attempt : {}, Success : {}\r".format(
        counter, success))
