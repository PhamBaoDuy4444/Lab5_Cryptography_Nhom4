from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_rsa_keys():
    try:
        key = RSA.generate(2048)
        private_key = key.export_key().decode('utf-8')
        public_key = key.publickey().export_key().decode('utf-8')
        return {"pub_key": public_key, "priv_key": private_key}
    except Exception as e:
        return {"error": str(e)}

def handle_asymmetric(action, text, pub_key=None, priv_key=None):
    try:
        if action == 'encrypt':
            if not pub_key: return {"error": "Thiếu Public Key"}
            recipient_key = RSA.import_key(pub_key)
            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            enc_data = cipher_rsa.encrypt(text.encode('utf-8'))
            return {"result": base64.b64encode(enc_data).decode('utf-8')}
        else:
            if not priv_key: return {"error": "Thiếu Private Key"}
            private_key = RSA.import_key(priv_key)
            cipher_rsa = PKCS1_OAEP.new(private_key)
            dec_data = cipher_rsa.decrypt(base64.b64decode(text))
            return {"result": dec_data.decode('utf-8')}
    except Exception as e:
        return {"error": str(e)}
    