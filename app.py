from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')#首頁
def form():
    return render_template('input_data.html')

@app.route('/submit_form', methods=['POST'])
def handle_form():
    id_number = request.form.get('id')
    name = request.form.get('name')
    gender = request.form.get('gender')
    email = request.form.get('email')

    # Validate ID number (assuming 台灣ID)
    if len(id_number)!=10:                        #1. 確認身份證號碼長度是否為10。
        return "身分證號碼應該為10碼", 400
    if not id_number[0].isalpha():                #2. 確認第一個字元是否為英文字母
        return "第一個字元應該為英文字母碼", 400
        
    if not id_number[1:].isdigit():               #3. 確認後九個字元是否為數字
        return "身分證號碼後九碼應為數字", 400

    #4. 將第一個英文字母轉換為對應的數字（A為10，B為11，C為12，...，Z為33）
    letter_to_number = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
        'F': 15, 'G': 16, 'H': 17, 'J': 18, 'K': 19,
        'L': 20, 'M': 21, 'N': 22, 'P': 23, 'Q': 24,
        'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29,
        'X': 30, 'Y': 31, 'W': 32, 'Z': 33, 'I': 34,
        'O': 35        }
    number = letter_to_number.get(id_number[0])

    




    
    # Validate name (assuming it's alphabetic)
    if not re.match(r'^[A-Za-z\s]+$', name):
        return "Invalid name", 400

    # Validate gender
    if gender not in ['Male', 'Female']:
        return "Invalid gender", 400

    # Validate email
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return "Invalid email", 400

    return "All entries are valid", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Listen on all available network interfaces and port 80

