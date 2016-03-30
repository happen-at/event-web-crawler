# -*- coding: utf-8 -*-

#import feedparser
#d = feedparser.parse('http://dai-heidelberg.de/de/veranstaltungen/feed/')
#print d['feed']['title']

import codecs
import simplejson
import requests
from bs4 import BeautifulSoup

page = requests.get("http://dai-heidelberg.de/de/veranstaltungen/?event-date=&event-category=0&event-type=0")
html = page.text

soup = BeautifulSoup(html, "html.parser")

options = soup.find(id="event-type").findAll("option")

categories = []
for option in options:
    info = {}
    info['id'] = option.attrs['value']
    info['label'] = option.text
    info['articles'] = []
    categories.append(info)

by_cat = {}

for category in categories[:1]:
    page = requests.get("http://dai-heidelberg.de/de/veranstaltungen/?event-date=&event-category=0&event-type=%s" % category['id'])
    html = page.text
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.findAll("article")
    for article in articles[:1]:
        content = article.findAll("a", { "class" : "event-list__content" })
        info = {}
        info['url'] = content[0].attrs['href']
        category['articles'].append(info)

for category in categories:
    for info in category['articles']:
        page = requests.get(info['url'])
        html = page.text
        soup = BeautifulSoup(html, "html.parser")
        article = soup.findAll("article")[0]
        info['title'] = article.findAll("h1", {"class": "main__title"})[0].text.strip()
        info['time'] = article.findAll("time")[0].text.strip()
        info['text'] = article.findAll("div", {"class": "event-single__text"})[0].text.strip()


json = simplejson.dumps(categories,
                        ensure_ascii=False,
                        indent=True,
                        sort_keys=True)
file_handler = codecs.open('dai.json', 'w', 'utf-8')
file_handler.write(json)
file_handler.close()

