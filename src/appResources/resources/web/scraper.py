__all__ = ['scraper']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['Scraper', 'axios_1', 'cheerio'])
@Js
def PyJsHoisted_Scraper_(url, login_page, this, arguments, var=var):
    var = Scope({'url':url, 'login_page':login_page, 'this':this, 'arguments':arguments}, var)
    var.registers(['Url', 'url', 'login_page', 'AxiosInstance'])
    var.put('Url', var.get('url'))
    var.put('AxiosInstance', var.get('axios_1').get('default').callprop('create'))
    @Js
    def PyJs_anonymous_0_(responce, this, arguments, var=var):
        var = Scope({'responce':responce, 'this':this, 'arguments':arguments}, var)
        var.registers(['website_pwd_field', '$', 'responce', 'html', 'website_usr_field'])
        var.put('html', var.get('responce').get('data'))
        var.put('$', var.get('cheerio').callprop('load', var.get('html')))
        var.put('website_usr_field', var.get('$')(Js('input[type=email]')))
        var.put('website_pwd_field', var.get('$')(Js('input[type=password]')))
        var.get('console').callprop('log', var.get('website_usr_field'))
        var.get('console').callprop('log', var.get('website_pwd_field'))
        return (var.get('website_usr_field') and var.get('website_pwd_field'))
    PyJs_anonymous_0_._set_name('anonymous')
    var.get('AxiosInstance').callprop('get', var.get('Url')).callprop('then', PyJs_anonymous_0_).callprop('catch', var.get('console').get('error'))
PyJsHoisted_Scraper_.func_name = 'Scraper'
var.put('Scraper', PyJsHoisted_Scraper_)
Js('use strict')
var.get('exports').put('__esModule', Js(True))
var.get('Object').callprop('defineProperty', var.get('exports'), Js('__esModule'), Js({'value':Js(True)}))
var.put('cheerio', var.get('require')(Js('cheerio')))
var.put('axios_1', var.get('require')(Js('axios')))
pass
var.get('Scraper')(Js('https://www.gmail.com/'), Js(False))
pass


# Add lib to the module scope
scraper = var.to_python()