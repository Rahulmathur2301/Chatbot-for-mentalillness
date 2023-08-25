import random

class MentalHealthChatbot:
    def __init__(self):
        self.greetings = ["hello", "hi", "hey", "hi there"]
        self.goodbyes = ["bye", "goodbye", "take care", "see you"]
        self.therepy = ["therepy","exercises","what should I do","therepies"]
        self.helpline=["helpline number","contact","emergency"]
        self.boost=["mind fresh","mood booster","jokes","funny","joke"]
        self.mentalillness=["Types of mental illness","types?"]
        self.anxiety=["What is anxiety?","Anxiety?"]
        self.depression=["What is depression?","Depression?"]
        self.advice = [
            "Remember to practice deep breathing when you're feeling anxious.",
            "Engaging in regular physical activity can have a positive impact on your mental well-being.",
            "Reach out to a friend or family member to talk about your feelings.",
            "Consider journaling your thoughts as a way to process your emotions.",
            "If you're struggling, don't hesitate to seek help from a mental health professional.",
            "Consult a counsellor for help",
        ]

    def get_response(self, user_input):
        if any(greeting in user_input.lower() for greeting in self.greetings):
            return "Hello! Am Freeboo, How can I help you today?"
        elif any(goodbye in user_input.lower() for goodbye in self.goodbyes):
            return "Take care and remember that I'm here if you need support.If you need more help contact 800-950-6264."
        elif any(helpline in user_input.lower() for helpline in self.helpline):
            return"Kindly contact 800-950-6264 for further support."
        elif any(mentalillness in user_input.lower() for mentalillness in self.mentalillness):
            return"Types of mental illness are anxiety,depression etc."
        elif any(anxiety in user_input.lower() for anxiety in self.anxiety):
            return"At the higest level, anxiety is your body's natural response to stress. It's a feeling of fear or apprehension about what's to come."
        elif any(depression in user_input.lower() for depression in self.depression):
            return"Depression is a mood disorder that causes a persistent feeling of sadness and loss of interest. Also called major depressive"
        elif any(boost in user_input.lower() for boost in self.boost):
            return"There are a few jokes that i like very much:\n What’s the best thing about Switzerland?\nI don’t know, but the flag is a big plus.\n I invented a new word!\n Plagiarism!\n Once, my father came home and found me in front of a roaring fire. That made my father very mad, as we didn’t have a fireplace.\n Listen up!You can’t believe everything you hear—but you can repeat it."
        elif any(therepy in user_input.lower() for therepy in self.therepy):
            return "There are different types of therepies which you can practice such as:\n Individual: This therapy involves only the patient and the therapist.\n Group: Two or more patients may participate in therapy at the same time. Patients are able to share experiences and learn that others feel the same way and have had the same experiences.\n Marital couples: This type of therapy helps spouses and partners understand why their loved one has a mental disorder, what changes in communication and behaviors can help, and what they can do to cope. This type of therapy can also be used to help a couple that is struggling with aspects of their relationship.\n Family: Because family is a key part of the team that helps people with mental illness get better, it is sometimes helpful for family members to understand what their loved one is going through, how they themselves can cope, and what they can do to help."
                    
        
        else:
            return random.choice(self.advice)

def main():
    chatbot = MentalHealthChatbot()
    print("Chatbot: Hello! I'm Freebo and I am here to provide advice for mental health. How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")
        
        if any(goodbye in user_input.lower() for goodbye in chatbot.goodbyes):
            print("Chatbot: Take care and have a healthy day!")
            break

if __name__ == "__main__":
    main()
