import matplotlib.pyplot as plt     #imports an API
dict = {}                           #assigns dictionary to list all the words
fo = open("BeautyATBeast.txt","r")   #reads the BeautyATBeast.txt
x = fo.read()                        #copies the file contents and inputs it in x
x = x.lower()                       #lowercases every letter
fo.close()                          #closes "BeautyATBeast.txt" in order to protect contents of the file
y = []                              #assigns an empty list to be appended from x

x = x.replace("”"," ").replace(","," ").replace("-"," ")\
    .replace("_"," ").replace('"' ," ").replace("."," ")\
    .replace(":"," ").replace(";"," ").replace("/"," ")\
    .replace("("," ").replace(")"," ").replace("!"," ")\
    .replace("?"," ")
#removes all the unused characters

y = x.split()                   #splits the words and appends them in array y


flag = 1                        #initialises the count of the word to be equal to 1
for word in y:                  #for each word in the array y
    if word in dict:            #checks if the word is already in the dictionary
        dict[word] += 1         #if it is, increases the flag of the word by 1
    else:
        dict[word] = flag       #if not, sets the word count to one and adds the word to the dictionary

print("DICTIONARY = ",dict)     #prints words-appended dictionary


fo = open("DictionaryOfBeautyAndTheBeast.txt", "w")
#opens "DictionaryOfBeautyAndTheBeast.txt", if it doesn't exist, creates and opens
fo.write(str(dict))     #writes dict to "DictionaryOfBeautyAndTheBeast.txt"
fo.close()              #closes "DictionaryOfBeautyAndTheBeast.txt" in order to protect contents of the file


sortedKey = list(sorted(dict, key=dict.__getitem__, reverse=True))  #decending sorts and puts elements into "sortedKey" list
top10Key = (sortedKey[:10])     #slices top 10 keys
print("Top 10 Keys = ",top10Key)    #prints top 10 keys

sortedValues = list(sorted(dict.values(),reverse=True))      #decending sorts and puts elements into "sortedValues" list
top10Values = (sortedValues[:10])   #slices top 10 Values
print("Top 10 Values = ",top10Values)   #prints top 10 Values

plt.plot(top10Key, top10Values)     #inserts top10Key and top10Values into a chart
plt.xlabel('Keys')  #gives a label @ x axis
plt.ylabel('Values')#gives a label @ y axis
plt.show()  #shows the chart

