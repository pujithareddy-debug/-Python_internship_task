text = "pujitha"
reverse_slice = text[::-1]
reverse_index = ""
for i in range(len(text)-1,-1,-1):
    reverse_index = reverse_index + text[i]
print("string:",text)
print("reversed using slicing:",reverse_slice)
print("reversed using indexing:",reverse_index)