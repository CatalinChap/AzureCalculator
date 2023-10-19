import tkinter as tk
 
# Function to calculate Azure storage cost
def calculate_cost():
    try:
        # Input from checkbuttons
        metadata_selected = metadata_var.get()
        blob_selected = blob_var.get()
 
        # Validate checkbuttons
        if not metadata_selected and not blob_selected:
            raise ValueError("Please select at least one option for changing tiers.")
 
        # Input from volume and storage model
        volume = float(volume_entry.get())
        storage_model = int(storage_model_var.get())
 
        # Validate volume (numbers only)
        if not volume_entry.get().replace(".", "", 1).isdigit():
            raise ValueError("Volume must be a number.")
 
        # Cost calculation based on selected options
        cost_per_unit = 0.13  # $0.13 per 10,000 units
 
        if metadata_selected and blob_selected:
            if storage_model == 1:
                cost = (volume * 2) / 10000 * cost_per_unit
            elif storage_model == 3:
                cost = (volume * 7) / 10000 * cost_per_unit
        elif blob_selected:
            if storage_model == 1:
                cost = (volume / 10000) * cost_per_unit
            else:
                cost = 0
        else:
            cost = 0
 
        result_label.config(text=f"Estimated cost for changing tier to cool: ${cost:.2f}")
    except ValueError as e:
        result_label.config(text=str(e))
 
# Create the main window
root = tk.Tk()
root.title("Azure Storage Cost Calculator")
 
# Checkboxes for changing tiers
metadata_var = tk.BooleanVar()
blob_var = tk.BooleanVar()
 
metadata_checkbox = tk.Checkbutton(root, text="Change tiers for Metadata", variable=metadata_var)
metadata_checkbox.pack()
 
blob_checkbox = tk.Checkbutton(root, text="Change tiers for Blobs", variable=blob_var)
blob_checkbox.pack()
 
# Volume Input
volume_label = tk.Label(root, text="No. of files:")
volume_label.pack()
volume_entry = tk.Entry(root)
volume_entry.pack()
 
# Storage Model Selection
storage_model_label = tk.Label(root, text="Select storage model:")
storage_model_label.pack()
storage_model_var = tk.IntVar()
storage_model_options = [("1", 1), ("3", 3)]
 
for option, value in storage_model_options:
    storage_model_radio = tk.Radiobutton(root, text=option, variable=storage_model_var, value=value)
    storage_model_radio.pack()
 
# Calculate Button
calculate_button = tk.Button(root, text="Calculate cost for changing tier", command=calculate_cost)
calculate_button.pack()
 
# Result Display
result_label = tk.Label(root, text="")
result_label.pack()
 
# Start the application
root.mainloop()