"""
<article id="post-12823" class="post-12823 dai_event type-dai_event status-publish has-post-thumbnail hentry event-single">
    <header class="event-single__header">
        <h1 class="main__title">Info Session – Nach dem Abi ins Ausland</h1>
    </header>

    <div class="event-single__content event-single__content-thumbnail">
            <div class="event-single__thumbnail">
            <img width="700" height="312" src="http://dai-heidelberg.de/de/wp-content/uploads/sites/2/2014/03/Study-USA.jpg" class="attachment-dai-singular wp-post-image" alt="Study-USA">        </div>
            <ul class="event-single__info">
            <li class="event-single__info__item">
                            </li>
            <li class="event-single__info__item">
                <time datetime="2015-12-15T15:16:25+00:00">
                    Mo, 14. März 2016, 18:00 Uhr                </time>
            </li>
            <li class="event-single__info__item">
                            Information                        </li>
            <li class="event-single__info__item">
                            </li>
                </ul>
        <div class="event-single__text">
            <p>Das Abi ist geschafft und nach zwölf Jahren Schule willst du endlich die Welt sehen, neue Leute kennen lernen, deinen Horizont erweitern oder einfach mal was Neues ausprobieren?<br>
Ein Jahr zur Orientierung ins Ausland? Aber was? Ob Freiwilligendienst, Au pair oder Work and Travel, wir zeigen die Bedingungen und Möglichkeiten auf und helfen dir herauszufinden, was für dich das Richtige ist. Es werden Ehemalige anwesend sein, die ihre Erfahrungen und Eindrücke aus der Zeit im Ausland schildern.</p>
                    </div>
                    Der Eintritt ist <strong>frei</strong>.        </div>
</article>

<article id="post-12823" class="post-12823 dai_event type-dai_event status-publish has-post-thumbnail hentry event-list">
    <div class="event-list__container" title="Permanenter Link zu Info Session – Nach dem Abi ins Ausland">
        <div class="event-list__thumbnail">
            <a href="http://dai-heidelberg.de/de/veranstaltungen/info-session-nach-dem-abi-ins-ausland-2-12823/">
                            <img width="140" height="140" src="http://dai-heidelberg.de/de/wp-content/uploads/sites/2/2014/03/Study-USA-140x140.jpg" class="attachment-dai-list wp-post-image" alt="Study-USA" data-pin-nopin="true">                        </a>
        </div>

        <a class="event-list__content" href="http://dai-heidelberg.de/de/veranstaltungen/info-session-nach-dem-abi-ins-ausland-2-12823/" title="Permanenter Link zu Info Session – Nach dem Abi ins Ausland" rel="bookmark">
            <header class="event-list__header">
                <h2 class="event-list__title">Info Session – Nach dem Abi ins Ausland</h2>
                            </header>

            <div class="event-list__excerpt">
                Das Abi ist geschafft und nach zwölf Jahren Schule willst du endlich die Welt sehen, neue Leute kennen lernen, deinen&nbsp;…
 →
            </div>
        </a>

        <div class="event-list__info">
            <div class="event-list__meta">
                <time class="event-list__date" datetime="2015-12-15T15:16:25+00:00">
                    Mo, 14. März 2016<br> 18:00 Uhr                </time>

                <p class="event-list__categories">Bibliothek, U20</p>
            </div>

                        </div>

    </div>
</article>

<article id="post-12823" class="post-12823 dai_event type-dai_event status-publish has-post-thumbnail hentry event-single">
    <header class="event-single__header">
        <h1 class="main__title">Info Session – Nach dem Abi ins Ausland</h1>
    </header>

    <div class="event-single__content event-single__content-thumbnail">
            <div class="event-single__thumbnail">
            <img width="700" height="312" src="http://dai-heidelberg.de/de/wp-content/uploads/sites/2/2014/03/Study-USA.jpg" class="attachment-dai-singular wp-post-image" alt="Study-USA">        </div>
            <ul class="event-single__info">
            <li class="event-single__info__item">
                            </li>
            <li class="event-single__info__item">
                <time datetime="2015-12-15T15:16:25+00:00">
                    Mo, 14. März 2016, 18:00 Uhr                </time>
            </li>
            <li class="event-single__info__item">
                            Information                        </li>
            <li class="event-single__info__item">
                            </li>
                </ul>
        <div class="event-single__text">
            <p>Das Abi ist geschafft und nach zwölf Jahren Schule willst du endlich die Welt sehen, neue Leute kennen lernen, deinen Horizont erweitern oder einfach mal was Neues ausprobieren?<br>
Ein Jahr zur Orientierung ins Ausland? Aber was? Ob Freiwilligendienst, Au pair oder Work and Travel, wir zeigen die Bedingungen und Möglichkeiten auf und helfen dir herauszufinden, was für dich das Richtige ist. Es werden Ehemalige anwesend sein, die ihre Erfahrungen und Eindrücke aus der Zeit im Ausland schildern.</p>
                    </div>
                    Der Eintritt ist <strong>frei</strong>.        </div>
</article>

<article id="post-12735" class="post-12735 dai_event type-dai_event status-publish has-post-thumbnail hentry event-single">
    <header class="event-single__header">
        <h1 class="main__title">Richard Dawkins ENTFÄLLT!</h1>
    </header>

    <div class="event-single__content event-single__content-thumbnail">
            <div class="event-single__thumbnail">
            <img width="700" height="312" src="http://dai-heidelberg.de/de/wp-content/uploads/sites/2/2015/12/160315_RichardDawkins_c_LallaWard.jpg" class="attachment-dai-singular wp-post-image" alt="160315_RichardDawkins_c_LallaWard">        </div>
            <ul class="event-single__info">
            <li class="event-single__info__item">
                Die Poesie der Naturwissenschaften            </li>
            <li class="event-single__info__item">
                <time datetime="2015-12-10T16:14:06+00:00">
                    Di, 15. März 2016, 20:00 Uhr                </time>
            </li>
            <li class="event-single__info__item">
                            Autobiographie                        </li>
            <li class="event-single__info__item">
                Aula der Neuen Universität            </li>
                    <li class="event-single__info__item">
                Im Dialog            </li>
                </ul>
        <div class="event-single__text">
            <p>Die Veranstaltung muss leider aus gesundheitlichen Gründen entfallen.</p>
<p>Bereits gekaufte Karten können an der jeweiligen Vorverkaufsstelle zurückgegeben werden.</p>
                    </div>
                <p class="event-single__ticket-link">
            <a class="btn-cart" href="https://shop.reservix.de/off/login_check.php?id=36ae96de8dddc4df70dce3f39db2b886ff117b9261533f02fa35ea4a3191d65e3a64633f4652f2d1ba3a365eff82ca70&amp;vID=2736&amp;eventGrpID=183672&amp;eventID=771990" target="_blank">Tickets kaufen</a>
        </p>
                                <div class="event-single__ticket-prices">
            <h2 class="main__subtitle event-single__ticket-prices__headline">Preise</h2>

                        <div class="event-single__ticket-prices__table">
                <table>
                    <caption>VVK (zzgl. Gebühren)</caption>
                                        <tbody><tr>
                        <th>Normal</th>
                        <td>12 €</td>
                    </tr>
                                        <tr>
                        <th>Ermäßigt</th>
                        <td>10 €</td>
                    </tr>
                                        <tr>
                        <th>Mitglieder</th>
                        <td>8 €</td>
                    </tr>
                                    </tbody></table>
            </div>
                        <div class="event-single__ticket-prices__table">
                <table>
                    <caption>Abendkasse</caption>
                                        <tbody><tr>
                        <th>Normal</th>
                        <td>14 €</td>
                    </tr>
                                        <tr>
                        <th>Ermäßigt</th>
                        <td>12 €</td>
                    </tr>
                                        <tr>
                        <th>Mitglieder</th>
                        <td>10 €</td>
                    </tr>
                                    </tbody></table>
            </div>
                    </div>
                </div>
</article>
"""



"""
http://dai-heidelberg.de/de/veranstaltungen/?event-date=&event-category=0&event-type=0
http://dai-heidelberg.de/de/veranstaltungen/page/2/?event-date&event-category=0&event-type=0
http://dai-heidelberg.de/de/veranstaltungen/page/3/?event-date&event-category=0&event-type=0
http://dai-heidelberg.de/de/veranstaltungen/page/4/?event-date&event-category=0&event-type=0
http://dai-heidelberg.de/de/veranstaltungen/page/5/?event-date&event-category=0&event-type=0
"""
