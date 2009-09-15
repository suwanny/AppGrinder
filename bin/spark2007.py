# The Grinder 3.2
# HTTP script recorded by TCPProxy at Jul 11, 2009 3:14:59 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

headers0= \
  ( NVPair('Accept', 'image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/x-shockwave-flash, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, application/x-silverlight, application/x-ms-application, application/x-ms-xbap, application/vnd.ms-xpsdocument, application/xaml+xml, */*'),
    NVPair('Accept-Language', 'ko'),
    NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; GTB5; SU 3.23; InfoPath.2; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'), )

headers1= \
  ( NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://appscale.cs.ucsb.edu/~spark2007/index.new.php'),
    NVPair('Accept-Language', 'ko'),
    NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; GTB5; SU 3.23; InfoPath.2; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'), )

headers2= \
  ( NVPair('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.33 Safari/530.5'),
    NVPair('Referer', 'http://mail.google.com/mail/?ui=2&view=js&name=js&ver=xWWCalDiPoM.en.&am=!1cqNLSaoA8C5he3iwbQ2woaWAD5IGcpXuAZXp6kv'),
    NVPair('Accept', '*/*'),
    NVPair('Accept-Encoding', 'gzip,deflate,bzip2,sdch'),
    NVPair('Accept-Language', 'en-US,en;q=0.8'),
    NVPair('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'), )

headers3= \
  ( NVPair('Accept', '*/*'),
    NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; GTB5; SU 3.23; InfoPath.2; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'), )

headers4= \
  ( NVPair('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.33 Safari/530.5'),
    NVPair('Cache-Control', 'max-age=0'),
    NVPair('Accept', 'application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5'),
    NVPair('Accept-Encoding', 'gzip,deflate,bzip2,sdch'),
    NVPair('Accept-Language', 'en-US,en;q=0.8'),
    NVPair('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'), )

headers5= \
  ( NVPair('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.33 Safari/530.5'),
    NVPair('Referer', 'http://appscale.cs.ucsb.edu/~spark2007/index.new.php'),
    NVPair('Cache-Control', 'max-age=0'),
    NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Accept-Encoding', 'gzip,deflate,bzip2,sdch'),
    NVPair('Accept-Language', 'en-US,en;q=0.8'),
    NVPair('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'), )

headers6= \
  ( NVPair('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.33 Safari/530.5'),
    NVPair('Referer', 'http://appscale.cs.ucsb.edu/~spark2007/index.new.php'),
    NVPair('Cache-Control', 'max-age=0'),
    NVPair('Accept', '*/*'),
    NVPair('Accept-Encoding', 'gzip,deflate,bzip2,sdch'),
    NVPair('Accept-Language', 'en-US,en;q=0.8'),
    NVPair('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'), )

url0 = 'http://appscale.cs.ucsb.edu:80'
url1 = 'http://www.google.com:80'
url2 = 'http://ajax.googleapis.com:80'
url3 = 'http://mail.google.com:80'
url4 = 'http://www.google-analytics.com:80'

# Create an HTTPRequest for each request, then replace the
# reference to the HTTPRequest with an instrumented version.
# You can access the unadorned instance using request101.__target__.
request101 = HTTPRequest(url=url0, headers=headers0)
request101 = Test(101, 'GET index.new.php').wrap(request101)

request102 = HTTPRequest(url=url0, headers=headers1)
request102 = Test(102, 'GET css.css').wrap(request102)

request103 = HTTPRequest(url=url0, headers=headers1)
request103 = Test(103, 'GET jquery-ui-1.7.2.custom.css').wrap(request103)

request201 = HTTPRequest(url=url1, headers=headers1)
request201 = Test(201, 'GET jsapi').wrap(request201)

request301 = HTTPRequest(url=url2, headers=headers1)
request301 = Test(301, 'GET jquery.min.js').wrap(request301)

request401 = HTTPRequest(url=url3, headers=headers2)
request401 = Test(401, 'POST bind').wrap(request401)

request501 = HTTPRequest(url=url2, headers=headers1)
request501 = Test(501, 'GET jquery-ui.min.js').wrap(request501)

request601 = HTTPRequest(url=url0, headers=headers1)
request601 = Test(601, 'GET clock.js').wrap(request601)

request602 = HTTPRequest(url=url0, headers=headers1)
request602 = Test(602, 'GET header.jpg').wrap(request602)

request701 = HTTPRequest(url=url3, headers=headers2)
request701 = Test(701, 'POST /').wrap(request701)

request801 = HTTPRequest(url=url0, headers=headers1)
request801 = Test(801, 'GET link_icon.jpg').wrap(request801)

request901 = HTTPRequest(url=url4, headers=headers1)
request901 = Test(901, 'GET ga.js').wrap(request901)

request902 = HTTPRequest(url=url4, headers=headers1)
request902 = Test(902, 'GET __utm.gif').wrap(request902)

request1001 = HTTPRequest(url=url0, headers=headers1)
request1001 = Test(1001, 'GET ui-bg_highlight-soft_100_eeeeee_1x100.png').wrap(request1001)

request1101 = HTTPRequest(url=url1, headers=headers1)
request1101 = Test(1101, 'GET stats').wrap(request1101)

request1201 = HTTPRequest(url=url0, headers=headers1)
request1201 = Test(1201, 'GET ui-icons_ef8c08_256x240.png').wrap(request1201)

request1202 = HTTPRequest(url=url0, headers=headers1)
request1202 = Test(1202, 'GET ui-bg_glass_100_f6f6f6_1x400.png').wrap(request1202)

request1203 = HTTPRequest(url=url0, headers=headers3)
request1203 = Test(1203, 'GET jupiter.ico').wrap(request1203)

request1204 = HTTPRequest(url=url0, headers=headers1)
request1204 = Test(1204, 'GET ui-bg_glass_65_ffffff_1x400.png').wrap(request1204)

request1205 = HTTPRequest(url=url0, headers=headers1)
request1205 = Test(1205, 'GET ui-icons_ffffff_256x240.png').wrap(request1205)

request1301 = HTTPRequest(url=url3, headers=headers2)
request1301 = Test(1301, 'POST bind').wrap(request1301)

request1401 = HTTPRequest(url=url0, headers=headers1)
request1401 = Test(1401, 'GET ui-bg_gloss-wave_35_f6a828_500x100.png').wrap(request1401)

request1402 = HTTPRequest(url=url0, headers=headers1)
request1402 = Test(1402, 'GET ui-bg_highlight-soft_75_ffe45c_1x100.png').wrap(request1402)

request1501 = HTTPRequest(url=url0, headers=headers4)
request1501 = Test(1501, 'GET index.new.php').wrap(request1501)

request1502 = HTTPRequest(url=url0, headers=headers5)
request1502 = Test(1502, 'GET jquery-ui-1.7.2.custom.css').wrap(request1502)

request1503 = HTTPRequest(url=url0, headers=headers5)
request1503 = Test(1503, 'GET css.css').wrap(request1503)

request1504 = HTTPRequest(url=url0, headers=headers1)
request1504 = Test(1504, 'GET ui-bg_glass_100_fdf5ce_1x400.png').wrap(request1504)

request1601 = HTTPRequest(url=url1, headers=headers6)
request1601 = Test(1601, 'GET jsapi').wrap(request1601)

request1701 = HTTPRequest(url=url2, headers=headers6)
request1701 = Test(1701, 'GET jquery.min.js').wrap(request1701)

request1801 = HTTPRequest(url=url0, headers=headers6)
request1801 = Test(1801, 'GET clock.js').wrap(request1801)

request1802 = HTTPRequest(url=url0, headers=headers6)
request1802 = Test(1802, 'GET link_icon.jpg').wrap(request1802)

request1901 = HTTPRequest(url=url3, headers=headers2)
request1901 = Test(1901, 'GET bind').wrap(request1901)

request2001 = HTTPRequest(url=url1, headers=headers6)
request2001 = Test(2001, 'GET stats').wrap(request2001)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET index.new.php (requests 101-103)."""
    result = request101.GET('/~spark2007/index.new.php')

    grinder.sleep(5205)
    request102.GET('/~spark2007/css/css.css')

    grinder.sleep(10116)
    request103.GET('/~spark2007/css/ui-lightness/jquery-ui-1.7.2.custom.css')

    return result

  def page2(self):
    """GET jsapi (request 201)."""
    result = request201.GET('/jsapi')

    return result

  def page3(self):
    """GET jquery.min.js (request 301)."""
    result = request301.GET('/ajax/libs/jquery/1.3.2/jquery.min.js')

    return result

  def page4(self):
    """POST bind (request 401)."""
    self.token_VER = \
      '6'
    self.token_it = \
      '718821'
    self.token_at = \
      'xn3j2zpap76rlhp4zyzjyr58rjhydc'
    self.token_SID = \
      'C7224FA2CB3E0BF1'
    self.token_RID = \
      '14153'
    self.token_zx = \
      'kew5b2hvwbas'
    self.token_t = \
      '1'
    result = request401.POST('/mail/channel/bind' +
      '?VER=' +
      self.token_VER +
      '&it=' +
      self.token_it +
      '&at=' +
      self.token_at +
      '&SID=' +
      self.token_SID +
      '&RID=' +
      self.token_RID +
      '&zx=' +
      self.token_zx +
      '&t=' +
      self.token_t,
      ( NVPair('count', '1'),
        NVPair('req0_type', 'i'),
        NVPair('req0_time', '718817'),
        NVPair('req0_evtype', 'keyup'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page5(self):
    """GET jquery-ui.min.js (request 501)."""
    result = request501.GET('/ajax/libs/jqueryui/1.7.2/jquery-ui.min.js')

    return result

  def page6(self):
    """GET clock.js (requests 601-602)."""
    result = request601.GET('/~spark2007/js/clock.js')

    grinder.sleep(84)
    request602.GET('/~spark2007/images/header.jpg')

    return result

  def page7(self):
    """POST / (request 701)."""
    self.token_ui = \
      '2'
    self.token_ik = \
      'd20d30084f'
    self.token_view = \
      'tl'
    self.token_start = \
      '0'
    self.token_num = \
      '70'
    self.token_auto = \
      '1'
    self.token_ver = \
      'xWWCalDiPoM.en.'
    self.token_am = \
      '!1cqNLSaoA8C5he3iwbQ2woaWAD5IGcpXuAZXp6kv'
    self.token_ari = \
      '300'
    self.token_rt = \
      'j'
    self.token_search = \
      'inbox'
    result = request701.POST('/mail/' +
      '?ui=' +
      self.token_ui +
      '&ik=' +
      self.token_ik +
      '&view=' +
      self.token_view +
      '&start=' +
      self.token_start +
      '&num=' +
      self.token_num +
      '&auto=' +
      self.token_auto +
      '&ver=' +
      self.token_ver +
      '&am=' +
      self.token_am +
      '&ari=' +
      self.token_ari +
      '&rt=' +
      self.token_rt +
      '&search=' +
      self.token_search,
      '',
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded;charset=utf-8'), ))

    return result

  def page8(self):
    """GET link_icon.jpg (request 801)."""
    result = request801.GET('/~spark2007/images/link_icon.jpg')

    return result

  def page9(self):
    """GET ga.js (requests 901-902)."""
    result = request901.GET('/ga.js')

    grinder.sleep(106)
    self.token_utmwv = \
      '4.3.1'
    self.token_utmn = \
      '1355577595'
    self.token_utmhn = \
      'appscale.cs.ucsb.edu'
    self.token_utmcs = \
      'ks_c_5601-1987'
    self.token_utmsr = \
      '1280x800'
    self.token_utmsc = \
      '32-bit'
    self.token_utmul = \
      'ko'
    self.token_utmje = \
      '1'
    self.token_utmfl = \
      '10.0 r12'
    self.token_utmdt = \
      'SOO HWAN PARK@CS.UCSB'
    self.token_utmhid = \
      '1530220599'
    self.token_utmr = \
      '-'
    self.token_utmp = \
      '/~spark2007/index.new.php'
    self.token_utmac = \
      'UA-9657390-1'
    self.token_utmcc = \
      '__utma=91329354.432216382147455740.1235161294.1246928688.1247350458.3;+__utmz=91329354.1235161294.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);'
    request902.GET('/__utm.gif' +
      '?utmwv=' +
      self.token_utmwv +
      '&utmn=' +
      self.token_utmn +
      '&utmhn=' +
      self.token_utmhn +
      '&utmcs=' +
      self.token_utmcs +
      '&utmsr=' +
      self.token_utmsr +
      '&utmsc=' +
      self.token_utmsc +
      '&utmul=' +
      self.token_utmul +
      '&utmje=' +
      self.token_utmje +
      '&utmfl=' +
      self.token_utmfl +
      '&utmdt=' +
      self.token_utmdt +
      '&utmhid=' +
      self.token_utmhid +
      '&utmr=' +
      self.token_utmr +
      '&utmp=' +
      self.token_utmp +
      '&utmac=' +
      self.token_utmac +
      '&utmcc=' +
      self.token_utmcc)

    return result

  def page10(self):
    """GET ui-bg_highlight-soft_100_eeeeee_1x100.png (request 1001)."""
    result = request1001.GET('/~spark2007/css/ui-lightness/images/ui-bg_highlight-soft_100_eeeeee_1x100.png')

    return result

  def page11(self):
    """GET stats (request 1101)."""
    self.token_r0 = \
      'el|jquery'
    self.token_r1 = \
      'el|jqueryui'
    self.token_nc = \
      '1247350447843_15015'
    result = request1101.GET('/uds/stats' +
      '?r0=' +
      self.token_r0 +
      '&r1=' +
      self.token_r1 +
      '&nc=' +
      self.token_nc)

    return result

  def page12(self):
    """GET ui-icons_ef8c08_256x240.png (requests 1201-1205)."""
    result = request1201.GET('/~spark2007/css/ui-lightness/images/ui-icons_ef8c08_256x240.png')

    grinder.sleep(4990)
    request1202.GET('/~spark2007/css/ui-lightness/images/ui-bg_glass_100_f6f6f6_1x400.png')

    grinder.sleep(5050)
    request1203.GET('/~spark2007/jupiter.ico')

    grinder.sleep(4977)
    request1204.GET('/~spark2007/css/ui-lightness/images/ui-bg_glass_65_ffffff_1x400.png')

    grinder.sleep(10057)
    request1205.GET('/~spark2007/css/ui-lightness/images/ui-icons_ffffff_256x240.png')

    return result

  def page13(self):
    """POST bind (request 1301)."""
    self.token_it = \
      '778834'
    self.token_RID = \
      '14154'
    self.token_zx = \
      'cmywf6ljyfad'
    result = request1301.POST('/mail/channel/bind' +
      '?VER=' +
      self.token_VER +
      '&it=' +
      self.token_it +
      '&at=' +
      self.token_at +
      '&SID=' +
      self.token_SID +
      '&RID=' +
      self.token_RID +
      '&zx=' +
      self.token_zx +
      '&t=' +
      self.token_t,
      ( NVPair('count', '1'),
        NVPair('req0_type', 'i'),
        NVPair('req0_time', '778830'),
        NVPair('req0_evtype', 'keyup'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page14(self):
    """GET ui-bg_gloss-wave_35_f6a828_500x100.png (requests 1401-1402)."""
    result = request1401.GET('/~spark2007/css/ui-lightness/images/ui-bg_gloss-wave_35_f6a828_500x100.png')

    grinder.sleep(5026)
    request1402.GET('/~spark2007/css/ui-lightness/images/ui-bg_highlight-soft_75_ffe45c_1x100.png')

    return result

  def page15(self):
    """GET index.new.php (requests 1501-1504)."""
    result = request1501.GET('/~spark2007/index.new.php')

    grinder.sleep(38)
    request1502.GET('/~spark2007/css/ui-lightness/jquery-ui-1.7.2.custom.css', None,
      ( NVPair('If-None-Match', '\"764e4f-6b88-46c250efe9e00\"'),
        NVPair('If-Modified-Since', 'Fri, 12 Jun 2009 11:32:08 GMT'), ))

    request1503.GET('/~spark2007/css/css.css', None,
      ( NVPair('If-None-Match', '\"764e74-19a0-46e560b14d4c0\"'),
        NVPair('If-Modified-Since', 'Fri, 10 Jul 2009 08:48:59 GMT'), ))

    grinder.sleep(707)
    request1504.GET('/~spark2007/css/ui-lightness/images/ui-bg_glass_100_fdf5ce_1x400.png')

    return result

  def page16(self):
    """GET jsapi (request 1601)."""
    result = request1601.GET('/jsapi')

    return result

  def page17(self):
    """GET jquery.min.js (request 1701)."""
    result = request1701.GET('/ajax/libs/jquery/1.3.2/jquery.min.js', None,
      ( NVPair('If-Modified-Since', 'Thu, 19 Feb 2009 22:38:52 GMT'), ))

    return result

  def page18(self):
    """GET clock.js (requests 1801-1802)."""
    result = request1801.GET('/~spark2007/js/clock.js', None,
      ( NVPair('If-None-Match', '\"764983-337-46e12c8bae1c0\"'),
        NVPair('If-Modified-Since', 'Tue, 07 Jul 2009 00:34:23 GMT'), ))

    grinder.sleep(5031)
    request1802.GET('/~spark2007/images/link_icon.jpg', None,
      ( NVPair('If-None-Match', '\"76499b-14aa-4441812bb20c0\"'),
        NVPair('If-Modified-Since', 'Sat, 19 Jan 2008 19:14:51 GMT'), ))

    return result

  def page19(self):
    """GET bind (request 1901)."""
    self.token_it = \
      '811686'
    self.token_RID = \
      'rpc'
    self.token_CI = \
      '0'
    self.token_AID = \
      '386'
    self.token_TYPE = \
      'xmlhttp'
    self.token_zx = \
      'llvr1ef03hej'
    result = request1901.GET('/mail/channel/bind' +
      '?VER=' +
      self.token_VER +
      '&it=' +
      self.token_it +
      '&at=' +
      self.token_at +
      '&RID=' +
      self.token_RID +
      '&SID=' +
      self.token_SID +
      '&CI=' +
      self.token_CI +
      '&AID=' +
      self.token_AID +
      '&TYPE=' +
      self.token_TYPE +
      '&zx=' +
      self.token_zx +
      '&t=' +
      self.token_t)

    return result

  def page20(self):
    """GET stats (request 2001)."""
    self.token_nc = \
      '1247350538674_15002'
    result = request2001.GET('/uds/stats' +
      '?r0=' +
      self.token_r0 +
      '&r1=' +
      self.token_r1 +
      '&nc=' +
      self.token_nc)

    return result

  def __call__(self):
    """This method is called for every run performed by the worker thread."""
    self.page1()      # GET index.new.php (requests 101-103)

    grinder.sleep(10045)
    self.page2()      # GET jsapi (request 201)

    grinder.sleep(61)
    self.page3()      # GET jquery.min.js (request 301)

    grinder.sleep(4921)
    self.page4()      # POST bind (request 401)

    grinder.sleep(4895)
    self.page5()      # GET jquery-ui.min.js (request 501)

    grinder.sleep(349)
    self.page6()      # GET clock.js (requests 601-602)

    grinder.sleep(4494)
    self.page7()      # POST / (request 701)

    grinder.sleep(4822)
    self.page8()      # GET link_icon.jpg (request 801)

    grinder.sleep(5076)
    self.page9()      # GET ga.js (requests 901-902)
    self.page10()     # GET ui-bg_highlight-soft_100_eeeeee_1x100.png (request 1001)

    grinder.sleep(4742)
    self.page11()     # GET stats (request 1101)

    grinder.sleep(32)
    self.page12()     # GET ui-icons_ef8c08_256x240.png (requests 1201-1205)

    grinder.sleep(3564)
    self.page13()     # POST bind (request 1301)

    grinder.sleep(6441)
    self.page14()     # GET ui-bg_gloss-wave_35_f6a828_500x100.png (requests 1401-1402)

    grinder.sleep(14427)
    self.page15()     # GET index.new.php (requests 1501-1504)

    grinder.sleep(5049)
    self.page16()     # GET jsapi (request 1601)

    grinder.sleep(51)
    self.page17()     # GET jquery.min.js (request 1701)

    grinder.sleep(4846)
    self.page18()     # GET clock.js (requests 1801-1802)
    self.page19()     # GET bind (request 1901)

    grinder.sleep(4933)
    self.page20()     # GET stats (request 2001)


def instrumentMethod(test, method_name, c=TestRunner):
  """Instrument a method with the given Test."""
  unadorned = getattr(c, method_name)
  import new
  method = new.instancemethod(test.wrap(unadorned), None, c)
  setattr(c, method_name, method)

# Replace each method with an instrumented version.
# You can call the unadorned method using self.page1.__target__().
instrumentMethod(Test(100, 'Page 1'), 'page1')
instrumentMethod(Test(200, 'Page 2'), 'page2')
instrumentMethod(Test(300, 'Page 3'), 'page3')
instrumentMethod(Test(400, 'Page 4'), 'page4')
instrumentMethod(Test(500, 'Page 5'), 'page5')
instrumentMethod(Test(600, 'Page 6'), 'page6')
instrumentMethod(Test(700, 'Page 7'), 'page7')
instrumentMethod(Test(800, 'Page 8'), 'page8')
instrumentMethod(Test(900, 'Page 9'), 'page9')
instrumentMethod(Test(1000, 'Page 10'), 'page10')
instrumentMethod(Test(1100, 'Page 11'), 'page11')
instrumentMethod(Test(1200, 'Page 12'), 'page12')
instrumentMethod(Test(1300, 'Page 13'), 'page13')
instrumentMethod(Test(1400, 'Page 14'), 'page14')
instrumentMethod(Test(1500, 'Page 15'), 'page15')
instrumentMethod(Test(1600, 'Page 16'), 'page16')
instrumentMethod(Test(1700, 'Page 17'), 'page17')
instrumentMethod(Test(1800, 'Page 18'), 'page18')
instrumentMethod(Test(1900, 'Page 19'), 'page19')
instrumentMethod(Test(2000, 'Page 20'), 'page20')
