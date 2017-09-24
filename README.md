# TaskCV project:

This program takes in pdf as input and converts it to raw data,scrape articles from Hackernews and displays relevant links to them based on the keywords searched

# Pre-Requisites:

1.Python installed with these libraries
    a.bs4
    b.nltk
    c.pdfminer

# Run the program:

You need to convert the pdf to raw data by typing the command "pdf2txt.py -o filename.txt -t tag <pdfname.pdf>". In order to run the program you'll need to type
"python taskCV.py"

# Input: 
CV (pdf)
# Output: 
Relevant content URLs of scraped articles from Hackernews.

# Test Results:
I have tested the above program in linux operating system and have recieved positive results.

# Successful Test:

keyword: action
# output:
https://news.ycombinator.com
news
newest
newcomments
show
ask
jobs
submit
login?goto=news
vote?id=15321015&how=up&goto=news
https://blog.plan99.net/its-time-to-kill-the-web-974a9fe80c89
from?site=plan99.net
user?id=raindev
item?id=15321015
hide?id=15321015&goto=news
item?id=15321015
vote?id=15321850&how=up&goto=news
http://karl-voit.at/2017/09/23/orgmode-as-markup-only/
from?site=karl-voit.at
user?id=pmoriarty
item?id=15321850
hide?id=15321850&goto=news
item?id=15321850
vote?id=15323042&how=up&goto=news
https://blog.scalents.com/2017/09/22/basic-category-theory-for-scala-programmers-part-i/
from?site=scalents.com
user?id=adamnemecek
item?id=15323042
hide?id=15323042&goto=news
item?id=15323042
vote?id=15302730&how=up&goto=news
https://medium.com/bbc-design-engineering/how-we-grow-junior-developers-at-the-bbc-dc3054f7e390
from?site=medium.com
user?id=chaghalibaghali
item?id=15302730
hide?id=15302730&goto=news
item?id=15302730
vote?id=15321070&how=up&goto=news
http://etherrag.blogspot.com/2013/07/duck-duck-go-illusion-of-privacy.html
from?site=etherrag.blogspot.com
user?id=awaisraad
item?id=15321070
hide?id=15321070&goto=news
item?id=15321070
vote?id=15320936&how=up&goto=news
https://www.neh.gov/about/awards/jefferson-lecture/martha-nussbaum-jefferson-lecture
from?site=neh.gov
user?id=drjohnson
item?id=15320936
hide?id=15320936&goto=news
item?id=15320936
vote?id=15321555&how=up&goto=news
https://thingsonreddit.com/
from?site=thingsonreddit.com
user?id=brudolph
item?id=15321555
hide?id=15321555&goto=news
item?id=15321555
vote?id=15302500&how=up&goto=news
http://jrruethe.github.io/blog/2015/04/23/bitcoin-paper-wallets/
from?site=jrruethe.github.io
user?id=j_s
item?id=15302500
hide?id=15302500&goto=news
item?id=15302500
vote?id=15302484&how=up&goto=news
https://kotaku.com/the-notorious-board-game-that-takes-1500-hours-to-compl-1818510912
from?site=kotaku.com
user?id=danso
item?id=15302484
hide?id=15302484&goto=news
item?id=15302484
vote?id=15302841&how=up&goto=news
https://medium.com/@mhluongo/zero-knowledge-proofs-zcash-and-ethereum-f6d89fa7cba8
from?site=medium.com
user?id=mhluongo
item?id=15302841
hide?id=15302841&goto=news
item?id=15302841
vote?id=15322805&how=up&goto=news
http://www.bbc.com/capital/story/20170919-the-power-of-a-not-to-do-list
from?site=bbc.com
user?id=jv22222
item?id=15322805
hide?id=15322805&goto=news
item?id=15322805
vote?id=15322447&how=up&goto=news
http://nautil.us/issue/52/the-hive/is-tribalism-a-natural-malfunction
from?site=nautil.us
user?id=dnetesn
item?id=15322447
hide?id=15322447&goto=news
item?id=15322447
vote?id=15320922&how=up&goto=news
https://medium.com/conversations-with-tyler/tyler-cowen-larry-summers-blog-secular-stagnation-twitter-421a69ed84c8
from?site=medium.com
user?id=objections
item?id=15320922
hide?id=15320922&goto=news
item?id=15320922
vote?id=15318440&how=up&goto=news
https://www.michalspacek.com/post-a-boarding-pass-on-facebook-get-your-account-stolen
from?site=michalspacek.com
user?id=flux_w42
item?id=15318440
hide?id=15318440&goto=news
item?id=15318440
vote?id=15320489&how=up&goto=news
http://pleasingfungus.com/Silicon%20Zeroes/?
from?site=pleasingfungus.com
user?id=jonnybgood
item?id=15320489
hide?id=15320489&goto=news
item?id=15320489
vote?id=15321588&how=up&goto=news
https://www.nytimes.com/2017/09/23/business/equifax-data-breach.html
from?site=nytimes.com
user?id=tim_sw
item?id=15321588
hide?id=15321588&goto=news
item?id=15321588
vote?id=15320778&how=up&goto=news
https://www.peterkrautzberger.org/0186/
from?site=peterkrautzberger.org
user?id=auggierose
item?id=15320778
hide?id=15320778&goto=news
item?id=15320778
vote?id=15321807&how=up&goto=news
https://www.recode.net/2017/9/23/13153814/casper-sleepopolis-lawsuits-mattress-reviews
from?site=recode.net
user?id=jsm386
item?id=15321807
hide?id=15321807&goto=news
item?id=15321807
vote?id=15314006&how=up&goto=news
http://www.bbc.com/news/health-41351159
from?site=bbc.com
user?id=hexrcs
item?id=15314006
hide?id=15314006&goto=news
item?id=15314006
vote?id=15320952&how=up&goto=news
http://kennethfriedman.org/thoughts/2016/then-and-now/
from?site=kennethfriedman.org
user?id=kennethfriedman
item?id=15320952
hide?id=15320952&goto=news
item?id=15320952
vote?id=15322627&how=up&goto=news
http://www.arnoldkling.com/blog/did-the-suits-win-the-internet/
from?site=arnoldkling.com
user?id=scarhill
item?id=15322627
hide?id=15322627&goto=news
item?id=15322627
vote?id=15316175&how=up&goto=news
https://code.facebook.com/posts/300798627056246
from?site=facebook.com
user?id=dwwoelfel
item?id=15316175
hide?id=15316175&goto=news
item?id=15316175
vote?id=15318530&how=up&goto=news
https://github.com/sgoedecke/socket-io-game/blob/master/BLOG.md
from?site=github.com
user?id=gfysfm
item?id=15318530
hide?id=15318530&goto=news
item?id=15318530
vote?id=15320616&how=up&goto=news
https://www.nytimes.com/2017/09/20/business/economy/startup-business.html
from?site=nytimes.com
user?id=lkrubner
item?id=15320616
hide?id=15320616&goto=news
item?id=15320616
vote?id=15322156&how=up&goto=news
https://www.nytimes.com/2017/09/23/opinion/sunday/facebook-ad-scandal.html
from?site=nytimes.com
user?id=stablemap
item?id=15322156
hide?id=15322156&goto=news
item?id=15322156
vote?id=15315129&how=up&goto=news
https://www.nytimes.com/2017/09/22/opinion/sunday/portugal-drug-decriminalization.html
from?site=nytimes.com
user?id=fanf2
item?id=15315129
hide?id=15315129&goto=news
item?id=15315129
vote?id=15318904&how=up&goto=news
http://www.pixelbeat.org/docs/unix-parallel-tools.html
from?site=pixelbeat.org
user?id=kiyanwang
item?id=15318904
hide?id=15318904&goto=news
item?id=15318904
vote?id=15302701&how=up&goto=news
http://www.denverpost.com/2017/09/20/mutant-butterflies-genetics/
from?site=denverpost.com
user?id=yawz
item?id=15302701
hide?id=15302701&goto=news
item?id=15302701
https://jobs.lever.co/hellosign?lever-origin=applied&lever-source%5B%5D=HackerNews
from?site=lever.co
item?id=15322890
hide?id=15322890&goto=news
vote?id=15302636&how=up&goto=news
http://www.bbc.co.uk/news/technology-41346717
from?site=bbc.co.uk
user?id=tooba
item?id=15302636
hide?id=15302636&goto=news
item?id=15302636
news?p=2
https://www.ycombinator.com/apply/
newsguidelines.html
newsfaq.html
mailto:hn@ycombinator.com
https://github.com/HackerNews/API
security.html
lists
bookmarklet.html
dmca.html
http://www.ycombinator.com/apply/
mailto:hn@ycombinator.com
