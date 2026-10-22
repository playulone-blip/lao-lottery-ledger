from datetime import datetime
import json
import os
import requests
from bs4 import BeautifulSoup


def fetch_latest_lottery():
  # จุดสำหรับเชื่อมต่อดึงข้อมูลจากเว็บไซต์ผลหวยจริง
  url = 'https://lotto.thaiorc.com/lao/stats/lottery-years10.php'
  headers = {'User-Agent': 'Mozilla/5.0'}

  try:
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
      soup = BeautifulSoup(response.content, 'html.parser')
      # TODO: เขียนโค้ดแกะตารางดึงวันที่และเลขล่าสุดจากเว็บไซต์ตรงนี้
      # ตัวอย่างจำลองการดึงค่าล่าสุดมาอัปเดต
      return None, None
  except Exception as e:
    print(f'Error fetching data: {e}')
  return None, None


def update_json_file():
  file_path = 'data.json'

  if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
      data = json.load(f)
  else:
    data = {}

  # ดึงข้อมูลจากเว็บจริงมาอัปเดตลง dictionary
  date_str, number = fetch_latest_lottery()
  if date_str and number:
    data[date_str] = number

  with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
  print('Data.json update process completed.')


if __name__ == '__main__':
  update_json_file()
