# SentiMeter - Aspect Based Sentiment Analyzer based on MicroServices
## BUSINESS NEED/OPPORTUNITY  

Businesses need to understand their customers better, so they can carry out better social media monitoring, enhanced market research, help customer feedback analysis, improved decision-making and hence can deliver improved customer satisfaction. These factors can help businesses in better focused campaigns to customers and cross-sell other products.

Businesses find difficulty to monitor the brand and product sentiment in customer feedback. Businesses fail to understand how customers feel about a certain product and steps needed to improve CX. Sentiment analysis is a powerful tool that helps businesses to understand and respond to the needs and preferences of their customers. 

Traditional monolithic software architectures include difficulty in deployment and scaling, inflexibility in technology choices, and reduced fault isolation. Microservices solves the challenges of monolithic systems by being as modular as possible. They help build an application organized around small, independent services that are independently deployable.
 
By implementing sentiment analysis using microservices, the businesses can have a go to solution application which is powerful as well as modular and compact in nature at the same time.

A solution like this can help the businesses alter their strategies and increase profits as the customer feedback is considered and with this the product can further be improved with the help of this feedback.

## TARGET SEGMENT/MARKET SIZE  

A target segment for sentiment analysis using microservices are a group of customers or users that the businesses or organizations are trying to reach with its sentiment analysis services. The intended customers for sentiment analysis using microservices can be any business or organization that needs to understand and respond to the sentiment of their customers, users, or the general public. Examples include social media platforms, e-commerce companies, marketing and market research firms, news organizations etc.

Sentiment analysis is one aspect of the broader market for data analytics and artificial intelligence services. This market is expected to grow significantly in the coming years. According to a report from MarketsandMarkets, the global data analytics market is expected to grow from $138.9 billion in 2018 to $229.4 billion by 2023, at a CAGR of 10.2% during the forecast period.

Microservices are just one aspect of the broader market for cloud computing and software as a service (SaaS). This market looks promising as many businesses are shifting to cloud infrastructure for a number of reasons. The global cloud computing market is expected to grow from $371.4 billion in 2020 to $832.1 billion by 2025, at a CAGR of 18.3% during the forecast period according to a report from MarketsandMarkets.

The above information can clearly conclude that there is growth for both microservices and sentiment analysis and such a product will add value for the growth of business and organizations.

## SOLUTION DETAILS  

The text or any written feedback from the customers are extracted with the help of Web-scrapping, APIs(from social media platforms, and online review systems).

The  preprocessed data is then passed onto another microservice which contains the aspect based sentiment analysis model which is a similar model compared to classical sentiment analysis one but has the ability to show sentiment for particular subject rather than for whole sentence which can be customized for identifying the emotion of the customer.

The USP of the solution includes the ability of the model to identify the aspect and the sentiment for the aspect automatically, availability of customized data organization for various businesses as the subjects can be changed and   it's a fully automated end-to-end system, which is accomplished by building a CI/CD pipeline. Coming to the scalability aspect, the microservices are specially known for modularity and portability.

The main feature includes its Dynamic Re-training ability which helps to increase it's accuracy and stability by identifying various new patterns  with time. 

There are many unique benefits that can be achieved with the solution which mainly include
Client relationship which is a main criteria for success of any Business and it can be improved through the solution as it provides the comfort to understand the need of customers and the review of any company’s services.

![image](https://github.com/user-attachments/assets/6e5706f1-685f-431a-b78b-e1c93f796132)

Flowchart Video: https://www.youtube.com/watch?v=fsw7CoHpKsk  
System Prototype: https://www.youtube.com/watch?v=wEzMGWOAJbQ

## FUTURE READINESS
Yes, this architecture can be replaced with a similar customer. In this case, we are training the model with public and community shared datasets which includes up to 21 ABSA(Aspect Based Sentiment Analysis) datasets in 8 languages that cover several domains. To implement the model for a specific industry, an industry-specific dataset can be used to re-train the model.

![image](https://github.com/user-attachments/assets/31c33cd2-8372-4983-afd2-22013954a61e)


![image](https://github.com/user-attachments/assets/11338093-8292-424d-97b5-09b14ba5eaf2)






