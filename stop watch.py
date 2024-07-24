import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.end_time  # Resume from paused time
            self.running = True
            print("Stopwatch started.")

    def stop(self):
        if self.running:
            self.end_time = time.time() - self.start_time  # Calculate elapsed time
            self.running = False
            print("Stopwatch stopped. Elapsed time:", self.get_elapsed_time())

    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.running = False
        print("Stopwatch reset.")

    def get_elapsed_time(self):
        if self.running:
            current_time = time.time() - self.start_time
        else:
            current_time = self.end_time
        return self.format_time(current_time)

    def format_time(self, elapsed):
        hours, rem = divmod(elapsed, 3600)
        minutes, seconds = divmod(rem, 60)
        return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)

# Example usage
stopwatch = Stopwatch()

while True:
    print("\n---- Stopwatch Menu ----")
    print("1. Start")
    print("2. Stop")
    print("3. Reset")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        stopwatch.start()
    elif choice == '2':
        stopwatch.stop()
    elif choice == '3':
        stopwatch.reset()
    elif choice == '4':
        print("Exiting stopwatch program...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

