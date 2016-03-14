# stream-tweets
This file helps us to track down the most used words on twitter, restricted by the following conditions:  
The words are scored as following:  
• Every time a word is seen, it’s score goes up by 1.  
• Every minute the word is not seen, it’s score goes down by 1. This scoring is done every 30 seconds.  
Once the score of a word falls below 0, it is pruned.  
New entries have score 1. Words with score 0 can be dropped to make space for new entries if maximum number of words have already been stored(this number can be decided apriory).  
It can be a great way to visualize the basis of 'trending' feature on social media platforms.
## What was the idea to be explored?
• First, suppose we somehow get the live streaming twitter data and convert them to set of words. Can the objective be fullfilled now?  
• Second, how can we get those live streaming data from twitter and convert them to set of words?
## Playing around the problems
### Tackling the first one
Suppose, we somehow get the live streaming twitter data and convert them to set of words. We have to store the corresponding score and time(when was the entry modified) pair also. Now as we stream more and more data, we can update score and time. With the updated score and time we can carry out the remaining operations.
### The second step
For live streaming twitter data, we can use Twitter Streaming API. It is the key to data for all the remaining opertions. We should somehow be able to use the builtin library functions to exploit the data.  

Considering the above ideas and arguments, we can see a lot of possibilities for python here. Python has a large number of libraries which include 'Tweepy'. Tweepy is built for manipulating the twitter data in many ways, some of which we shall . Also, python has a bunch of useful data structures like dictionary, list or string which we can observe to be used here a lot. Therefore, our final implementation can be in python.
### The Final Implementation
