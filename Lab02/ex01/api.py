from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher  # Import đúng class CaesarCipher

app = Flask(__name__)

# Tạo một instance của CaesarCipher để tái sử dụng
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    """API mã hóa văn bản bằng Caesar Cipher."""
    data = request.get_json()

    # Kiểm tra nếu request không chứa dữ liệu hợp lệ
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({"error": "Missing 'plain_text' or 'key' in request"}), 400

    plain_text = data['plain_text']
    try:
        key = int(data['key'])  # Chuyển đổi key sang số nguyên
    except ValueError:
        return jsonify({"error": "'key' must be an integer"}), 400

    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)

    return jsonify({'encrypted_message': encrypted_text}), 200

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    """API giải mã văn bản bằng Caesar Cipher."""
    data = request.get_json()

    # Kiểm tra nếu request không chứa dữ liệu hợp lệ
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({"error": "Missing 'cipher_text' or 'key' in request"}), 400

    cipher_text = data['cipher_text']
    try:
        key = int(data['key'])  # Chuyển đổi key sang số nguyên
    except ValueError:
        return jsonify({"error": "'key' must be an integer"}), 400

    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)

    return jsonify({'decrypted_message': decrypted_text}), 200

# Chạy server Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
