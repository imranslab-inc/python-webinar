import os

# List of folder names to create
folder_names = [
    "module4.1-java-thread-and-runnable",
    "module4.2-java-thread-sleep",
    "module4.3-java-thread-join",
    "module4.4-java-thread-states",
    "module4.5-java-thread-wait-notify-and-notifyall",
    "module4.6-thread-safety-and-synchronization",
    "module4.7-java-exception-in-thread-main",
    "module4.8-thread-safety-in-singleton-class",
    "module4.9-daemon-thread-in-java",
    "module4.10-java-thread-local",
    "module4.11-java-thread-dump",
    "module4.12-how-to-analyze-deadlock-in-java",
    "module4.13-java-timer-thread",
    "module4.14-java-producer-consumer-problem",
    "module4.15-java-thread-pool",
    "module4.16-java-callable-future",
    "module4.17-java-futuretask-example"
]

for folder_name in folder_names:
    # Check if the folder already exists
    if not os.path.exists(folder_name):
        # Create the folder
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")
