from client import *
from openssl import *
from hashlib import sha256, md5
import random
import base64
import math
c = Connection()
#print(c.post("/bin/login",user="guest",password="guest"))
#print(c.get("/home/"))

#mess = c.get("/home/guest/NASA.bin")
#cyphe = decrypt(mess, 'ISEC')
#print(cyphe)
#print(c.get("/home/guest/NASA.bin"))
user1 = "wilkinsonethan"
password1 = "!r3YPa7u#&"
print(c.post("/bin/login",user=user1,password=password1))
IV = c.get("/sbin/monitor-settings")
log  = c.get("/bin/login/CHAP")
plaintext = user1 + "-" + log['challenge']
response = encrypt(plaintext,password1)
print(c.post("/bin/login/CHAP",user = user1,response = response))
#print(c.get("/sbin/monitor-settings"))
IV = c.get("/sbin/monitor-settings")

#print(c.get("/home/wilkinsonethan"))
#print(c.get("/home/wilkinsonethan/bye-bye.txt"))
#print(c.get("/home/wilkinsonethan/INBOX"))
#print(c.get("/home/wilkinsonethan/INBOX/4250"))
#print(c.get("/bin/crypto_helpdesk"))
#print(c.get("/bin/crypto_helpdesk/ticket/493"))
## TUtoriel
#attachement = c.get("/bin/crypto_helpdesk/ticket/493/attachment/fetch-me")
#mail = (c.get("/bin/crypto_helpdesk/ticket/493/attachment/client"))['email']
#dic = {'foo':attachement,'bar':42}
#print(dic)
#print("______\n",mail,"\n____\n")
#print(c.post("/bin/sendmail",to=mail,subject="Tutoriel",content=dic))
#print(c.post("/bin/crypto_helpdesk/ticket/493/close"))

##Ticket 2
#attachement = c.get("/bin/crypto_helpdesk/ticket/494/attachment/password")
#mail = "omarschwartz"
#data = c.get("/bin/long-term-storage/1024")
#message = c.get("/bin/long-term-storage/device/17b9264b")
#cypher = encrypt(message,attachement)
#print(c.post("/bin/sendmail",to=mail,subject="Beltran Group",content=cypher))

## Tciket 3
#cipher = c.get("/bin/crypto_helpdesk/ticket/495/attachment/cipher")
#mdp = c.get("/bin/crypto_helpdesk/ticket/495/attachment/password")
#mail = "hawkinsjesse"
#cipher_text = c.get("/bin/crypto_helpdesk/ticket/495/attachment/ciphertext")
#print(cipher)
#real_message = decrypt(cipher_text,mdp,cipher = cipher)
#print(decrypt(cipher_text,mdp,cipher = cipher))
#print(c.post("/bin/sendmail",to=mail,subject="Problème de déchiffrement (méthode inhabituelle)",content=real_message))

""" message = c.get("/bin/crypto_helpdesk/ticket/517/attachment/message")
public_key = c.get("/bin/crypto_helpdesk/ticket/517/attachment/public-key")
mail = c.get("/bin/crypto_helpdesk/ticket/517/attachment/client")['email']
cypher = pkencrypt(message,public_key)
print(cypher)
cypher = base64.b64encode(cypher).decode()
print(c.post("/bin/sendmail",to=mail,subject="Message à chiffrer (clef publique)",content=cypher))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
print(c.post("/bin/crypto_helpdesk/ticket/517/close")) """

