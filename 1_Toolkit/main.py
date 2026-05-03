from flask import Flask, render_template, request, jsonify
# Import logic từ thư mục utils
from utils.symmetric import handle_symmetric
from utils.asymmetric import handle_asymmetric, generate_rsa_keys
from utils.hashing import handle_hashing

app = Flask(__name__)

# Route chính để hiển thị giao diện từ templates/index.html
@app.route('/')
def index():
    return render_template('index.html')

# API xử lý mã hóa đối xứng (AES, DES, 3DES)
@app.route('/api/symmetric', methods=['POST'])
def sym_api():
    data = request.json
    # Gọi hàm xử lý từ utils/symmetric.py
    result = handle_symmetric(data['algo'], data['action'], data['input'], data['key'])
    return jsonify(result)

# API tạo cặp khóa RSA
@app.route('/api/asymmetric/genkeys', methods=['POST'])
def gen_keys_api():
    return jsonify(generate_rsa_keys())

# API xử lý RSA (Mã hóa/Giải mã)
@app.route('/api/asymmetric/process', methods=['POST'])
def asym_api():
    data = request.json
    result = handle_asymmetric(data['action'], data['input'], data.get('pub_key'), data.get('priv_key'))
    return jsonify(result)

# API xử lý hàm băm (MD5, SHA256)
@app.route('/api/hash', methods=['POST'])
def hash_api():
    data = request.json
    result = handle_hashing(data['algo'], data['input'])
    return jsonify(result)

if __name__ == '__main__':
    print("Server đang chạy tại http://127.0.0.1:5000")
    app.run(port=5000, debug=True)
    