from django.shortcuts import render
import rsa

def second(request):
    if request.method == "POST":
        if len(request.POST.get('message', '')) > 0:
            key_pub, key_priv = keys()
            return render(request, 'second.html', {'start': crypto(request.POST['message'].encode('utf8'), key_pub), 'key': key_pub, 'key2': key_priv})
        
        if len(request.POST.get('message2', '')) > 0:
            return render(request, 'second.html', {'encr': decrypto(request.POST['message2'], request.POST['key4']).decode('utf8')}) 
    else:
        return render(request, 'second.html', {'start': {}})

def keys():
    (pubkey, privkey) = rsa.newkeys(512)
    return pubkey, privkey

def crypto(message, key_public):
    return(rsa.encrypt(message, key_public))

def decrypto(crypto, key_private):
    return rsa.decrypt(crypto, key_private) 