"""
print(c.get("/bin/crypto_helpdesk/ticket/518"))
id  = c.get("/bin/crypto_helpdesk/ticket/518/attachment/contact")
client = c.get("/bin/crypto_helpdesk/ticket/518/attachment/client")
message = "informations très très très sensibles"
key = c.get("/bin/key-management/"+id)
cypher = pkencrypt(message,key)
cypher = base64.b64encode(cypher).decode()
k,s = genpkey()
print(k,s)
print(c.post("/bin/key-management/upload-pk",public_key = k,confirm=True))
print(c.post("/bin/sendmail",to=id,subject="Message à chiffrer (clef publique)",content=cypher))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
send = c.get("/home/wilkinsonethan/INBOX/"+str(i)+"/body")
print(send)
print(len(send.encode('utf-8')))
mess = pkencrypt(base64.b64decode(send),s,0)
print(mess.decode())
print(c.post("/bin/sendmail",to=client['email'],subject="Message à chiffrer (clef publique)",content=mess.decode()))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
print(c.post("/bin/crypto_helpdesk/ticket/518/close"))

## Ticket 519
print(c.get("/bin/crypto_helpdesk/ticket/519"))
contact  = c.get("/bin/crypto_helpdesk/ticket/519/attachment/contact")
client = c.get("/bin/crypto_helpdesk/ticket/519/attachment/client")
client_pk = c.get(("/bin/key-management/{}/pk").format(contact))
temp_key = "Ab560plfjcuaoddI3"
print(temp_key)
reciprocity = c.get("/bin/crypto_helpdesk/ticket/519/attachment/reciprocity")
session_key = pkencrypt(temp_key,client_pk)
session_key = (base64.b64encode(session_key).decode())
# Encrypt the payload
payload = encrypt(reciprocity,temp_key)
content = {'session_key':session_key,'payload':payload}
print(c.post("/bin/sendmail",to=contact,subject="Message à chiffrer (clef hybrid)",content=content))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
print(c.post("/bin/crypto_helpdesk/ticket/519/close"))
## Contrat de travaik
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
email = c.get("/home/wilkinsonethan/INBOX/"+str(i)+"/sender")
contract = c.get("/home/wilkinsonethan/INBOX/"+str(i)+"/body")

print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
signed = sign(contract,s)
print(c.post("/bin/sendmail",to=email,subject="Votre nouveau contrat de travail",content=base64.b64encode(signed).decode()))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
"""
"""
def sxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

## SAV BYE BYE
print(c.get("/bin/police_hq"))
print(c.get("/bin/police_hq/ticket/683"))
text_fileb64 = c.get("/bin/police_hq/ticket/683/attachment/exhibit-A")
print(text_fileb64)
text_file = base64.b64decode(text_fileb64)
plain_pbmb64 = c.get("/bin/police_hq/ticket/683/attachment/exhibit-B")
plain_pbm = base64.b64decode(plain_pbmb64)
i = c.get("/bin/police_hq/ticket/683/attachment/i")
j = c.get("/bin/police_hq/ticket/683/attachment/j")

key = sxor(text_fileb64, plain_pbmb64)
size = len(key)
mask0 = "0"*size
mask1 = "1"*size
print(text_file.decode())
print(sxor(key,mask0).encode('utf-8'))
print(sxor(key,mask1).encode('utf-8'))
print(sxor(sxor(key,mask0),mask1).encode('utf-8'))
"""

"""
username = "shane90"
response="U2FsdGVkX1/g2bSIROGwVLNRdDhruketd/M6cseXvKi2IB1gukEstWbel7zPgyZY\nrsNDGo3dl+qj8qmgRkQQtQ==\n"
print(c.get("/bin/login/CHAP"))
print(c.get("/bin/police_hq/ticket/686/attachment/trace"))
challenge="6b9d0e4104b54b138d59445ac4adca5f"
words=c.get("/share/words")
words=words.split('\n')
for w in words:
    plaintext=username+"-"+challenge
    print(w)
    try:
        rep=decrypt(response,w)
        if rep==plaintext:
            print(w)
            break
    except:
        pass

username="shane90"
password='means'
log  = c.get("/bin/login/CHAP")
plaintext = username + "-" + log['challenge']
response = encrypt(plaintext,password)
print(c.post("/bin/login/CHAP",user = username,response = response))
"""
bande = 4919

def get_stp(K,adess):
        dict = {'method':'GET','url':adess}
        jdict =json.dumps(dict)
        enc_jdict = encrypt(jdict,K)
        response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))
        return(decrypt_b64(response,K))



def post_stp(K,adress,args):
        dict = {'method':'POST','url':adress,'args':args}
        jdict =json.dumps(dict)
        enc_jdict = encrypt(jdict,K)
        response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))
        return(decrypt_b64(response,K))



