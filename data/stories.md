## happy path all info 1               
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* length
  - utter_length
* thanks
  - utter_thanks
  
  
## happy path all info 2               
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* length
  - utter_length
* speaker
  - utter_speaker
* thanks
  - utter_thanks    
  

## happy path all info 3               
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* speaker
  - utter_speaker
* length
  - utter_length
* thanks
  - utter_thanks  


## happy path no relevant audience            
* greet              
  - utter_greet
* recommend_session
  - utter_ask_relevant_audience
* inform{"relevant_audience":"Data Scientists"}
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* length
  - utter_length
* speaker
  - utter_speaker
* thanks
  - utter_thanks 

  
## multi-intents story1              
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* speaker+length
  - utter_length
  - utter_speaker
* thanks
  - utter_thanks
  
## multi-intents story2              
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* speaker+length
  - utter_length
  - utter_speaker
* abstract
  - utter_abstract
* thanks
  - utter_thanks
  
## multi-intents story2              
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* speaker+length
  - utter_length
  - utter_speaker
* abstract
  - utter_abstract
* thanks
  - utter_thanks
  
  
## multi-intents story2              
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* speaker+length
  - utter_length
  - utter_speaker
* abstract
  - utter_abstract
* thanks
  - utter_thanks
  
  
  
## out-of-scope input story 1            
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* out-of-scope
  - utter_out_of_scope
  - utter_ask_other_questions
* abstract
  - utter_abstract
* thanks
  - utter_thanks
  
## out-of-scope input story 2            
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* out-of-scope
  - utter_out_of_scope
  - utter_ask_other_questions
* thanks
  - utter_thanks 
  
## out-of-scope input story              
* greet              
  - utter_greet
* recommend_session{"relevant_audience":"Data Scientists"}               
  - action_recommend_session
  - slot{"speaker":"Justina"}
  - slot{"length":"5 min"}
  - slot{"abstract":"Workshop on chatbots"}
* out-of-scope
  - utter_out_of_scope
  - utter_ask_other_questions
* greet
    - utter_greet
* recommend_session{"relevant_audience": "ML"}
    - slot{"relevant_audience": "ML"}
    - action_recommend_session
    - slot{"speaker": "Till Bergmann and Leah McGuire"}
    - slot{"length": ""}
    - slot{"abstract": "A problem in predictive modeling data is label leakage. At Enterprise companies such as Salesforce, this problem takes on monstrous proportions as the data is populated by diverse business processes, making it hard to distinguish cause from effect. We will describe how we tackled this problem at Salesforce, where we need to churn out thousands of customer-specific models for any given use case."}
* thanks
    - utter_goodbye
* goodbye
    - utter_thanks

