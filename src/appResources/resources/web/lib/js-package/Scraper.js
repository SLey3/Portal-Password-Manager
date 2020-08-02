"use strict";
exports.__esModule = true;
var cheerio = require("cheerio");
var axios_1 = require("axios");
function Scraper(url, login_page, header_str) {
    if (login_page) {
        var link = url + '/' + login_page;
    }
    else {
        var link = url;
    }
    var user_agent = header_str;
    var AxiosInstance = axios_1["default"].create();
    AxiosInstance.get(link, { headers: { 'User-Agent': user_agent } })
        .then(function (responce) {
        var html = responce.data;
        var $ = cheerio.load(html);
        var website_usr_field = $('input[type=email]');
        //if ()
        /*
        TODO:
        1) Create if statement for assigning login type variable for values.
        */
        var website_pwd_field = $('input[type=password]');
        console.log(website_usr_field);
        console.log(website_pwd_field);
        return website_usr_field && website_pwd_field;
    })["catch"](console.error);
}
Scraper('stackoverflow.com', 'users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f');
//'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
