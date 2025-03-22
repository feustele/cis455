import pytest
import hashlib
from pathlib import Path
import merkletree

def test_filehash_single_file():
    # Create a test file
    file_path = Path("test_file.txt")
    file_path.write_text("This is a test file.")

    # Calculate the hash using filehash()
    calculated_hash = merkletree.filehash(file_path)

    # Calculate the expected hash using hashlib
    with open(file_path, 'rb') as file:
        data = file.read()
        expected_hash = hashlib.sha1(data).hexdigest()

    # Assert that the hashes match
    assert calculated_hash == expected_hash

    # Clean up the temporary file
    file_path.unlink()

def test_merkletree_single_file():
    # Create test file
    file_path = Path("test_file.txt")
    file_path.write_text("This is a test file.")

    # Calculate the top hash using merkletree()
    top_hash = merkletree.merkletree(file_path)

    # Calculate the expected hash using filehash()
    expected_hash = merkletree.filehash(file_path)

    # Assert that the top hash matches the expected hash when there's only one file
    assert top_hash == expected_hash

    file_path.unlink()

def test_merkletree_multiple_files():
    # Create multiple temporary files with different content
    file_paths = [Path("test_file.txt"), Path("test_file2.txt"), Path("test_file3.txt")]
    file_paths[0].write_text("This is the first file.")
    file_paths[1].write_text("This is the second file.")
    file_paths[2].write_text("This is the third file.")

    # Calculate the top hash using your merkletree function
    top_hash = merkletree.merkletree(*file_paths)

    # Assert that the top hash is not None
    assert top_hash is not None

    for file_path in file_paths:
        file_path.unlink()

def test_merkletree_modified_file():
    # Create multiple temporary files with different content
    file_paths = [Path("test_file1.txt"), Path("test_file2.txt")]
    file_paths[0].write_text("This is the first file.")
    file_paths[1].write_text("This is the second file.")

    # Calculate the initial top hash
    initial_top_hash = merkletree.merkletree(*file_paths)

    # Modify one of the files
    file_paths[0].write_text("hahaha I changed the file >:}.")

    # Calculate the new top hash
    modified_top_hash = merkletree.merkletree(*file_paths)

    # Assert that the top hash has changed
    assert initial_top_hash != modified_top_hash

    for file_path in file_paths:
        file_path.unlink()
