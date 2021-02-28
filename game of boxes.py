import random

import cv2

thislist = [10,10,10]
random_box =0
random_object=0
x = 0
print(thislist)
flag =0
while thislist[0] != 0 or thislist[1] != 0 or thislist[2] != 0:

    if (x % 2 == 0):

         while True:



             print("Select a bag: ")
             bag_no = input()
             bag_no = int(bag_no)

             print("Select number of objects: ")
             no_of_objectd = input()
             no_of_objectd = int(no_of_objectd)

             if bag_no <= 3 and  1 <= bag_no:

                 if(no_of_objectd <= 5):

                     if thislist[bag_no - 1] >= no_of_objectd:
                         thislist[bag_no - 1] = thislist[bag_no - 1] - no_of_objectd
                         print(f"You took: {no_of_objectd} objects from Bag {bag_no}")
                         print(thislist)
                         flag = 0
                         break

                     elif ((no_of_objectd >= 1 and no_of_objectd <= 5) and thislist[bag_no] < no_of_objectd):
                         print("You cannot remove this number.")

                     else:
                         print("Please enter a valid number.")
                 else:
                     print("please choose less than 5 balls or equal")

             else:
                 print("Please select a correct bag.")

    if(x%2 != 0):

         while True:


             if thislist[0] > 0 and thislist[1] > 0 and thislist[2] > 0:
                 random_box = random.randrange(1, 3)
                 random_object = random.randrange(1, 5)

             elif thislist[0] > 0 and thislist[1] > 0:
                 random_box = random.randrange(1, 2)
                 random_object = random.randrange(1, 5)

             elif thislist[0] > 0 and thislist[2] > 0:
                 random_box = random.randrange(1, 3, 2)
                 random_object = random.randrange(1, 5)

             elif thislist[1] > 0 and thislist[2] > 0:
                 random_box = random.randrange(2, 3)
                 random_object = random.randrange(1, 5)

             elif(thislist[0] > 0):
                 random_box = 1
                 random_object = random.randrange(1, 5)

             elif thislist[1] > 0:
                 random_box = 2
                 random_object = random.randrange(1, 5)

             else:
                 random_box = 3
                 random_object = random.randrange(1, 5)


             if thislist[random_box-1] != 0 and thislist[random_box-1] >= random_object:
                 thislist[random_box - 1] = thislist[random_box - 1] - random_object
                 print(f"Computer took: {random_object} objects from bag: {random_box}")
                 print(thislist)
                 flag =1
                 break

    x =x+1


if flag == 1:
    image = cv2.imread('D:\pic\download.png')
    cv2.imshow('Welcome', image)
else:
    image = cv2.imread('D:\pic\winner.png')
    cv2.imshow('Welcome', image)


cv2.waitKey(0)
cv2.destroyAllWindows()