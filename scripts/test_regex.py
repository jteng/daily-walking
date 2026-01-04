import re

text = '「起初」即在还未有时间以先，神已存在\n\n<p>换句话说，尚未有宇宙与世界以先，在任何被造物还未 出现之前，神已经存在。2.它否决了泛神论者之立场'

print("--- Original ---")
print(repr(text))

# Current Regex
split_text = re.sub(r'([。?？!！])\s*(\d+\.)', r'\1\n\2', text)
print("\n--- Split Result ---")
print(repr(split_text))

if '。\n2.' in split_text:
    print("\nSUCCESS: Split happened")
else:
    print("\nFAIL: Did not split")
