from hashlib import sha256
from time import asctime

class Blockchain:
    def __init__(self):
        self.blockchain = {}
        self.chain = 0
        self.prevAddrs = '0000000000000000000000000000000000000000000000000000000000000000'
    
    def newBlock(self, dataIn):
        hashAddrs = '0000000000000000000000000000000000000000000000000000000000000000'
        nonce = 0
        
        while(hashAddrs[:3] != '333'):
            newBlock = {
                'header' : self.chain,
                'time' : asctime(),
                'prevAddrs' : self.prevAddrs,
                'nonce' : nonce,
                'data' : dataIn
            }
            nonce = nonce + 1
            hashAddrs = sha256(str(newBlock).encode()).hexdigest()
        
        self.blockchain.update({'block %i' %self.chain : newBlock})
        self.chain = self.chain + 1
        self.prevAddrs = hashAddrs
    
    def check(self):
        checkedBlock = {}
        prevAddrsCheck = '0000000000000000000000000000000000000000000000000000000000000000'
        cHash = '0000000000000000000000000000000000000000000000000000000000000000'
        
        for cBlock in self.blockchain:
            blockCheck =  {
                'header' : self.blockchain[cBlock]['header'],
                'time' : self.blockchain[cBlock]['time'],
                'prevAddrs' : prevAddrsCheck,
                'nonce' : self.blockchain[cBlock]['nonce'],
                'data' : self.blockchain[cBlock]['data']
            }
            
            cHash = sha256(str(blockCheck).encode()).hexdigest()
            prevAddrsCheck = cHash
            if(cHash[:3] == '333'):
                checkedBlock.update({str(cBlock) : 'valid'})
            else:
                checkedBlock.update({str(cBlock) : 'invalid'})
        return checkedBlock


x = {
    "nama" : "adill deswal agi firmansyah",
    "kelas" : "2a",
    "prodi" : "teknik elektro"
}

bc = Blockchain()

bc.newBlock('apel')
bc.newBlock('nanas')
bc.newBlock('mangga')
bc.newBlock('alpukat')

for i in bc.blockchain.items():
    print(i)

# bc.blockchain['block 2']['data'] = 'banana'
# print(bc.check())
# bc.blockchain['block 2']['data'] = 'mangga'
print(bc.check())

# while(True):
#     inp = input('check' )
#     if(inp == '0'):
#         bc.check()
#     else:
#         break