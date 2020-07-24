"use strict";
exports.__esModule = true;
var cheerio_1 = require("cheerio");
var axios_1 = require("axios");
function Scraper(url, content) {
    var Url = url;
    var AxiosInstance = axios_1["default"].create();
    AxiosInstance.get(Url)
        .then(function (responce) {
        var html = responce.data;
        var $ = cheerio_1.cheerio.load(html);
    });
}
