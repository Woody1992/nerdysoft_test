import json
import tkinter as tk


def get_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def add_word(word):
    word = word.lower()
    filename = 'words.json'
    data = get_data(filename)

    if any(x['name'] == word for x in data):
        entry_add_word.delete(0, 'end')
        label['text'] = f'Word {word} already in vocabulary'
        return None

    data.append({'name': word})
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

    entry_add_word.delete(0, 'end')
    label['text'] = f'Word {word} was added'



def search_words(search: str):
    search = search.lower()
    filename = 'words.json'
    data = get_data(filename)
    letter_dict = {}
    for letter in search:
        letter_dict[letter] = letter_dict[letter] + 1 if letter in letter_dict.keys() else 1
    result = []
    for word in data:
        if all(val <= word['name'].count(key) for key, val in letter_dict.items()):
            result.append(word['name'])
    if not search or search.isspace():
        result = []
    result.sort()
    label['text'] = f'Found {len(result)} words for "{search}":\n'
    label['text'] += '\n'.join(str(x) for x in result[:15]) if result else "No match found"


# Tkinter GUI
HEIGHT = 700
WIDTH = 1000

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_img = tk.PhotoImage(file='img.png', height=HEIGHT, width=WIDTH)
background_label = tk.Label(root, image=background_img)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_search = tk.Entry(frame, font="Helvetica 18 bold")
entry_search.place(rely=0.05, relx=0.02, relwidth=0.65, relheight=0.4)

entry_add_word = tk.Entry(frame, font="Helvetica 18 bold")
entry_add_word.place(rely=0.55, relx=0.02, relwidth=0.65, relheight=0.4)

btn_search = tk.Button(frame, text='Search', font="Helvetica 16 bold", command=lambda: search_words(entry_search.get()))
btn_search.place(rely=0.05, relx=0.7, relwidth=0.25, relheight=0.4)

btn_add_word = tk.Button(frame, text='Add word', font="Helvetica 16 bold", command=lambda: add_word(entry_add_word.get()))
btn_add_word.place(rely=0.55, relx=0.7, relwidth=0.25, relheight=0.4)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font="Helvetica 16 bold", anchor="nw", justify='left')
label.place(relwidth=1, relheight=1)

if __name__ == "__main__":
    root.mainloop()
