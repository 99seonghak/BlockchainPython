from hashlib import sha256 as sha

def hashcash(msg, difficulty):
    nonce = 0
    while True:
        target = '%s%d' %(msg, nonce)
        ret = sha(target.encode()).hexdigest()

        #if ret[:difficulty] == '1'*difficulty:
        if ret[:difficulty] == '0000':
            print()
            print('new hash value   : ' + ret)
            print('--> NONCE = %d' %nonce)
            break
        nonce += 1 

if __name__ == '__main__':
    msg = '99seonghak'
    difficulty = 4

    print("msg's hash value : "+ sha((msg.encode())).hexdigest())
    hashcash(msg, difficulty)