def dh_auten(username):
    k,s = genpkey()
    print(c.post("/bin/key-management/upload-pk",public_key = k,confirm=True))
    parameters = c.get("/bin/login/dh/parameters")
    g = parameters['g']
    p = parameters['p']
    certificate = c.get("/bin/banks/CA")
    x = int(random.uniform(0,500))
    A = pow(g,x)%p
    dic = c.post("/bin/login/dh",username=username,A = A)
    pk = get_pub_cert(certificate)
    B = dic['B']
    k = dic['k']
    S = "{},{},{},{}".format(A,B,k,username)
    verif = verify_signature(pk,dic['signature'],S)
    if(verif == False):
        print("verification invalide")
        return
    AB = pow(B,x)%p
    H = sha256()
    size = 1 + AB.bit_length() // 8
    H.update(AB.to_bytes(size, byteorder='big'))
    K = H.hexdigest()
    print(K)
    adresse = "/bin/login/dh/confirmation"
    T = "{},{},{},{}".format(A,B,k,"UGLIX")
    signature = sign(T,s)
    signature = base64.b64encode(signature).decode()
    post_stp(K,adresse,{'signature':signature})
    return K,k,s

K,k,s = dh_auten(user1)
print(get_stp(K,"/bin/hackademy"))



############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################




from client import *
from openssl import *
import base64
import random
from hashlib import sha256
import json




def get_stp(url,K):
    dict={"url": url , "method": "GET"}
    dict_json=json.dumps(dict)
    plaintext=encrypt(dict_json, K)
    plaintext=base64.b64decode(plaintext)
    try:
        rep=c.post_raw('/bin/gateway',plaintext)
        return(decrypt_b64(rep,K))
    except Exception as e:
        return(decrypt_b64(e.msg,K))
    return(decrypt_b64(rep,K))

def post_stp(url,args,K):
    if(args!=""):
        dict={"url": url , "method": "POST", "args": args}
    else:
        dict={"url": url , "method": "POST"}
    dict_json=json.dumps(dict)
    plaintext=encrypt(dict_json, K)
    plaintext=base64.b64decode(plaintext)
    try:
        rep=c.post_raw('/bin/gateway',plaintext)
        return(decrypt_b64(rep,K))
    except Exception as e:
        return(decrypt_b64(e.msg,K))
    return(decrypt_b64(rep,K))

def dh_auten(username):
    k,s = genpkey()
    print(c.post("/bin/key-management/upload-pk",public_key = k,confirm=True))
    parameters = c.get("/bin/login/dh/parameters")
    g = parameters['g']
    p = parameters['p']
    certificate = c.get("/bin/banks/CA")
    x = int(random.uniform(0,500))
    A = pow(g,x,p)
    dic = c.post("/bin/login/dh",username=username,A = A)
    pk = get_pub_cert(certificate)
    B = dic['B']
    k = dic['k']
    S = "{},{},{},{}".format(A,B,k,username)
    verif = verify_signature(pk,dic['signature'],S)
    if(verif == False):
        print("verification invalide")
        return
    AB = pow(B,x)%p
    H = sha256()
    size = 1 + AB.bit_length() // 8
    H.update(AB.to_bytes(size, byteorder='big'))
    K = H.hexdigest()
    print(K)
    adresse = "/bin/login/dh/confirmation"
    T = "{},{},{},{}".format(A,B,k,"UGLIX")
    signature = sign(T,s)
    signature = base64.b64encode(signature).decode()
    print(post_stp(adresse,{'signature':signature},K))
    return(K)
"""
K=dh_auten(username)
print(get_stp("/bin/banks/drh",K))
print(get_stp("/bin/banks/drh/rules",K))
get_stp("/bin/jukebox/disable",K)
get_stp("/bin/jukebox/stop",K)
"""

def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def modinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b

def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b/2)

    return x % c

def decrypt_elgamal(h,y,p,a,b):
    coup=(b*modinv(pow(h,y,p),p))%p
    return coup

from random import randrange, getrandbits
def is_prime(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n-1:
            j = 1
            while j < s and x != n-1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
        return True

def generate_prime_candidate(length):
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=1024):
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 256):
        p = generate_prime_candidate(length)
    return p


