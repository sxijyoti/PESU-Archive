from napkin import request, response

response.status_code = 200

# Predefined list of jokes
jokes = [
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What did the ocean say to the shore? Nothing, it just waved.",
    "Why don’t eggs tell jokes? They’d crack each other up!"
]

# Helper function to get a random joke
def get_random_joke():
    import random
    return random.choice(jokes)

if request.method == 'GET':
    # Respond with a random joke
    response.body = {
        "joke": get_random_joke()
    }

else:
    # Handle unsupported HTTP methods
    response.status_code = 405
    response.body = {
        "error": "HTTP METHOD NOT ALLOWED",
        "allowed-methods": ["GET"]
    }