# projekto kelimas i serveri
# https://www.hostinger.com/ vienas lengviausių dalykų (pigu, nemokamas domenas ir gera pradedantiesiems)
# https://www.gandi.net/en-US domenai vien
# https://pages.github.com/ paleisti per githubą automatiškai statinę (be duomenų bazės) svetainę
# https://www.linode.com/lp/free-credit-short/?promo=sitelin100-02162023&promo_value=100&promo_length=60&locationid=9062292&device=c_c


# from uuid import uuid4
# s = str(uuid4()).split('-')
# q = s[4]
# print(s)
# print(q)

# user = models.Foregnkey(User, on_delete..., related_name=profile)
# u = User.objects.get(id=1)

from datetime import date, timedelta
reiksme = '30d'
reiksme_pakeista = reiksme.replace('d', '')
reiksme_int = int(reiksme_pakeista)
terminas = date.today() + timedelta(days=reiksme_int)

print(terminas)