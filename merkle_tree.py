import hashlib

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = self._build_tree(transactions)

    def _hash(self, data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def _build_tree(self, nodes):
        if len(nodes) == 0:
            return None
        
        hashed_nodes = [self._hash(node) for node in nodes]
        
        while len(hashed_nodes) > 1:
            if len(hashed_nodes) % 2 != 0:
                hashed_nodes.append(hashed_nodes[-1])
            
            next_level = []
            for i in range(0, len(hashed_nodes), 2):
                combined = hashed_nodes[i] + hashed_nodes[i+1]
                next_level.append(self._hash(combined))
            hashed_nodes = next_level
            
        return hashed_nodes[0]
