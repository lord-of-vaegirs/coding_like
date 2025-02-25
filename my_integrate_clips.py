import os

lt=[]

with open('deadpoem.m3u8',mode='r',encoding='utf-8') as f:
    for line in f:
        if line.startswith('#'):
            continue
        else:
            line=line.strip()
            lt.append('/Users/lxjarctane2/Documents/pythonide/'+'deadpoem_doc'+line.split('/')[-1])

s=" ".join(lt)
os.system(f"cat {s} > deadpoem_movie.mp4")


# /Users/lxjarctane2/Documents/pythonide/deadpoem_doccc8e34d5c88000000.ts



