import hashlib

class sha:

    def get512(text, __SETTINGS__ = "-none"):

        TIMES__ = 512

        if __SETTINGS__ == "-none":
            pass
        if "-intext" in __SETTINGS__:
            print("Starting Hash")
        if "-EXTRA" in __SETTINGS__:
            TIMES__ = TIMES__ * TIMES__
        if "-EXTRAPLUS" in __SETTINGS__:
            TIMES__ += int(TIMES__ + (256 + ((TIMES__ / 4) - 32)))
        if "-HARD" in __SETTINGS__:
            text = hashlib.sha256( text.encode('utf-8') ).hexdigest()

        if "-status" in __SETTINGS__:
            for i in range(TIMES__):
                text = hashlib.sha512( text.encode('utf-8') ).hexdigest()
                print(" STATUS: " + str(text))
        else:
            for i in range(TIMES__):
                text = hashlib.sha512( text.encode('utf-8') ).hexdigest()

        if "-BIG" in __SETTINGS__:
            if "-status" in __SETTINGS__:
                for i in range(int(5)):
                    text += hashlib.sha512( text.encode('utf-8') ).hexdigest()
                    print(" STATUS: " + str(text))
            else:
                for i in range(int(5)):
                    text += hashlib.sha512( text.encode('utf-8') ).hexdigest()
        if "-BIGPLUS" in __SETTINGS__:
            if "-status" in __SETTINGS__:
                for i in range(int(5)):
                    text += hashlib.sha512( text.encode('utf-8') ).hexdigest() + str(TIMES__ + i ^ i) + str(text)
                    print(" STATUS: " + str(text))
            else:
                for i in range(int(5)):
                    text += hashlib.sha512( text.encode('utf-8') ).hexdigest() + str(TIMES__ + i ^ i) + str(text)
        if "-intext" in __SETTINGS__:
            print("Finished!")
        return str(text)
def genGoodPass(text):
    if (len(text) < 64):
        hashed = ehashClass.get512(text, "-EXTRA -EXTRAPLUS -HARD")
    else:
        hashed = ehashClass.get512(ehashClass.get512(text, "-EXTRA -EXTRAPLUS -BIG"), "-EXTRA -EXTRAPLUS -HARD")
    return str(hashed)
