# L1, L2, L3 and L4 are files. Your program is supposed to compute Top Hash. You can choose to use MD5 or SHA1 for hashing.
# You can use source code of SHA1 or MD5 from the internet.
import hashlib
from pathlib import Path

def filehash(filename):
  h = hashlib.sha1()
  # creates an instance of sha1
  with open(filename, 'rb') as file:
    while True:
      data = file.read(65536)
      # reads from file path in 64k chunks
      if not data:
        break
      h.update(data)
      # hashes data using sha1
      return h.hexdigest()

def merkletree(*args):
  # no upper bound to number of files - dynamic
  filename = None
  # initialize the filename to nothing
  if len(args) == 1:
    filename = Path(args[0]).resolve()
    # resolves to file
    return filehash(filename)
    # if there's only one argument, hash and pass
  while len(args) > 1:
    # if more than one argument
    new_args = []
    if len(args) % 2 == 0:
      for i in range(0, len(args), 2):
        # processes argument list in pairs
        filename = Path(args[i]).resolve()
        filename2 = Path(args[i + 1]).resolve()
        # resolves pair to files
        if i + 1 < len(args):
          # if the length of the arguments is not less than the next pair's value
          file1 = filehash(filename)
          file2 = filehash(filename2)
          new_args.append(file1 + file2)
          #hash the files and append them to the new_args list
    else:
      # if only one argument entry remains, hash and append to list. It doesn't like it if I try to cut the "len == 1" before while loop
      if filename is None:
          filename = Path(args[0]).resolve()
      file1 = filehash(filename)
      new_args.append(file1)
    # once all hashes are calculated, reassign new_args to args
    args = new_args
  return args[0]
# Input: Pathnames of files. There should be no upper bound on the number of files. Your program should be able to handle thousands of files.

# Output: Compute Top Hash and demonstrate that Top Hash does not match when one or more files are modified.


# Deliverables:
  # Source code submission using GitHub.
  # A printout of the output.

#The following grading criteria will be applied:
  #Correctness & Completeness 70%
  #Program Output & Testing 15%
  #Program Organization & Source Code Management 10%
  #Documentation 5%
