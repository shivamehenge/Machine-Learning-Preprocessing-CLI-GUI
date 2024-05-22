import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from data_description import DataDescription
from imputation import Imputation
from categorical import Categorical
from download import Download
from feature_scaling import FeatureScaling


class PreprocessorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Machine Learning Preprocessor")

        self.data = None

        # Custom colors
        self.button_color = "#ed1e5f"
        self.label_color = "#db2188"
        self.frame_color = "#e3ceda"
        self.font_style = ("Helvetica", 18, "bold")


        # Load Dataset button
        self.load_button = tk.Button(root, text="Import The Dataset", bg=self.button_color, fg="white", command=self.load_dataset)
        self.load_button.pack(pady=20)

        # Image
        #self.logo_image = Image.open("Shantanu123.jpg")  # Replace "logo.png" with your image file
        #self.logo_image = self.logo_image.resize((200, 200)) 
        #self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        #self.logo_label = tk.Label(root, image=self.logo_photo)
        #self.logo_label.pack()


        # Tasks frame
        self.tasks_frame = tk.Frame(root, bg=self.frame_color)
        self.tasks_frame.pack()

        
        

        # Tasks
        self.tasks = [
            ('Data Description', DataDescription , "Here we can access the specific column Information.."),
            ('Handling NULL Values', Imputation , "Here we can Handle the null values.."),
            ('Encoding Categorical Data', Categorical, "Here We can Encode the categorical data.. "),
            ('Feature Scaling of the Dataset', FeatureScaling, "Here we can perform the Normalization and Standardisation on the specific columns.. "),
            ('Download the modified dataset', Download , "From here we can download the preprocessed data set..")
        ]

        for idx, (task_name, task_class, task_description) in enumerate(self.tasks, start=1):
            # Task button
            task_button = tk.Button(self.tasks_frame, text=task_name, bg=self.button_color, fg="white", command=lambda task=task_class: self.execute_task(task))
            task_button.grid(row=idx, column=0, padx=50, pady=35, sticky="ew")

            # Task description
            description_label = tk.Label(self.tasks_frame, text=task_description, bg=self.label_color, fg="white", padx=10, pady=10, wraplength=500)
            description_label.grid(row=idx, column=1, padx=50, pady=35, sticky="w")
        

    

    def load_dataset(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)  # You can use read_excel() for Excel files
                messagebox.showinfo("Success", "Dataset loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load dataset: {str(e)}")

    def execute_task(self, task_class):
        if self.data is None:
            messagebox.showerror("Error", "Please load a dataset first!")
            return

        task_instance = task_class(self.data)
        self.data = task_instance.execute()
        messagebox.showinfo("Success", "Task completed successfully!")


def main():
    root = tk.Tk()
    app = PreprocessorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
