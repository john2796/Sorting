# -------------------------- Selection Sort --------------------------
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp
    # print('------- selection_sort -------- ', arr)
    return arr


# -------------------------- Bubble Sort --------------------------
def bubble_sort(arr):
    swapped = True
    while swapped is True:
        swapped = False
        print(arr)
        for i in range(0, len(arr) - 1):
            if arr[i+1] < arr[i]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swapped = True

    return arr

# js version
# function bubleSort(arr){
#   // check if left is greater than the right side
#   // need to repeat for loop as long something swapped
#     let swapped = true;
#     while (swapped) {
#     swapped = false
#     for(let i = 0; i < arr.length; i++){
#         if(arr[i] > arr[i + 1] ){
#           let temp = arr[i]
#           arr[i] = arr[i + 1]
#           arr[i + 1] = temp
#           swapped = true
#       }
#     }
#   }
#   return arr
# }
# bubleSort(bubbleArr)
# -------------------------- Count Sort --------------------------


def count_sort(arr, maximum=-1):

    return arr

# -------------------------- Insertion Sort --------------------------
# class Book:
#     def __init__(self, title, author, genre):
#         self.title = title
#         self.author = author
#         self.genre = genre

#     def __repr__(self):
#         return str(self.genre) + ": " + str(self.title) + " by " + str(self.author)


# harryPotter = Book('harryPotter', 'harryPotter ', 'gay')
# mbDick = Book('asdfharryPotter', 'ulolasdf ', 'adsf')
# awesomeBook = Book('awesome', 'uloladsf ', 'magicdasf')
# dirk = Book('dirk', 'dsaf ', 'dasf')

# books = []


# books.append(harryPotter)
# books.append(mbDick)
# books.append(awesomeBook)
# books.append(dirk)


# def insertion_sort(books):
#     for i in range(1, len(books)):
#         print(i)
