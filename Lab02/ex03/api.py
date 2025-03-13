import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from cipher.railfence.railfence_cipher import RailFenceCipher

from flask import Flask, request, jsonify

app = Flask(__name__) 
railfence_cipher = RailFenceCipher()

@app.route("/api/railfence/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)