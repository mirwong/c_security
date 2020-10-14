# Cryptography: Hashes

- Looked at hashes
- How does "brute force" breaking of hashes increase with time?
  - Given length of plaintext, encrypt all possibilities using the hash until one matches
  - Increases exponentially with time (on second thought this is obvious...)
  - a bit more time also added to the hashing process as the combos get longer
- Researched a bit on how different hashes are used for different applications
  - ex. streaming requires hashes that are faster to confirm
  - something more secure such as login has a more complex hash as it doesn't matter to most users to wait an extra few seconds