def debut_match(K):
    p = int('FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1'
        '29024E088A67CC74020BBEA63B139B22514A08798E3404DD'
        'EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245'
        'E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED'
        'EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D'
        'C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F'
        '83655D23DCA3AD961C62F356208552BB9ED529077096966D'
        '670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF', base=16)


    test = (p-1)//2
    while(pow(88275625857605,test,p)==1 or pow(19779480974019653,test,p)==1 or pow(18939445432636760,test,p)==1 ):
        p = generate_prime_number(2048)
        test = (p-1)//2
    g = 4
    """
    p=16973503711342477120805274135165619430835938743130314432054926136585928578912660174525970168659915374359727660856827057233817677312192836048898602632666177723528093433540324359025833006067992002566412718794891266025607160515284251482242568317403493898696382741971476164339781911130801156170188729203368675405031096029001040490171163591856775940982483031628912906850898345778957570258953707546194908235407045793360264256745116018346951723960210122845670298475045087367649843749596147556564176481254188618555819016544745578842756258847255193764842219562330491104021390515564019379529467330118170590366570162451975730327
    #P posssède bien 2048 bit, il est aussi un nombre super
    y = randrange(3000,20000)
    q = p-1//2
    temp = 2
    print(temp)
    while(pow(y,temp,p)==1):
        y = randrange(300,2000000)

    g = pow(y,temp,p)
    print(g)
    """
    h = pow(g,int(random.uniform(300,5000)),p)
    print(is_prime(g))
    try:
        key_adversaire=json.loads(post_stp("/bin/banks/assistant/start",{'p': p,'g': g,'h':h },K))
    except Exception as e:
        print(post_stp("/bin/banks/assistant/start",{'p': p,'g': g,'h':h },K))
    print(key_adversaire)
    return(key_adversaire,g,h,p)


def round(K,g,p,h,key_adversaire):
    dic_coup={"PIERRE":88275625857605,"FEUILLE":19779480974019653,"CISEAUX":18939445432636760}
    dic_coup2={88275625857605:"PIERRE",19779480974019653: "FEUILLE", 18939445432636760:"CISEAUX"}

    #xgcd(dic_coup["PIERRE"],dic_coup["CISEAUX"]) ne sont pas premiers entre eux!!
    #(5, 1452445245935753, -6769760686231)
    temp=json.loads(get_stp("/bin/banks/assistant/round",K))
    if(len(temp.keys())==2):
        a_adversaire=temp["a"]
        b_adversaire=temp["b"]
        waiting = False
    else:
        print(temp["status"])
        waiting = True
    temp=random.randint(1,3)
    if(temp==1):
        coup = "PIERRE"
    elif(temp==2):
        coup = "CISEAUX"
    elif(temp==3):
        coup = "FEUILLE"
    #coup = "FEUILLE" #Match nul h24 avec CISEAUX
    print(coup)
    y  = randrange(3,20000)%p
    a = pow(g,y,p)                          # a= g^y
    b = (dic_coup[coup]*pow(h,y,p))%p           # b= coup * h^y avec h la clef que j'ai postéen
    #b//=5                                    # On divise par 5 car pgcPIERRE CISEAUX  =5
    # Quand je joue CISEAUX il crois que je joue FEUILLE, quand je joue FEUILLE il le sait pareil pour PAPIER
    if(waiting):
        try:
            res=json.loads(post_stp("/bin/banks/assistant/move",{'a':a,'b': b},K))
        except Exception  as e:
            print(post_stp("/bin/banks/assistant/move",{'a':a,'b': b},K))
        a_adversaire=res["a"]
        b_adversaire=res["b"]
        waiting = False
    else:
        res=(post_stp("/bin/banks/assistant/move",{'a':a,'b': b},K))
    try:
        temp=json.loads(post_stp("/bin/banks/assistant/outcome",{'move':coup,'y':y},K))
    except Exception  as e:
        print((post_stp("/bin/banks/assistant/outcome",{'move':coup,'y':y},K)))
    print(temp)
    print(temp["referee_says"])
    y=temp["y"]
    coup_jouer_adv=temp["move"]
    if(pow(key_adversaire['g'],y,key_adversaire['p'])!=a_adversaire):
        #pass
        print(post_stp("/bin/banks/referee","",K))
    else:
        coup_adv=decrypt_elgamal(key_adversaire["h"],y,key_adversaire["p"],a_adversaire,b_adversaire)
        if(coup_adv!=dic_coup[coup_jouer_adv]):
            print(post_stp("/bin/banks/referee","",K))
        else:
            pass
            #print("coup adversaire : ", dic_coup2[coup_adv])
            #print(coup_adv)
    fin_du_jeu = temp['referee_says']['match_result']

    if(fin_du_jeu != "GAME OVER --- Vous avez perdu"):
        return 0
    else:
        return 1

"""
clef,g1,h1,p1= debut_match(K)
for i in range(0,2000):
    bool=round(K,g1,p1,h1,clef)
    if(bool == 1):
        break

print(get_stp("/bin/banks",K))
print(get_stp("/bin/police_hq",K))
"""
