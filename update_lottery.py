from datetime import datetime
import json
import os
import requests
from bs4 import BeautifulSoup


def fetch_latest_lottery():
  # ตัวอย่าง URL แหล่งข้อมูลสถิติหรือประกาศผล
  url = 'https://lotto.thaiorc.com/lao/stats/lottery-years10.php'
  headers = {'User-Agent': 'Mozilla/5.0'}

  try:
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
      soup = BeautifulSoup(response.content, 'html.parser')
      # เขียน Logic แกะตารางดึงผลหวยล่าสุดตรงนี้
      # สมมติว่าดึงวันที่และเลขล่าสุดมาได้ เช่น:
      # latest_date = "2026-10-22"
      # latest_number = "123456"
      return None, None
  except Exception as e:
    print(f'Error fetching data: {e}')
  return None, None


def update_json_file():
  file_path = 'data.json'

  # โหลดข้อมูลเดิมที่มีอยู่
  if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
      data = json.load(f)
  else:
    data = {}

  # ดึงข้อมูลล่าสุด (ตัวอย่างจำลองการอัปเดต)
  # date_str, number = fetch_latest_lottery()
  # ถ้าระบบดึงข้อมูลได้จริง นำมาใส่เงื่อนไขบันทึก:
  # if date_str and number:
  #     data[date_str] = number

  # บันทึกกลับลงไฟล์ JSON
  with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
  print('Data.json updated successfully.')


if __name__ == '__main__':
  update_json_file()