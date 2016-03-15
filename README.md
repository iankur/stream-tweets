# stream-tweets
This program helps us to track down the most used words on twitter, restricted by the following conditions:  
The words are scored as following:  
* Every time a word is seen, it’s score goes up by 1.  
* Every minute the word is not seen, it’s score goes down by 1. This scoring is done every 30 seconds.  
Once the score of a word falls below 0, it is pruned.  
New entries have score 1. Words with score 0 can be dropped to make space for new entries if maximum number of words have already been stored(this number can be decided apriory).  
It can be a great way to visualize the basis of 'trending' feature on social media platforms.

## What was the idea to be explored?  
* First, suppose we somehow get the live streaming twitter data and convert them to set of words. Can the objective be fullfilled now?  
* Second, how can we get those live streaming data from twitter and convert them to set of words?

## Playing around the problems
### Tackling the first one
Suppose, we somehow get the live streaming twitter data and convert them to set of words. We have to store the corresponding score and time(when was the entry modified) pair also. Now as we stream more and more data, we can update score and time. With the updated score and time we can carry out the remaining operations.
### The second step
For live streaming twitter data, we can use Twitter Streaming API. It is the key to data for all the remaining opertions. We should somehow be able to use the builtin library functions to exploit the data.  

Considering the above ideas and arguments, we can see a lot of possibilities for python here. Python has a large number of libraries which include 'Tweepy'. Tweepy is built for manipulating the twitter data in many ways, some of which we shall . Also, python has a bunch of useful data structures like dictionary, list or string which we can observe to be used here a lot. Therefore, our final implementation can be in python.
### The Final Implementation
* My final implementation is in python programming language. I have used 'Tweepy' library to use Twitter Streaming API.
* To use the Twitter Streaming API we should have consumer key and consumer secret, which one can obtain by registering an application on Twitter developer website.  
* Any application uses some API, in this case the Twitter Streaming API, means that it uses data on behalf of some user. Therefore, it should have some access key and access secret to be able to access data. In this case, I have used my own set of keys. But if various users were to run this program as an application then there should be a mechanism to retrieve access key and secret from Twitter on each user's behalf.  
* Once the application has been authenticated, using the streaming API consists of three steps:
  1. Create a class inheriting from StreamListener: This class is important since the incoming data is routed to instance of this class. The 'on_data' method recieves all data and then calls subsequent methods. Therefore, we can manipulate this method as well as class to adjust to our needs. The 'on_data' method should return 'True' to recieve further streams.
  2. Using that class create a Stream object: We need to create a Stream object before we start streaming. Once we have our inherited from StreamListener and created an api object, we are ready to create our Stream object.
  3. Connect to the Twitter API using the Stream: Finally we start streaming with the help of 'filter' method to track all tweets containing the given keyword. This keyword cab be an input from the user.  
* When I recieve streams, I convert it into python object(a dictionary) with the help of JSON and extract 'tweets' from this dictionary using the key 'text'(JSON processes data that way).  
* I do some preprocessing on this data,i.e., I remove the user name(the person who tweeted) and hyperlinks, if any, from the text I get with the help of regular expressions. Now I split this text to get a list of words which are to be tracked down.
* I have used python dictionary to store the words, their scores and time of modification. This dictionary has words as key and a list as value, where the first element of list is the score of that key and second element is corresponding time.
* Every time I get a list of words, I update my dictionary. If a word is already present in the dictionary, I simply update its score and time. Else I insert that word in the dictionary. If the size of dictionary becomes the specified value, I delete those elements from the dictionary which have 0 as score. After every 30 seconds, I update the dictionary,i.e., all the words which have been modified 60 seconds earlier or more, get their score decreased by one(also, if in the process, score becomes negative I delete that entry). After every 60 seconds, I print the words in the dictionary with their score.  

### Challenges Faced
* Key Error: 'text'  
	When implemented, initially the program appeared to run properly. However, every execution of the program used to terminate with an exception raised - KeyError: 'text'. On exploring the term it appeared that the key 'text' was being accessed even when it was missing in the dictionary(but which dictionary, it was not clear). Thoroughly checking the program I made sure that there was nothing wrong with my dictionary implementation. Even then the problem would arise. Therefore the only possibility was while accessing 'tweets' from the streamed data with key 'text'. What the problem was, in some streamed data there was no 'text' or tweet. So I fixed the code to process streamed data only when there is actually any tweet.

### Some scope of Improvement
* I have implemented dictionary, maximum size and time with global variables. However, a better idea can be to implement these variables as instance variables.
* This program assumes that words are case sensitive,i.e., word with a lowercase letter is different from the same word but having the same letter in uppercase. 

IN CASE OF ANY ISSUES, PLEASE LET ME KNOW BY DROPPING A MAIL AT ankurk@iitk.ac.in
