from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Chatbot responses with multiple options
responses = {
    "hello": ["Hi there! Stay hydrated. 💧", "Hello! Need water advice?", "Hey! Ask me about hydration."],
    "how much water should i drink": [
        "You should drink at least 2-3 liters of water per day.",
        "A healthy adult should drink 8-10 glasses of water daily.",
        "It depends on your body weight, but generally, 2-4 liters is good."
    ],
    "benefits of drinking water": [
        "Water helps digestion, boosts energy, and improves skin health.",
        "Drinking enough water prevents dehydration and keeps your kidneys healthy.",
        "Water helps regulate body temperature and flush out toxins."
    ],
    "symptoms of dehydration": [
        "Dehydration can cause headaches, dry skin, dizziness, and fatigue.",
        "Feeling thirsty, dark urine, and dry mouth are signs of dehydration.",
        "Lack of water can lead to confusion, muscle cramps, and low energy."
    ],
    "best time to drink water": [
        "Drink a glass of water after waking up to start your day.",
        "It's best to drink water 30 minutes before meals for digestion.",
        "Stay hydrated throughout the day, especially after workouts."
    ],
    "remind me to drink water": [
        "Sure! Try setting a reminder every 2 hours.",
        "Drink a glass of water every morning and after every meal!",
        "Keep a water bottle near you and sip frequently."
    ],
    "can i drink too much water": [
        "Yes, drinking excessive water can lead to water intoxication (hyponatremia).",
        "Drinking too much water can dilute sodium levels in your body.",
        "Moderation is key! Aim for 2-4 liters per day based on your activity."
    ],
    "does coffee or tea count as water intake": [
        "Yes, but caffeinated drinks can cause mild dehydration.",
        "Tea and coffee contribute to water intake, but pure water is best.",
        "Herbal teas are a great alternative for hydration!"
    ],
    "what foods help with hydration": [
        "Fruits like watermelon, oranges, and cucumbers have high water content.",
        "Leafy greens and soups also help keep you hydrated!",
        "Coconut water is a great natural hydrator!"
    ],
    "bye": ["Goodbye! Stay hydrated! 💧", "Take care! Drink enough water.", "Bye! Remember to sip water regularly."],
}

# Keywords for matching similar questions
keywords_mapping = {
    "how much water": "how much water should i drink",
    "drink water": "remind me to drink water",
    "hydration": "benefits of drinking water",
    "dehydration symptoms": "symptoms of dehydration",
    "best time to drink": "best time to drink water",
    "overhydration": "can i drink too much water",
    "coffee count as water": "does coffee or tea count as water intake",
    "hydrating foods": "what foods help with hydration"
}

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chat/{query}")
def chat(query: str):
    query = query.lower()

    # Match similar phrases using keyword mapping
    for key, standard_query in keywords_mapping.items():
        if key in query:
            query = standard_query
            break

    if query in responses:
        return {"response": random.choice(responses[query])}
    
    return {"response": "I'm not sure, but remember to drink enough water! 💧"}
