__all__ = ['scraper']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['Scraper'])
@Js
def PyJsHoisted_Scraper_(username, password, this, arguments, var=var):
    var = Scope({'username':username, 'password':password, 'this':this, 'arguments':arguments}, var)
    var.registers(['password', 'username'])
    var.get('console').callprop('log', Js('This is a temporary message.'))
PyJsHoisted_Scraper_.func_name = 'Scraper'
var.put('Scraper', PyJsHoisted_Scraper_)
pass
pass


# Add lib to the module scope
scraper = var.to_python()