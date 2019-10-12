import requests

headers = {
    'authority': 's.1688.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,_/_;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'none',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'cna=zqu8FGo3tQACAWVEROown73f; ali_apache_id=11.27.146.52.154986650175.410353.8; ali_ab=101.68.68.234.1551952961093.8; lid=sp%E4%B9%88%E4%B9%88%E5%93%92214; ali_apache_track=c_mid=b2b-30255702317c68f|c_lid=sp%E4%B9%88%E4%B9%88%E5%93%92214|c_ms=1; cookie2=146f7a6922bccf66535d3e78f9fd815d; hng=CN%7Czh-CN%7CCNY%7C156; t=11cff45c72004287dbc7d7f445b6ddd2; _tb_token_=f4eadb18605be; **cn_logon**=false; h_keys="%u6c7d%u8f66#%u5c0f%u7c73"; alisw=swIs1200%3D1%7C; alicnweb=homeIdttS%3D92877635209548718074379840853382764800%7Ctouch_tb_at%3D1568099210736%7ChomeIdttSAction%3Dtrue%7Clastlogonid%3Dsp%25E4%25B9%2588%25E4%25B9%2588%25E5%2593%2592214; ad_prefer="2019/09/10 15:11:47"; isg=BHl5Eq2TAB-L7N2dHojcged7iOVZTmN4WMQuApuu8aAfIpm049fBCNlwoGZxoQVw; l=cBNTeJrqvoue-lN2XOCaourza779IIRYjuPzaNbMi_5ha68_HRbOkz0g6FJ6cjWdOgLB4rRpHn99-etkql5PvK9PJA6P.',
}

params = (
    ('keywords', '\uFFFD\uFFFD\uFFFD\uFFFD'),
    ('n', 'y'),
    ('netType', '1,11'),
    ('spm', 'a260k.dacugeneral/new.search.0'),
)

response = requests.get('https://s.1688.com/company/company_search.htm', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://s.1688.com/company/company_search.htm?keywords=%C6%FB%B3%B5&n=y&netType=1%2C11&spm=a260k.dacugeneral%2Fnew.search.0', headers=headers)
