import hashlib
import math

class PeerToPeerFileVerifier:
    @staticmethod
    def _hash(data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    @staticmethod
    def build_merkle_tree(chunks):
        """Builds a Merkle tree from file chunks and returns all levels for proof generation."""
        if not chunks:
            return [], ""

        current_level = [PeerToPeerFileVerifier._hash(chunk) for chunk in chunks]
        tree_levels = [current_level]

        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i + 1] if i + 1 < len(current_level) else left
                parent = PeerToPeerFileVerifier._hash(left + right)
                next_level.append(parent)
            tree_levels.append(next_level)
            current_level = next_level

        return tree_levels, tree_levels[-1][0] # Returns full tree structure and Root Hash

    @staticmethod
    def generate_proof(tree_levels, index):
        """Generates a cryptographic Merkle proof for a specific chunk index."""
        proof = []
        for level in tree_levels[:-1]: # Exclude root level
            is_right_node = (index % 2 == 1)
            sibling_index = index - 1 if is_right_node else index + 1
            
            if sibling_index < len(level):
                proof.append((level[sibling_index], not is_right_node))
            else:
                proof.append((level[index], not is_right_node)) # Handle padding
            index //= 2
        return proof

    @staticmethod
    def verify_proof(chunk_data, proof, root_hash):
        """Verifies if a downloaded file chunk belongs to the verified torrent file root hash."""
        current_hash = PeerToPeerFileVerifier._hash(chunk_data)
        for sibling_hash, is_left_sibling in proof:
            if is_left_sibling:
                current_hash = PeerToPeerFileVerifier._hash(sibling_hash + current_hash)
            else:
                current_hash = PeerToPeerFileVerifier._hash(current_hash + sibling_hash)
        return current_hash == root_hash

# Example Usage: BitTorrent Piece Verification via Merkle Proofs
if __name__ == "__main__":
    file_chunks = ["Chunk_0: Video Data A", "Chunk_1: Video Data B", "Chunk_2: Video Data C", "Chunk_3: Video Data D"]
    
    # 1. Seeder creates the Merkle Tree and shares the Root Hash
    tree_levels, root_hash = PeerToPeerFileVerifier.build_merkle_tree(file_chunks)
    print("Torrent Root Hash (Shared by Seeder):", root_hash)

    # 2. Peer downloads Chunk #2 and requests a Merkle proof for verification
    target_index = 2
    proof = PeerToPeerFileVerifier.generate_proof(tree_levels, target_index)
    
    # 3. Peer verifies the downloaded chunk against the trusted root hash without downloading the whole file
    is_valid = PeerToPeerFileVerifier.verify_proof(file_chunks[target_index], proof, root_hash)
    print(f"Is downloaded '{file_chunks[target_index]}' authentic and uncorrupted? {is_valid}")
