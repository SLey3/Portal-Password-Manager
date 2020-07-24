__all__ = ['scraper']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['cheerio_1', 'axios_1', 'Scraper'])
@Js
def PyJsHoisted_Scraper_(url, content, this, arguments, var=var):
    var = Scope({'url':url, 'content':content, 'this':this, 'arguments':arguments}, var)
    var.registers(['AxiosInstance', 'url', 'content', 'Url'])
    var.put('Url', var.get('url'))
    var.put('AxiosInstance', var.get('axios_1').get('default').callprop('create'))
    @Js
    def PyJs_anonymous_0_(responce, this, arguments, var=var):
        var = Scope({'responce':responce, 'this':this, 'arguments':arguments}, var)
        var.registers(['$', 'html', 'responce'])
        var.put('html', var.get('responce').get('data'))
        var.put('$', var.get('cheerio_1').get('cheerio').callprop('load', var.get('html')))
    PyJs_anonymous_0_._set_name('anonymous')
    var.get('AxiosInstance').callprop('get', var.get('Url')).callprop('then', PyJs_anonymous_0_)
PyJsHoisted_Scraper_.func_name = 'Scraper'
var.put('Scraper', PyJsHoisted_Scraper_)
Js('use strict')
var.get('exports').put('__esModule', Js(True))
var.put('cheerio_1', var.get('require')(Js('cheerio')))
var.put('axios_1', var.get('require')(Js('axios')))
pass
pass


# Add lib to the module scope
scraper = var.to_python()