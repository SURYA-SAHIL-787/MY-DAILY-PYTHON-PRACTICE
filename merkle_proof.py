import hashlib

def verify_merkle_proof(target_hash, merkle_proof, merkle_root):
    def hash_pair(left, right):
        combined = left + right
        return hashlib.sha256(combined.encode('utf-8')).hexdigest()
    
    current_hash = target_hash
    
    for sibling_hash, direction in merkle_proof:
        if direction == 'left':
            current_hash = hash_pair(sibling_hash, current_hash)
        else:
            current_hash = hash_pair(current_hash, sibling_hash)
            
    return current_hash == merkle_root
