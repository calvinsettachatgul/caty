# my_arr = [1,2,3]

# for num in my_arr:
#     print(num)

from collections import defaultdict

    
book1 = {
    "title": "mobydick",
    "author": "Herman Melville"
}

book2 = {
    "title": "gone girl",
    "author": "Gillian Flynn"
}
    
book3 = {
    "title": "catcher in the rye",
    "author": "J. D. Salinger"
}

book4 = {
    "title": "tom sawyer",
    "author":"mark twain"
}

books = [book1, book2, book3, book4]

#for book in books:
#     print("*********************************************")
#     print("book title: {} \nbook author: {}\n".format(book["title"], book["author"]))
    
# iterate over an array and count the number of occurrences of each number
#

# [1,1,2,2,3,3] => { 1 : 2,
#                   2 : 2, 
#                   3 : 2} 

# keep a dictionary of the frequency
my_list = [1,1,2,2,3,3,3,4]

# iterate over the array
    # for num in my_list:
# when you come accross a number with a vvalue that is not defined yet
    #    if(freq[num] == None)
# initialze the count with 1
     #       freq[num] = 1
# when you come accross another occurrence (means that you saw the number again) incement the value by 1
        # else
        
# return the dictionary 

frequency = defaultdict(int)
'''
1 1 {1:1}
2 1 {1:2}
3 2 {1:2, 2:1}
4 2 {1:2, 2:2}
5 3 {1:2, 2:2, 3:1}
6 3 {1:2, 2:2, 3:2}
'''


for num in my_list:
    print(num)
    # increment the value of frequency at the number ie increment freqency[num]
    #frequency[num] += 1
    
    
#print(frequency)