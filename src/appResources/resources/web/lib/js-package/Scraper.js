"use strict";
exports.__esModule = true;
Object.defineProperty(exports, "__esModule", { value: true });
var cheerio = require("cheerio");
var axios_1 = require("axios");
var userAgent = require("ua-parser-js");
var parser = new userAgent.UAParser();
console.log(parser.getUA());
console.log(navigator.userAgent);
function Scraper(url, login_page) {
    if (login_page) {
        var link = url + '/' + login_page;
    }
    else {
        var link = url;
    }
    var AxiosInstance = axios_1["default"].create();
    AxiosInstance.get(link)
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
