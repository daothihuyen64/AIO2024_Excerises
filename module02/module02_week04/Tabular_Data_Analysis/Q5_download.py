import gdown

url = 'https://drive.google.com/uc?id=1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq'
output = 'Q5_advertising.csv'  # Đặt tên tệp tải về

gdown.download(url, output, quiet=False)
