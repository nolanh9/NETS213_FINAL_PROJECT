# NETS213_FINAL_PROJECT
<!-- Output copied to clipboard! -->

<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 0.651 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β29
* Tue Apr 13 2021 16:37:40 GMT-0700 (PDT)
* Source doc: ReadMe
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 1.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



# NETS 213 Final Project


## Overview

Our project focuses on the biases and political skews of United States based tweets. We use advanced Natural Language Processing techniques and deep learning models to learn how to classify tweets based on political leaning. Ultimately, we will be able to map tweet text to a linear political spectrum, between consertative and liberal.



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")



## Twitter Data Collection

This component of the project deals with pulling tweets from Twitter into a CSV that will be used to populate the HITs on Mechanical Turk. We will use Tweepy to pull tweets from various political commentators on Twitter. The users we will focus on will be politicians, politically inclined celebrities, political pundits, and popular users not necessarily connected to politics (to provide an ample amount of apolitical tweets). We will then clean these tweets to remove images and explicit language. The different components and work required are detailed below:



*   Write a script to pull tweets from a given set of users (1 point)
*   Write a script to clean tweets, removing tweets with images or explicit content (1 point)


## Mechanical Turk HITs and Quality Control



*   Create the preliminary QC survey that consists of 5 tweet rating questions touching on the various political affiliations to gauge literacy in this area and support this gold standard we want to achieve. There will be 2 questions which are ‘left-leaning’, 2 questions which are ‘right-leaning’, and one which has no political relevance what-so-ever. (1 point)
*   Write a script to verify the correctness of the worker responses on the survey. (1 point)
*   Create the architecture for the general HITs that will consist of a random tweet from the dataset along with a few options to rate the tweet on the political spectrum. (3 points)


## Data Aggregation

Data aggregation will consist of compiling each of our separate data sets from online resources, and the data sets scraped from Twitter using Tweepy. Will will not need to perform feature extraction, however much data wrangling and entity resolution will be required in order to mold our data to a usable state.



*   Combination of datasets (1 point)
*   Data wrangling and entity resolution (5 points)


## Model

We are going to train and finetune a pre-trained transformer model using Pytorch’s transformer library. Specifically, we want to utilize the Bidirectional Encoder Representations from Transformers (also known as BERT) model to label an embedding of our tweets on a scale between 0 and 10. We are going to take the pretrained BERT model and change the final fully connected layer to a couple linear layers that we softmax and then we regularize between 0 and 10. (5 points)


## Applications


### Political Analysis of a User’s Timeline

We can perform analysis on an entire user’s timeline. After training our language model, we can output a “political rating” class for a given tweet based on the model that’s trained using MTurk labels. To analyze a user’s timeline, we can call the Twitter API to get all tweets by a given user, then use our model to predict labels for each tweet, keeping a running average as we go through each tweet. We can then come up with a political score for the user, to see where they lie on the political spectrum.


### Political Analysis of a User’s Profile

As an extension of our ability to analyze a user’s timeline, we will be also able to analyze a user’s profile with a political lense. As mentioned above, we can then come up with a political score for the user after analyzing text such as their bios and timeline. Therefore, we can use this score to place a user along the political spectrum based off of their content. 

This gets particularly interesting when applying this method to journalist/influencer profiles. Because of how much bias exists on online media, it may be beneficial to keep in mind where certain accounts lie on the political spectrum. We could even perhaps average out all the account scores of the people you follow to see where your specific feed lies on the political spectrum. 


### Identification and Collection of Politically Salient Tweets for Further Research

With the world, and especially the United States, becoming increasingly politically divided, it becomes imperative that we keep up with the current state of political affairs. Since Twitter in particular has become a popular mode of communication amongst all platforms, it is also important to help others sift through relevant and non-relevant political information. Our political model will allow researchers to identify and select users and tweets in an efficient manner for a particular subsection of the political spectrum that they may be interested in.
