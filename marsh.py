import marshal

# خواندن داده های مارشال شده از فایل
with open('bot.py', 'rb') as file:
    marshalled_data = file.read()

# دیکد کردن داده های مارشال شده
decoded_data = marshal.loads(marshalled_data)

print(decoded_data)

