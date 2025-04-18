import random
from datetime import datetime

quotes = [
    "Success doesn't come to you, you go to it.",
    "Reading a book a day keeps ignorance away.",
    "Discipline is the bridge between goals and accomplishment.",
    "Small steps every day lead to big results.",
    "Invest in your mind. It's your greatest asset."
]

books = [
    "Atomic Habits by James Clear",
    "Deep Work by Cal Newport",
    "Think and Grow Rich by Napoleon Hill",
    "The 7 Habits of Highly Effective People by Stephen Covey"
]

def generate_daily_post():
    quote = random.choice(quotes)
    book = random.choice(books)
    date = datetime.now().strftime("%B %d, %Y")
    post = f"**{date} Motivation**\n\n{quote}\n\nToday’s Book: {book}\n\n#ShopBooksBot #Mindset #DailyInspo"
    return post
