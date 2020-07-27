"use strict";
exports.__esModule = true;
Object.defineProperty(exports, "__esModule", { value: true });
var cheerio = require("cheerio");
var axios_1 = require("axios");
function Scraper(url, login_page) {
    var Url = url;
    var AxiosInstance = axios_1["default"].create();
    AxiosInstance.get(Url)
        .then(function (responce) {
        var dataType = [];
        var html = responce.data;
        var $ = cheerio.load(html);
        var website_usr_field = $('input[type=email]');
        website_usr_field.each(function (i, elem) {
            var website_usr_field_type = $(elem).find('input[type]').text();
            var datatype = [website_usr_field_type];
        });
        var website_usr_html_type = dataType[0];
        console.log(website_usr_html_type);
        if (dataType[0] == 'text') {
            var website_usr_field_1 = $('input[type=text]');
        }
        /*
        TODO:
        1) Fix potential bug that is limiting websites to be scraped even if they have the same types for both username and password.
        2) Fix if statement with mentor
        */
        var website_pwd_field = $('input[type=password]');
        // console.log(website_usr_field);
        // console.log(website_pwd_field);
        return website_usr_field && website_pwd_field;
    })["catch"](console.error);
}
Scraper('https://www.codechef.com/', false);
