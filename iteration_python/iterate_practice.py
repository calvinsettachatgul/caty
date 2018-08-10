# my_arr = [1,2,3]

# for num in my_arr:
#     print(num)
    
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

for book in books:
    print("*********************************************")
    print("book title: {} \nbook author: {}\n".format(book["title"], book["author"]))