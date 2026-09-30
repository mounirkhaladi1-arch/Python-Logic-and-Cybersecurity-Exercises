#!usr/bin/env python3

# XOR encryption function

"""test_string='b'
print(ord(test_string))
print(bin(ord(test_string)))

def xor_encryption(word:str):
    key="I LA"
    key=''.join(format(ord(char), '08b') for char in key)
    key=int(key,2)
    word=''.join(format(ord(char), '08b') for char in word)
    word=int(word,2)
    encrypted_string=ord(key^word)

    return encrypted_string

x=xor_encryption(test_string)

print(x)
"""

# 📋 المصفوفة الكاملة والمصححة من واقع لقطة شاشتك
ll = [51, 54, 48, 51, 61, 57, 50, 54, 48, 52, 55, 50, 50, 57, 47, 52, 57, 47, 54, 24, 57, 58, 62]
TARGET_SUM = 2406

# قائمة الحروف المقبولة والمسموح بها داخل القوسين حسب وصف التحدي
ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyz0123456789_")

valid_flags = []


# 📋 الأرقام السرية المستخرجة من واقع لقطة شاشتك
secret_numbers = [
    92, 98, 87, 93, 113, 95, 105, 85, 106, 94, 95, 105, 85, 89, 87, 91, 105, 87, 104,
    85, 89, 95, 102, 94, 91, 104, 53, 115
]

flag = ""

# 🚀 تطبيق الهندسة العكسية: إضافة 10 وتحويل القيمة الحية إلى أحرف ASCII
for num in secret_numbers:
    original_ascii = num + 10
    flag += chr(original_ascii)

print("\n" + "="*50)
print(f"[+] SUCCESS! Your True Flag is:\n{flag}")
print("="*50 + "\n")
