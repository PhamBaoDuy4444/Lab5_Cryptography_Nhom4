

# LAB 5: CRYPTOGRAPHY 

## 🛠 CHI TIẾT NHIỆM VỤ

### 📁 Task 1: Cryptography Toolkit (`/1_Toolkit`)
- Xây dựng bộ công cụ mã hóa đối xứng: AES (CBC/ECB), DES.
- Xây dựng các hàm băm: MD5, SHA-256.
- Hoàn thiện giao diện menu (`main.py`) để chạy thử các tính năng.

### 📁 Task 2: MD5 Collision Attack (`/2_MD5_Collision`)
- Sử dụng `fastcoll.exe` tạo 2 file va chạm MD5 (`file1.bin`, `file2.bin`).
- Viết script kiểm chứng bằng Python.
- Giải thích hiện tượng va chạm trong báo cáo.

### 📁 Task 3: RSA Implementation (`/3_RSA`)
- Tự lập trình thuật toán RSA: Sinh khóa (p, q, n, e, d).
- Viết hàm Encryption/Decryption toán học.
- Lưu trữ khóa tại folder `/keys`.

### 📁 Task 4: PKI Infrastructure (`/4_PKI`)
- Sử dụng OpenSSL thiết lập Root CA.
- Tạo CSR và ký chứng chỉ cho Server.
- Kiểm tra tính hợp lệ của chuỗi chứng chỉ (Chain of Trust).

---

## 🚀 HƯỚNG DẪN CHẠY CODE
1. Cài đặt Python 3.x
2. Cài đặt thư viện: `pip install pycryptodome`
3. Truy cập từng folder và chạy các file `.py` hoặc lệnh OpenSSL theo file `commands.sh`.