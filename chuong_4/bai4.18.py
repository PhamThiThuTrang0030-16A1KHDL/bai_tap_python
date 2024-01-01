import pandas as pd
emails = pd.Series(['mua sách tại amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}'
valid_emails = emails.str.extract(f'({pattern})')[0]
print(valid_emails.dropna())
