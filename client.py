import tkinter as tk
from tkinter import ttk
from backend import connect_to_server, send_messages

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Sup de Vinci IRC Client")

        # Set the window size and center it
        self.master.geometry("800x600")
        self.center_window(800, 600)

        # Create the message log (Text widget)
        self.create_message_log()

        # Create the footer with the search bar and buttons
        self.create_footer()

        # Connect to the server
        self.sock = connect_to_server(update_chat_callback=self.display_message)

        # Show the main content
        self.pack()

    def center_window(self, width, height):
        """Put the window in the center of the user's screen"""
        # Get the screen dimensions
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate the position for the window to be centered
        pos_x = (screen_width // 2) - (width // 2)
        pos_y = (screen_height // 2) - (height // 2)

        # Position the window
        self.master.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

    def create_message_log(self):
        """frame for the message log"""
        # Create a Text widget for the message log
        self.message_log = tk.Text(self.master, height=20, state=tk.DISABLED, bg="white", fg="black")
        self.message_log.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10, expand=True)

    def create_footer(self):
        """Footer of the window"""
        # Create a footer frame and set its background color to gray
        footer = tk.Frame(self.master, bg="gray", height=50)
        footer.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        # Label for message entry
        label = tk.Label(footer, text="Enter your message:", bg="gray", fg="white")
        label.pack(side=tk.LEFT, padx=5)

        # Entry widget (search bar) for user to type their message
        self.message_entry = ttk.Entry(footer, width=60)
        self.message_entry.pack(side=tk.LEFT, padx=10)

        # Send button to capture the input and send the message
        send_button = ttk.Button(footer, text="Send", command=self.send_message)
        send_button.pack(side=tk.LEFT, padx=5)

        # Bind the Enter key to send_message
        self.message_entry.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        # Retrieve the message entered by the user
        message = self.message_entry.get()

        # Display the message in the log
        self.display_message(f"You: {message}")

        # (You would send the message to the server here, using sockets)
        if self.sock:
            send_messages(self.sock, message)
            self.message_entry.delete(0, tk.END)

        # Clear the message entry after sending
        self.message_entry.delete(0, tk.END)

    def display_message(self, message):
        # Enable the Text widget to append the message
        self.message_log.config(state=tk.NORMAL)
        self.message_log.insert(tk.END, message + "\n")  # Add the message followed by a new line
        self.message_log.config(state=tk.DISABLED)  # Disable editing again
        self.message_log.yview(tk.END)  # Auto-scroll to the bottom

    def update_chat(self, message):
        self.message_entry.insert(tk.END, message + "\n")

if  __name__ == "__main__":
    # Create and display the window
    root = tk.Tk()
    Client = App(master=root)
    Client.mainloop()

