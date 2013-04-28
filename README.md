#Overview
**vino_mamba**:it is linked with Los Angel Lakers's Super Star ***Kobe Bryant***'s two nick names.<br />
OK, It's a web crawler! Building with [scrapy] and Google Custom Search API.
[scrapy]:http://doc.scrapy.org/en/latest/intro/overview.html
Giving several key words then it receives some available results via Google Search API. And making analysis with these searched results .At the end, showing you the most effective result.

## Usage

###must environment:<br />
> Python 2.7.2 <br />
> a available mysql server<br />
> Pycharm (optional)

**step one**  install [virtualenv] 

[virtualenv]:http://www.virtualenv.org/en/latest/ 

```
sudo pip install virtualenv
```

```
sudo mkdir ~/Documents/Python/Virtualenvs/v2.7.2
```

```
cd ~/Documents/Python/Virtualenvs/v2.7.2
```

```
sudo virtualenv vino_mamba
```

```
cd vino_mamba
```

```
sudo source bin/activate
```


**step two** install these libraries listed below:

* pymysql	: a library to access mysql
* scrappy	: a very simple and powerful crawler writed by python
* beautifulsoup4 : a nice html/xml parser 


**step three** use Google API (RESTful)

apply a google project in [google console] to get a API key

[google console]:https://developers.google.com/api-client-library/python/reference/supported_apis
create a app based on Google Custom Search at [here] to get a ID(**cx**). [must]

> It will request u fill the site or the domain that you want to search to create a custom search engine. If you just want to get the result from google, write google's domain name e.g.:www.google.com www.google.com/hk ...

[root domain]:https://zh.wikipedia.org/wiki/%E6%A0%B9%E5%9F%9F%E5%90%8D%E6%9C%8D%E5%8B%99%E5%99%A8
[here]:https://www.google.com/cse/manage/create


then quick start for google api via [their documents]

[their documents]:https://developers.google.com/api-client-library/python/start/get_started#auth

and the service I used is [Google custom-search] , you should be familiar with the document and it's [python-api].

[Google custom-search]:https://developers.google.com/custom-search/v1/using_rest
[python-api]:https://google-api-client-libraries.appspot.com/documentation/customsearch/v1/python/latest/

##Modules

###search

###model

###dao

###crawler

###analysis

###report


