# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
# import torch
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
# model_name = "HuggingFaceH4/zephyr-7b-alpha"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")
#
#
# class ActionCareerCounsellor(Action):
#     def name(self) -> Text:
#         return "action_career_counsellor"
# 
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_query = tracker.latest_message.get('text')
#         prompt = f"""You are an AI career counsellor. Answer this clearly and helpfully:\n\n{user_query}\n"""
# 
#         try:
#             input_ids = tokenizer.encode(prompt, return_tensors="pt").to(model.device)
#             outputs = model.generate(input_ids, max_new_tokens=300, do_sample=True, temperature=0.7)
#             answer = tokenizer.decode(outputs[0], skip_special_tokens=True).replace(prompt, "").strip()
#         except Exception as e:
#             answer = f"Sorry, I encountered an error. ({e})"
# 
#         dispatcher.utter_message(text=answer)
#        return []




