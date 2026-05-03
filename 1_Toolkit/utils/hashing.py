import hashlib


SUPPORTED_HASHES = {
    "MD5": hashlib.md5,
    "SHA256": hashlib.sha256,
}


def handle_hashing(algo, text):
    if not algo:
        return {"error": "Thieu thuat toan bam"}

    if text is None:
        return {"error": "Thieu du lieu dau vao"}

    normalized_algo = algo.strip().upper().replace("-", "")
    hash_func = SUPPORTED_HASHES.get(normalized_algo)

    if hash_func is None:
        return {"error": "Thuat toan bam khong ho tro"}

    data = str(text).encode("utf-8")
    return {"result": hash_func(data).hexdigest()}
