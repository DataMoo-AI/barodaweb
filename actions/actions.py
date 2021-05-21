# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted, AllSlotsReset, Restarted
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class DetailsForm(Action):

    def name(self) -> Text:
        return "intern_details_form"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        required_slots = ["name", "email", "mobile","colname"]
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot", slot_name)]
        return [SlotSet("requested_slot", None)]

class ActionEnquiryForm(Action):

     def name(self) -> Text:
         return "action_intern_create_form"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         print(f"user_id:{tracker.sender_id}")


         name = tracker.get_slot("name")
         email = tracker.get_slot("email")
         mobile = tracker.get_slot("mobile")
         colname= tracker.get_slot("colname")

         message = (f"Thanks for the details,"
                    f" provided name as {name}"
                    f" provided email as {email}"
                    f" provided mobile as {mobile}"
                    f" provided college name as {colname}"
                    f" we will reach out to you soon. Thank you")

         dispatcher.utter_message(message)

         return []
