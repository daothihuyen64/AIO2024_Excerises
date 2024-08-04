import gdown

url = 'https://drive.google.com/uc?id=1jh2p2DlaWsDo_vEWIcTrNh3mUuXd-cw6'
output = 'Q10_advertising.csv'  # Đặt tên tệp tải về

gdown.download(url, output, quiet=False)
