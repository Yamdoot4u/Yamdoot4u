import tkinter as tk

class ToDoApp:
    def __init__(self, master):
        self.tasks = []
        self.master = master
        self.task_entry = tk.Entry(self.master)
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.task_list = tk.Listbox(self.master)
        self.del_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)

        # Arrange Widgets
        self.task_entry.pack()
        self.add_button.pack()
        self.task_list.pack()
        self.del_button.pack()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.task_list.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_index)
        except IndexError:
            pass

def launch_app():
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("300x400")
    root.config(bg='#FFEFDB')
    ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    launch_app()
