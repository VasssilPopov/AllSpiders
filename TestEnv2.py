from sys import exit, path
from datetime import date, timedelta
import platform

if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

from ScrapingHelpers import *
from HelperTools import *
from Dates import *
from Duplicates import *
from Monthly_Report import *
from urllib2 import quote


# Monthly Reports of collected data (Start)------------------------------------
# during a year and month
# output reports will be text files
# into _MonthlyReports subdirectory of root directory
# file name will be MonthlyReport-YYYY-mm.txt
# example MonthlyReport-2017-05.txt
# report of collected data during 2017 year and
# month of May

# example input parameters
# Report Year 2017 and report month (August)
repYear='2017'
repMonth=9

# single month report
##monthlyDataReport(repYear, repMonth)

## range of months report
## create separate text file reports
## from May to September
#!!!! uncomment next lines to have a report
# for m in range(5,10):
#     monthlyDataReport(repYear, m)
# Monthly Reports of collected data (End)------------------------------------
'''
import time
startTime=time.time()

for i in range(0,3):
        time.sleep(1)

endTime=time.time()

print '%s Duration: %f' % (time.localtime(startTime),(endTime - startTime))

s='Шĸcтимo зoгинoxo пpи нoвeднĸния, пpичинĸни eт лeшeтe вpĸмĸ в Итoлия'

import string
#a='cemvhny'
#b='1234567'
a=u'ко'
b=u'еа'
x=string.maketrans(a,b)
#s='The cow jumped over the moon'
s=u'Шĸcтимo зoгинoxo пpи нoвeднĸния'

print a,b
print
print s
print s.translate(x)
'''
import string 
print 'new'
def trans(to_translate):
    tabin  = u'ĸoeCΠPBEXHMTAKa'       #привет'
    tabout = u'еаоТРСНКПВАXEMк'      #тевирп'
    tabin = [ord(char) for char in tabin]
    translate_table = dict(zip(tabin, tabout))
    return to_translate.translate(translate_table)
newline= u''
s=u'Шĸcтимo дyши co зoгинoли, o тpимo cĸ вeдят бĸзcлĸднe изчĸзнoли в Ливepнe, eблocт Cecaoнo зopoди нoвeднĸния днĸc, cъeбщoвo Πeйтĸpc aoтe cĸ пeзeвoвo нo coйтo нo в."Eepиĸpĸ дĸлo cĸpo".'
s=s+newline+u'Pпepĸд oгĸнция Фpoнc пpĸc, aeятe цитиpo пeжopниaopи, жĸpтвитĸ нo eбилнитĸ вoлĸжи co нoд пĸт, aoтe чĸтиpи co cĸмĸйcтвe, eтapитe в нoвeднĸнoтo cи aъщo в Ливepнe, aъдĸтe cĸ ĸ изcипoл изaлючитĸлнe cилĸн дъжд зo чĸтиpи чoco тoзи нeщ, пpĸвpъщoйaи yлицитĸ в pĸaи и eтнocяйaи oвтeмeбили, цитиpo БCM.'
s=s+newline+u'"Eepиĸpĸ дĸлo cĸpo" yтeчни, чĸ cтoвo дyмo зo мeмичĸнцĸ, peдитĸлитĸ мy и дядeтe. Cялeтe нo дpyг чeвĸa ĸ билe eтapитe в зeнo нo cвлoчищo.'
s=s+newline+u'"Извънpĸднoтo cитyoция нĸ ĸ пpиaлючилo," пeceчвo мĸcтнoтo oдминиcтpoция в coйтo cи.'
s=s+newline+u'Eмĸтът нo Ливepнe Филипe Beгopин eпpĸдĸля cитyoциятo aoтe дpoмoтичнo, тpyднo и apитичнo.'
s=s+newline+u'Зo Флepĸнция ĸ eбявĸн epoнжĸв aeд, aoтe бypитĸ зoпeчнoли cнeщи eт Pĸвĸpнo Итoлия cĸ пpидвижвoт нo юг.'
s=s+newline+u'Xeдлĸзитĸ в Πим co зoтвepĸни aoтe пpĸдпoзнo мяpao.'
s=s+newline+u'Boциeнoлнoтo aeнфĸдĸpoция нo cĸлcaecтeпoнcaитĸ пpeизвeдитĸли Eeлдиpĸти (Таldіrоttі) aeмĸнтиpo, чĸ лeшeтe вpĸмĸ ĸ нocтъпилe вĸднoгo cлĸд cyшoтo, зopoди aeятe зĸмятo ĸ пe-cyxo eт eбиaнeвĸнe и нĸ мeжĸ дo пeĸмĸ дъждeвĸтĸ.'
s=s+newline+u'Hoлĸжитĸ в Cecaoнo co нoмoлĸли c 57 пpeцĸнтo тeвo лятe, eтбĸлязвo epгoнизoциятo, цитиpoнo eт Фpoнc пpĸc.'
s=s+newline+u'Cpeпиaoлизoциятo нo aлимoтo yвĸличoвo apoйнecтитĸ във вpĸмĸтe - гepĸщи вълни, cилни вoжĸли, тĸжaи гpoдyшaи, aeитe вpĸдят нo нoциeнoлнeтe cĸлcaecтeпoнcae пpeизвeдcтвe, пeceчвo Eeлдиpĸти.'
s=s+newline+u'Pпepĸд epгoнизoциятo пpĸз пecлĸднитĸ 10 гeдини щĸтитĸ възлизoт нo 14 милиopдo ĸвpe.'

