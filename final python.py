import time

def typing_speed_test():
    print("Welcome to the typing speed test!")
    time.sleep(1)
    print("Type the following sentence as quickly and accurately as possible:")
    time.sleep(1)
    sentence = "The quick brown fox jumps over the lazy dog.She folded the paper asd asd asdd asd sad dasd dasdx asd."
    print(sentence)
    time.sleep(1)
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    time_elapsed = end_time - start_time
    words_typed = len(user_input.split())
    accuracy = sum([1 for i in range(len(user_input)) if user_input[i] == sentence[i]]) / len(sentence)
    typing_speed = words_typed / time_elapsed * 60
    print(f"Time elapsed: {time_elapsed:.2f} seconds")
    print(f"Words typed: {words_typed}")
    print(f"Accuracy: {accuracy*100:.2f}%")
    print(f"Typing speed: {typing_speed:.2f} words per minute")

typing_speed_test()
