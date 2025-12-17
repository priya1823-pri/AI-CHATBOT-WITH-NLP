import nltk
from nltk.chat.util import Chat, reflections

pairs = [

    # GREETINGS
    [
        r"(hi|hello|hey|hlo|yo|sup)(.*)",
        ["Hello! How can I assist you today?",
         "Hi there! What can I do for you?",
         "Hey! How can I help?"]
    ],

    # ASK NAME
    [
        r"(what is your name|your name|who are you)(.*)",
        ["I am your smart NLP chatbot created using NLTK.",
         "People call me ChatBot-X. Here to assist you!"]
    ],

    # FEELINGS
    [
        r"(i am sad|i feel sad|feeling down|depressed|upset)",
        ["I'm sorry to hear that. Want to talk about it?",
         "I’m here for you. What happened?",
         "It's okay to feel that way. Tell me more."]
    ],
    [
        r"(i am happy|feeling great|very happy|excited)",
        ["That's awesome! What made you so happy?",
         "Great to hear that! Keep smiling :)"]
    ],

    # HELP WITH STUDIES
    [
        r"(explain|help|teach|what is|define)(.*)",
        ["Sure! Could you please specify the topic you want help with?",
         "I'm ready! Tell me what you want to learn.",
         "Give me a topic and I’ll explain it simply."]
    ],

    # JOKES
    [
        r"(tell me a joke|joke|make me laugh)",
        ["Why don’t programmers like nature? Too many bugs!",
         "I would tell you a UDP joke… but you might not get it.",
         "Why did the computer get cold? It forgot to close its Windows!"]
    ],

    # WEATHER (dummy)
    [
        r"(weather|temperature|is it hot|is it raining)(.*)",
        ["I can't check live weather, but you can ask me anything else!",
         "Wish I had weather sensors! But let's talk about something else."]
    ],

    # PERSONAL QUESTIONS
    [
        r"(do you love me|do you like me)",
        ["Of course I like you! You talk to me :)",
         "I love chatting with you. That counts, right?"]
    ],

    # THANK YOU
    [
        r"(thank you|thanks|thx)(.*)",
        ["You're welcome!",
         "Anytime!",
         "Happy to help :)"]
    ],

    # GOODBYE
    [
        r"(bye|goodbye|exit|quit)(.*)",
        ["Goodbye! Have a great day!",
         "See you later! Stay awesome.",
         "Bye! Come back soon :)"]
    ],

    # GENERAL SMART RESPONSES
    [
        r"(.*) your age(.*)",
        ["I'm as old as the code running me!",
         "I don't age—I'm digital >:)"]
    ],
    [
        r"(.*) created you(.*)",
        ["You did! You executed my Python script.",
         "I was created using Python and NLTK."]
    ],
    [
        r"(.*) (location|live)(.*)",
        ["I live inside your computer",
         "My home is wherever Python runs!"]
    ],

    # FALLBACK DEFAULT
    [
        r"(.*)",
        ["Interesting... Tell me more.",
         "Hmm... I'm not sure I understood. Could you rephrase?",
         "Let's talk more about that!",
         "Can you explain that in another way?"]
    ]
]

chatbot = Chat(pairs, reflections)

print("Chatbot: Hello! I am your smart NLTK chatbot. Type 'quit' to exit.")
chatbot.converse()