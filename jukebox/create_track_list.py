import tkinter as tk
from tkinter import ttk, messagebox

# List to store track details (title and URL)
track_list = []

def add_to_list(title, url):
    if title and url:
        track_list.append((title, url))
        messagebox.showinfo("Success", "Track added to the list!")
    else:
        messagebox.showerror("Error", "Please enter both title and URL.")

def save_list():
    if track_list:
        with open('track_list.txt', 'w') as file:
            for title, url in track_list:
                file.write(f"{title} - {url}\n")
        messagebox.showinfo("Success", "Track list saved!")
    else:
        messagebox.showerror("Error", "No tracks to save.")

def show_list():
    if track_list:
        list_content = "\n".join([f"{i+1}. {title} - {url}" for i, (title, url) in enumerate(track_list)])
        messagebox.showinfo("Track List", list_content)
    else:
        messagebox.showinfo("Track List", "No tracks in the list.")

def main():
    root = tk.Tk()
    root.title("Create Track List")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="Track Title:").grid(row=0, column=0, sticky=tk.W)
    title_entry = ttk.Entry(frame)
    title_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Track URL:").grid(row=1, column=0, sticky=tk.W)
    url_entry = ttk.Entry(frame)
    url_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

    ttk.Button(frame, text="Add to List", command=lambda: add_to_list(title_entry.get(), url_entry.get())).grid(row=2, column=0, columnspan=2)
    ttk.Button(frame, text="Save List", command=save_list).grid(row=3, column=0, columnspan=2)
    ttk.Button(frame, text="Show List", command=show_list).grid(row=4, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
