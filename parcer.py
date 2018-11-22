from requests_html import HTMLSession
import fille 
def get_url():
    ses=HTMLSession()
    r = ses.get('https://s11028.edu35.ru/2013-06-12-15-17-31/raspisanie')
    i=0
    m=len(r.html.find('.at_url'))
    hg = []
    while i<m:
        g=1
        f=r.html.find('.at_icon')[i].attrs
        f=f.get('href')
        print(f)
        listhor=['1 смена','1_смена','1смена','1 СМЕНА']
        for j in listhor:
            result=f.find(j)
#        fh=f.find('224/')
#        day_real=fille.get_real_date()
#        day=int(f[fh+4:fh+6])
#        if result!=-1 and day_real==day:
        if result!=-1: 
            hg.append(f)

        i=i+1
    month=fille.get_month()
    try:
        uk=hg[-1]
    except IndexError:
        return(0,0)
    kh=uk.find(month)
    if kh == -1:
        month=month.upper()
        kh=uk.find(month)
    fh=uk.find('224/')
    cast = uk[fh+4:kh+len(month)]
    return(hg[-1],cast)

