from datetime import datetime
import json
import os
import requests
from bs4 import BeautifulSoup


def fetch_latest_lottery():
  # ตัวอย่างเว็บไซต์แหล่งข้อมูลผลหวยลาว
  url = 'https://lotto.thaiorc.com/lao/stats/lottery-years10.php'
  headers = {
      'User-Agent': (
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
          ' like Gecko) Chrome/120.0.0.0 Safari/537.36'
      )
  }

  try:
    response = requests.get(url, headers=headers, timeout=15)
    if response.status_code == 200:
      soup = BeautifulSoup(response.content, 'html.parser')

      # ค้นหาตารางหรือข้อมูลผลรางวัลจากหน้าเว็บ
      # (ส่วนนี้สามารถปรับแต่ง Selector ให้ตรงกับโครงสร้าง HTML ของเว็บเป้าหมายได้)
      table = soup.find('table')
      if table:
        rows = table.find_all('tr')
        fetched_data = {}

        for row in rows:
          cols = row.find_all(['td', 'th'])
          if len(cols) >= 2:
            # ดึงข้อความวันที่และผลรางวัลจากตาราง (ต้องปรับตำแหน่ง index ตามโครงสร้างจริงของเว็บ)
            # ตัวอย่างโครงสร้างสมมติ: date_text = cols[0].text.strip(), num_text = cols[1].text.strip()
            pass

        return fetched_data
  except Exception as e:
    print(f'Error fetching data: {e}')

  return {}


def update_json_file():
  file_path = 'data.json'

  # โหลดข้อมูลเดิมที่มีอยู่
  if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
      data = json.load(f)
  else:
    data = {}

  # ดึงข้อมูลใหม่จากเว็บ
  new_data = fetch_latest_lottery()
  if new_data:
    # อัปเดตข้อมูลใหม่รวมกับข้อมูลเดิม
    data.update(new_data)

  # บันทึกกลับลงไฟล์ data.json
  with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
  print('Data.json update process completed.')


if __name__ == '__main__':
  update_json_file()
