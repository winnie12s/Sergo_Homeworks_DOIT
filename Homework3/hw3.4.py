stop_phrase = "quit"

while True:
    phrase_to_repeat = input("Give me a phrase to repeat:")
    if phrase_to_repeat != stop_phrase:
        print("User said Whaaaat?")
        print(f"User said {phrase_to_repeat}")
    else:
        break