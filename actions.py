from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import sqlite3 as lite
import pandas as pd
import time
from datetime import datetime
import random


class ActionRecommendTalk(Action):
    def name(self):
        return "action_recommend_session"
        
    def run(self, dispatcher, tracker, domain):
        conn = lite.connect('ConfDB.db')
        cur = conn.cursor()
        relevant_audience = tracker.get_slot('relevant_audience')
        cur.execute("SELECT * FROM agenda where relevant_audience like '%{}%'".format(relevant_audience))

        rows = cur.fetchall()
        ind = random.randint(0,len(rows))
        recommend_talk = list(rows[ind])
        title = recommend_talk[0]
        length = recommend_talk[8]
        speaker = recommend_talk[2]
        abstract = recommend_talk[4]
        
        dispatcher.utter_message("I would recommend you attend: {}".format(title))


        return [SlotSet("speaker", speaker), SlotSet("length",length), SlotSet("abstract", abstract)]