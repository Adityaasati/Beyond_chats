import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
import json 

def func_citation(values):
    data_list = []
    for val in values:
        sources = val['source']
        for s in sources:
            ids = s['id']
            links = s['link']
            data_list.append({
                'Id': ids,
                'Link': links
            })
    return data_list

def fetch_data():
    api_url = api_entry.get()
    if not api_url:
        messagebox.showerror("Error", "Please enter a valid API URL.")
        return
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch data from the API: {e}")
        return


    result_text.delete(1.0, tk.END)


    page=1
    all_data = []
    while True:
        res = requests.get(f"{api_url}?page={page}")
        response = json.loads(res.text)
        page_no = response['data']['current_page']
        print("page_no",page_no)
        page+=1
        if response['data']['data']:
            citations_data = func_citation(response['data']['data'])
            all_data.extend(citations_data) 
        else:
            break

        for citation in all_data:
            result_text.insert(tk.END, f"{citation}\n")
        result_text.insert(tk.END, "\n")
        

root = tk.Tk()
root.title("API Data Fetcher")

# Create and place the widgets
tk.Label(root, text="API URL:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
api_entry = tk.Entry(root, width=50)
api_entry.grid(row=0, column=1, padx=10, pady=10)

fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.grid(row=0, column=2, padx=10, pady=10)

result_text = scrolledtext.ScrolledText(root, width=80, height=20)
result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)


root.mainloop()
