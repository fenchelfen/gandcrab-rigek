import base64


def crypt(key, data):
    S = list(range(256))
    j = 0
    for i in list(range(256)):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]
    j = 0
    y = 0
    out = []
    for char in data:
        j = (j + 1) % 256
        y = (y + S[j]) % 256
        S[j], S[y] = S[y], S[j]
        out.append(chr(ord(char) ^ S[(S[j] + S[y]) % 256]))
    return ''.join(out)


def main():
	with open('to_be_encrypted.js') as i:
		with open('encrypted.js', 'w') as o:
			o.write('fvbnvbn("' + base64.b64encode(''.join([hex(ord(c))[-2:].replace('x', '0') for c in crypt('secret_key', i.read())]).encode('ascii')).decode('utf-8') + '")')


if __name__ == '__main__':
	main()