'''
newline= u''
s=u'Bĸвиждoнo бypя cĸ poзpoзи eт 8.00 дe 10.00 ч. (9.00 - 11.00 ч. бългopcae вpĸмĸ) тoзи cyтpин нoд Зoдop, Pĸвĸpнo Дoлмoция в Tъpвoтcao, aoтe зo бpeĸни минyти нoвeдни вcичaи пeдлĸзи и пpĸвъpнo yлицитĸ нo тypиcтичĸcaия гpoд в cъщинcaи pĸaи, пpĸдoвoт xъpвoтcaитĸ мĸдии. Pпepĸд тĸлĸвизия N1 гpoдът ĸ в xoec, cпpян ĸ гpoдcaият тpoнcпepт и цĸнтpoлнитĸ мoгoзини co зoтвepĸни зopoди нoвeднĸниĸ, цитиpo \"Фeayc\".'
s=s+newline+u'Cĸлĸвизиятo cъeбщoвo, чĸ coмe зo двo чoco вoлĸжитĸ co нoдxвъpлили 190 л./aв.м., aoтe тeвo ĸ пpĸвишилe cpĸднoтo нepмo зo двo мĸcĸцo.'
s=s+newline+u'Aлĸaтpeннeтe издoниĸ Dnоvnа твъpди, чĸ гpoдът ĸ в aeлoпc, дeaoтe Іndох eзoглoвявo пyблиaoциятo cи \"Xeтeп в Зoдop\" и cъeбщoвo, чĸ мĸcтния цĸнтъp 112 ĸ зoтpyпoн c eбoждoния.'
s=s+newline+u'Гeлĸми чocти eт гpoдo co бĸз ĸлĸaтpичĸcтвe.'
s=s+newline+u'Xepeйни дъждeвĸ пpĸз изминoлoтo нeщ eбxвoнoxo и Бecнo и Tĸpцĸгeвинo и пpĸдизвиaoxo нoвeднĸния в жилищни и индycтpиoлни eбĸaти, aoaтe и cпиpoнĸ нo тpoнcпepтo в poйeнo нo гpoд Kecтop, cъeбщи KИM. Зopoди пepeйния дъжд и eбилнитĸ aeличĸcтвo вeдo нo пътищoтo eт тoзи cyтpин ĸ пpĸaъcнoтe движĸниĸтe в няaeлae пътни eтcĸчaи в eaeлнecтитĸ нo Kecтop, pĸгиcтpиpoни co и мнeгe cвлoчищo в poйeнo, cъeбщи БCM.'

'''
print trans(s)
