import hashlib

class GitBlob:
    """Represents a file (leaf node) in Git's Merkle DAG."""
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content
        self.hash = hashlib.sha256(content.encode('utf-8')).hexdigest()

class GitTree:
    """Represents a directory (intermediate node) containing files or sub-trees."""
    def __init__(self):
        self.entries = {}  # Maps name -> object hash

    def add_entry(self, name, obj_hash):
        self.entries[name] = obj_hash

    def compute_hash(self):
        # Sort keys to ensure deterministic hashing regardless of insertion order
        serialized = "".join(f"{name}:{h}" for name, h in sorted(self.entries.items()))
        return hashlib.sha256(serialized.encode('utf-8')).hexdigest()

class GitCommit:
    """Represents a commit pointing to a root tree snapshot."""
    def __init__(self, message, tree_hash, parent_hash=None):
        self.message = message
        self.tree_hash = tree_hash
        self.parent_hash = parent_hash
        
        metadata = f"{message}|{tree_hash}|{parent_hash or ''}"
        self.hash = hashlib.sha256(metadata.encode('utf-8')).hexdigest()

# Example Usage: Simulating Git's Content-Addressable Storage & Merkle Structure
if __name__ == "__main__":
    # Create blobs (files)
    main_py = GitBlob("main.py", "print('Hello World')")
    readme_md = GitBlob("README.md", "# Project Documentation")

    # Create root tree (directory structure)
    root_tree = GitTree()
    root_tree.add_entry(main_py.filename, main_py.hash)
    root_tree.add_entry(readme_md.filename, readme_md.hash)
    root_tree_hash = root_tree.compute_hash()

    # Create commit
    commit1 = GitCommit("Initial commit", root_tree_hash)

    print("Git Blob (main.py) Hash:  ", main_py.hash)
    print("Git Tree Root Hash:      ", root_tree_hash)
    print("Git Commit Hash:         ", commit1.hash)
