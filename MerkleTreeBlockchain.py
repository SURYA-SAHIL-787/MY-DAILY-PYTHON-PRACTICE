import hashlib

class MerkleNode:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        if value:
            self.hash = self._hash(value)
        else:
            # Combine child hashes for interior nodes
            left_hash = left.hash if left else ""
            right_hash = right.hash if right else ""
            self.hash = self._hash(left_hash + right_hash)

    def _hash(self, data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = self._build_tree(transactions)

    def _build_tree(self, data_blocks):
        if not data_blocks:
            return None
        
        # Create leaf nodes from transaction data
        current_level = [MerkleNode(value=tx) for tx in data_blocks]

        # Bottom-up tree construction
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                # Handle odd number of elements by duplicating the last node
                right = current_level[i + 1] if i + 1 < len(current_level) else current_level[i]
                parent = MerkleNode(left=left, right=right)
                next_level.append(parent)
            current_level = next_level

        return current_level[0]

    def get_root_hash(self):
        return self.root.hash if self.root else None

# Example Usage: Real-world Blockchain Transaction Integrity Verification
if __name__ == "__main__":
    valid_transactions = [
        "Alice pays Bob 5 BTC",
        "Bob pays Charlie 2 BTC",
        "Charlie pays Dave 1 BTC",
        "Dave pays Eve 0.5 BTC"
    ]
    
    blockchain_block = MerkleTree(valid_transactions)
    print("Original Merkle Root Hash:     ", blockchain_block.get_root_hash())
    
    # Simulating a malicious tampering attempt on a single transaction in the ledger
    tampered_transactions = [
        "Alice pays Bob 500 BTC",  # Tampered amount!
        "Bob pays Charlie 2 BTC",
        "Charlie pays Dave 1 BTC",
        "Dave pays Eve 0.5 BTC"
    ]
    
    tampered_block = MerkleTree(tampered_transactions)
    print("Tampered Merkle Root Hash:     ", tampered_block.get_root_hash())
    print("Data integrity check passed?   ", blockchain_block.get_root_hash() == tampered_block.get_root_hash())
