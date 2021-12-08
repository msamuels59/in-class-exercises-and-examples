# Warm Up - fix this function.

# This function is supposed to take a list of words and return a new 
# list with the one-letter words removed. It's not doing that. First,
# run the function with some test word lists to see what it is doing
# then fix it so it has the desired output.

def remove_short_words(word_list):
    scrubbedList = [x for x in word_list if len(x) > 1]
    print (scrubbedList)
    return scrubbedList

test_list =['knee','a','append']

remove_short_words(test_list)
