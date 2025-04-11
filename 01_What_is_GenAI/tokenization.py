import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab Size", encoder.n_vocab) # 2,00,019 (200K)

text = "Hello, how are you doing today?"
print("Text :",text)
tokens = encoder.encode(text)

print("Encoded Tokens :", tokens) # Tokens [13225, 11, 1495, 553, 481, 5306, 4044, 30]

my_tokens = [13225, 11, 1495, 553, 481, 5306, 4044, 30]
decoder = encoder.decode(my_tokens)
print("Decoded as :", decoder)