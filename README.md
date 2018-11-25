# CareBot
A Care Bot That Loves All

## Inspiration
**Enhancing students well-being and academic performance is a major concern for societies.**

**We help tackling this challenge using Chatbots and AI for university students!**

Research shows (Kosidou et al., 2014) that students at risk for school failure have increased rates of suicide. So it is important to have a easy to use interface in which students get immediate help. Additionally, sometimes, even when we are doing well in life, we just need to talk, however it's not so easy to openly seek help.This can be due to outside pressures, stereotypes, or cultural-based stigmas. Something sensitive such as suicidal thoughts might be too hard to speak freely about. Introducing CareBot, the non-judgemental AI concierge chatbot for students in crisis!

## What it does
-Uses a ML model to predict grades of students based on several multi-dimensional outcomes such as educational, social, and socioeconomics. 

-Detects suicide predictors from grades and offers support. Additionally, the bot can offer suicide intervention to people that aren't suffering from low grades.

## How we built it
AWS Lex was the basis for the chatbot, Azure Face & Emotion API was used in combination with peer-reviewed psychological scales to detect current mental state, and we implemented the python scripts using AWS Lambda. Finally, we deployed the app on the Facebook Messenger platform for simplicity and ease of use.

## Challenges we ran into
-Integration of Azure and AWS.

-Getting Zucced by Mark Zuckerberg's spam algorithm while sharing API keys and links with teammates, which broke my API. 

## Accomplishments that we're proud of
-Getting it to finally run on the Messenger platform.

-Running the machine learning model and having the chatbot tell me that I will "definitely fail" based on my grades.

## What we learned
-How to use AWS

-Building AI chatbots

## What's next for CareBot

-Expand Carebot to deal with more mental health issues than just suicide (ex. Depression, Anxiety, & Stress).

-Have a more meaningful conversation by creating more intents and slots. 

-Returning meaningful advice based on actual peer-reviewed psychological evidence

-Expand to Whatsapp (via Twilio)

-Make use of AWS Cognito services 
