from Crypto.Cipher import AES

key = 'SuperVinter2020!'

#iv = 'efd67e45-9a1c-47a9-82db-da32d339cfc2.z0mb13z.ctf'
iv = "65 66 64 36 37 65 34 35 2d 39 61 31 63 2d 34 37 61 39 2d 38 32 64 62 2d 64 61 33 32 64 33 33 39"

aes = AES.new(key, AES.MODE_CFB, iv)


# KJk4PE5TcPF2w9Y9WjCpqTfJEpou7P.efd67e45-9a1c-47a9-82db-da32d339cfc2.z0mb13z.ctf
# KJk4PE5TcPF2w9Y9WjCpqTfJEpou7P.efd67e45-9a1c-47a9-82db-da32d339cfc2.z0mb13z.ctf: type TLSA, class IN
# 2fYzdjYWYuSxcLZ5ueyLXF9ArB8ZkN1RbfySK43Qc4H57gptcyLLnr2cGZ3VDyB.3W9N7Pug3fZXco7o8Wc7AeR5k.efd67e45-9a1c-47a9-82db-da32d339cfc2.z0mb13z.ctf

# base 58?
code = "1e 4b 4a 6b 34 50 45 35 54 63 50 46 32 77 39 59 39 57 6a 43 70 71 54 66 4a 45 70 6f 75 37 50 24"

decode = aes.decrypt(code)

'''
1e 4b 4a 6b 34 50 45 35 54 63 50 46 32 77 39 59   .KJk4PE5TcPF2w9Y
39 57 6a 43 70 71 54 66 4a 45 70 6f 75 37 50 24   9WjCpqTfJEpou7P$
65 66 64 36 37 65 34 35 2d 39 61 31 63 2d 34 37   efd67e45-9a1c-47
61 39 2d 38 32 64 62 2d 64 61 33 32 64 33 33 39   a9-82db-da32d339
63 66 63 32 07 7a 30 6d 62 31 33 7a 03 63 74 66   cfc2.z0mb13z.ctf
'''