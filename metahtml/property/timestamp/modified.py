from metahtml.property.timestamp.__common__ import TimestampExtractor

class Extractor(TimestampExtractor):
    jsonpaths = [
        ( 'en.antaranews.com', '$.disabled' ),

        ( None, '$.dateModified'),
        ( None, '$."@graph"[*].dateModified'),
        ]

    xpaths = [
        # xpaths
        ( 'airsafe.com',                    '//div[@class="blocked_off"]/text()'),
        ( 'alexandrina.eco-compliance.de',  '//a[@class="last-modified"]/text()'),
        ( 'arabic.rt.com',                  '(//time)[3]'),
        ( 'artgnews.com',                   '(//div[@class="info_area"]/span[@class="date"]/span)[2]' ),
        ( 'asiae.co.kr',                    '(//div[@class="articleInfo"]/div/em)[2]'),
        ( 'bangkokpost.com',                '//div[@class="article-info"]/div[@class="row"]/div[1]/p[2]'),
        ( 'buzzfeednews.com',               '//p[@class="news-article-header__timestamps-updated"]'),
        ( 'consilium.europa.eu',            '//div[@class="time-wrapper"]/time/@datetime'),
        ( 'cronicaglobal.elespanol.com',    '(//div[@class="news_ext_date"]/time)[2]'),
        ( 'datarepository.wolframcloud.com', '(//ul[@class="source-metadata"]/li/span[@class="property"])[2]'),
        ( 'deagel.com',                     '//div[@id="date"]/text()'),
        ( 'donga.com',                      '(//span[@class="date01"])[2]' ),
        ( 'europe1.fr',                     '(//span[@class="publication"]/time/@datetime)[2]'),
        ( 'europe1.fr',                     '(//span[@class="publication"]/time/@datetime)[2]'),
        ( 'foxnews.com',                    '//div[@class="article-updated"]' ),
        ( 'foxnews.com',                    '//div[@class="article-updated"]' ),
        ( 'globalecho.org',                 '//meta[@name="shareaholic:article_modified_time"]/@content'),
        ( 'globalsecurity.org',             '//div[@id="modified"]' ),
        ( 'icanswitzerland.ch',             '//time[@class="updated"]/@datetime'),
        ( 'infox.ru',                       '//meta[@itemprop="dateModified"]/@content'),
        ( 'islamsounnah.com',               '//meta[@property="article:modified_time"]/@content'),
        ( 'lessentiel.lu',                  '//div[@class="published clearfix"]/p/span'),
        ( 'lindependant.fr',                '//span[@class="article-detail-infos-modified"]/time/@content'),
        ( 'minwonnews.com',                 '(//div[@class="info_area"]/span[@class="date"]/span)[2]' ),
        ( 'newindianexpress.com',           '(//p[@class="ArticlePublish margin-bottom-10"]/span)[2]'),
        ( 'news.asiantown.net',             '//div[@id="b_by"]/@data-t' ),
        ( 'niconews55.com',                 '//time[@class="date gf entry-date undo updated"]/@datetime'),
        ( 'ottawacitizen.com',              '//span[@class="updated-date__since"]/@date-last-update' ),
        ( 'politico.com',                   '//p[@class="story-meta__updated"]/time/@datetime'),
        ( 'politico.com',                   '//span[@class="updated"]'),
        ( 'renegadetribune.com',            '//span[@class="posted-on"]//time[@class="updated"]/@datetime' ),
        ( 'saymar.org',                     '//span[@class="updated"]'),
        ( 'senenews.com',                   '//span[@class="date updated"]' ),
        ( 'senenews.com',                   '//span[@class="timeT"]'),
        ( 'service-public.fr',              '(//p[@class="date"]/text())[1]'),
        ( 'sohfrance.org',                  '//meta[@property="article:modified_time"]/@content' ),
        ( 'sternchen4you.de',               '//time[@class="updated"]/@datetime'),
        ( 'topia.ne.jp',                    '//p[@class="updatedAt"]/text()'),
        ( 'tvanouvelles.ca',                '//p[@class="date-line"]/time/@datetime'),
        ( 'tvanouvelles.ca',                '//time[@itemprop="dateUpdated"]/@datetime' ),
        ( 'unis.unvienna.org',              '//meta[@name="posting-date"]/@content'),
        ( 'upi.com',                        '//div[@class="article-date"]/span'),
        ( 'varlamov.ru',                    '//span[@class="j-e-date"]/time[@itemprop="dateModified"]'),
        ( 'vias.org',                       '//td[@align="right"]/text()'),
        ( 'vie-publique.fr',                '//div[@class="dateBox"]/p/time/@datetime'),
        ( 'wiki.arcs.com',                  '//li[@id="lastmod"]/text()'),
        ( 'wiki.islamiccounterterrorism.org', '//li[@id="lastmod"]/text()'),
        ( 'world-nuclear.org',              '(//em/text())[1]'),
        ( 'worldometers.info',              '//div[@style="font-size:13px; color:#999; text-align:center"]/text()'),
        ( 'youthdaily.co.kr',               '(//ul[@class="art_info"]/li/text())[2]'),
        
        # meta xpaths
        ( None, '//meta[@*="DCTERMS.modified"]/@content'),
        ( None, '//meta[@*="Date-Revision-yyyymmdd"]/@content'),
        ( None, '//meta[@*="article.updated"]/@content'),
        ( None, '//meta[@*="article:modified"]/@content' ),
        ( None, '//meta[@*="article:modified_time"]/@content' ),
        ( None, '//meta[@*="article:post_modified"]/@content' ),
        ( None, '//meta[@*="dcterms.modified"]/@content'),
        ( None, '//meta[@*="dd:modified_time"]/@content' ),
        ( None, '//meta[@*="last_updated_date"]/@content' ),
        ( None, '//meta[@*="lastmod"]/@content' ),
        ( None, '//meta[@*="modified-date"]/@content' ),
        ( None, '//meta[@*="og:article:modified_time"]/@content' ),
        ( None, '//meta[@*="og:modified_time"]/@content' ),
        ( None, '//meta[@*="og:updated_time"]/@content' ),
        ( None, '//meta[@*="revised"]/@content'),
        ( None, '//meta[@*="rnews:dateModified"]/@content' ),

        # microdata paths
        ( None, '//*[@*="dateModified"]/@content' ),
        ( None, '//*[@*="dateModified"]/@datetime' ),
        ( None, '//*[@*="dateModified"]' ),

        ]

