# Code AES/DES/3DES
from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad
import base64

def handle_symmetric(algo, action, text, key):
    try:
        key_bytes = key.encode('utf-8')
        algo = algo.upper()

        if algo == 'AES':
            key_bytes = key_bytes.ljust(16)[:16]
            cipher = AES.new(key_bytes, AES.MODE_ECB)
        elif algo == 'DES':
            key_bytes = key_bytes.ljust(8)[:8]
            cipher = DES.new(key_bytes, DES.MODE_ECB)
        elif algo in ['3DES', 'TRIPLEDES']:
            # 3DES cần key 16 hoặc 24 bytes
            key_bytes = key_bytes.ljust(16)[:16]
            cipher = DES3.new(key_bytes, DES3.MODE_ECB)
        else:
            return {"error": "Thuật toán đối xứng không hỗ trợ"}

        if action == 'encrypt':
            data_bytes = text.encode('utf-8')
            ct_bytes = cipher.encrypt(pad(data_bytes, cipher.block_size))
            return {"result": base64.b64encode(ct_bytes).decode('utf-8')}
        else:
            ct_bytes = base64.b64decode(text)
            pt = unpad(cipher.decrypt(ct_bytes), cipher.block_size)
            return {"result": pt.decode('utf-8')}
    except Exception as e:
        return {"error": str(e)}