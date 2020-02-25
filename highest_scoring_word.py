# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.



def high(x):
    scoreboard=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    heck = x.split()
    score=0
    score_final=0
    big_word=[]
    for each in heck:
        print(each)
        for every in each:
            if every in scoreboard:
                score= score + scoreboard.index(every) + 1
                print(score)
        if score > score_final:
            score_final = score
            big_word = each
            score = 0
        else:
            score = 0
    return big_word
    # Code here 54
    
    #for every in word: if every in scoreboard, score + every.index()