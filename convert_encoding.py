# convert_encoding.py
with open('mafony/views.py', 'r', encoding='cp1251') as f:
    content = f.read()

with open('mafony/views.py', 'w', encoding='utf-8') as f:
    f.write(content)
