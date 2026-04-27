# Code tự xây dựng thuật toán RSA (Sinh khóa, Encrypt, Decrypt)
import os
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

# --- 1. CÁC HÀM TOÁN HỌC CƠ BẢN ---
def extended_gcd(a, b):
    if a == 0: return b, 0, 1
    g, y, x = extended_gcd(b % a, a)
    return g, x - (b // a) * y, y

def mod_inverse(e, phi):
    g, x, y = extended_gcd(e, phi)
    if g != 1: return None
    return x % phi

# --- 2. CÁC HÀM RSA CHÍNH ---
def generate_keys(bits=1024):
    print(f"[*] Đang tạo cặp khóa RSA {bits} bits...")
    p = getPrime(bits // 2)
    q = getPrime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, phi)
    
    
    # Ghi khóa vào file trong thư mục keys/ đúng cấu trúc của bạn
    with open('keys/public_key.txt', 'w') as f:
        f.write(f"n={hex(n)}\ne={hex(e)}")
    with open('keys/private_key.txt', 'w') as f:
        f.write(f"n={hex(n)}\nd={hex(d)}")
    
    print("[+] Đã lưu khóa vào thư mục keys/")
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    m_int = bytes_to_long(message.encode())
    return pow(m_int, e, n) # C = M^e mod n

def decrypt(ciphertext, private_key):
    d, n = private_key
    m_int = pow(ciphertext, d, n) # M = C^d mod n
    return long_to_bytes(m_int).decode()

# --- 3. GIẢI QUYẾT CÁC TASK TRONG PDF (SỐ LIỆU THẬT) ---
def solve_pdf_tasks():
    print("\n" + "="*40)
    print(" GIẢI CHI TIẾT CÁC TASK:")
    print("="*40)
    
    # Task 1: Tìm d
    p_1 = int("F7E75FDC469067FFDC4E847C51F452DF", 16)
    q_1 = int("E85CED54AF57E53E092113E62F436F4F", 16)
    e_1 = int("0D88C3", 16)
    n_1 = p_1 * q_1
    d_1 = mod_inverse(e_1, (p_1-1)*(q_1-1))
    print(f"[Task 1] Khóa bí mật d: {hex(d_1).upper()}\n")

    # Dữ liệu chung cho Task 2, 3, 4
    n_common = int("DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5", 16)
    e_common = 0x010001
    d_common = int("74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D", 16)

    # --- TASK 2: Encrypting a Message ---
    msg2 = "A top secret!"
    m2_int = bytes_to_long(msg2.encode())
    c2 = pow(m2_int, e_common, n_common) # C = M^e mod n
    print(f"[Task 2] Mã hóa thông điệp '{msg2}':\n{hex(c2).upper()}\n")
    # Task 3: Giải mã bản mã C
    c_3 = int("8C0F971DF2F3672B28811407E2DABBE1DA0FEBBBDFC7DCB67396567EA1E2493F", 16)
    m_3_int = pow(c_3, d_common, n_common)
    print(f"[Task 3] Bản rõ sau giải mã: {long_to_bytes(m_3_int).decode()}\n")

    # Task 4: Ký tên lên thông điệp (Signing)
    msg_4a = "I owe you $2000."
    s_4a = pow(bytes_to_long(msg_4a.encode()), d_common, n_common)
    print(f"[Task 4] Chữ ký cho '$2000': {hex(s_4a).upper()}")
    
    msg_4b = "I owe you $3000."
    s_4b = pow(bytes_to_long(msg_4b.encode()), d_common, n_common)
    print(f"[Task 4] Chữ ký cho '$3000': {hex(s_4b).upper()}")
    print(" -> Quan sát: Khi thông điệp thay đổi dù chỉ 1 ký tự, chữ ký thay đổi hoàn toàn.\n")

    # Task 5: Xác thực chữ ký (Verifying)
    n_5 = int("AE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115", 16)
    e_5 = 0x010001
    s_5 = int("643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F", 16)
    msg_5 = "Launch a missile."
    # Xác thực: S^e mod n có bằng M không?
    m_check = pow(s_5, e_5, n_5)
    if long_to_bytes(m_check).decode() == msg_5:
        print(f"[Task 5] Xác thực chữ ký cho '{msg_5}': THÀNH CÔNG (Hợp lệ)")
    else:
        print(f"[Task 5] Xác thực thất bại!")
    # Chạy giải bài tập PDF
if __name__ == "__main__":
    generate_keys(1024)
    solve_pdf_tasks()
    
