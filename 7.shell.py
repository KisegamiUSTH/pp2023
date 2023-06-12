import subprocess

while True:
    command = input("Shell $ ")

    if command == "exit":
        break

    parts = command.split(" ")

    if ">" in parts:
        # Output redirection to file
        index = parts.index(">")
        output_file = parts[index + 1]
        command = parts[:index]

        with open(output_file, "w") as file:
            subprocess.run(command, stdout=file)

    elif "<" in parts:
        # Input redirection from file
        index = parts.index("<")
        input_file = parts[index + 1]
        command = parts[:index]

        with open(input_file, "r") as file:
            subprocess.run(command, stdin=file)

    elif "|" in parts:
        # Command chaining using pipes
        index = parts.index("|")
        command1 = parts[:index]
        command2 = parts[index + 1:]

        process1 = subprocess.Popen(command1, stdout=subprocess.PIPE)
        process2 = subprocess.Popen(command2, stdin=process1.stdout)

        process1.stdout.close()
        process2.wait()

    else:
        # Simple command execution
        subprocess.run(parts)

# Well at least it should work with linux