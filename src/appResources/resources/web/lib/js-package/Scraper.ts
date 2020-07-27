Object.defineProperty(exports, "__esModule", { value: true });
import * as cheerio from 'cheerio';
import axios from 'axios';

interface usrdata {
  [index: number]: string
}

function Scraper(url: string, login_page?: boolean){
  const Url = url;
  const AxiosInstance = axios.create();
  AxiosInstance.get(Url)
    .then(responce => {
      const dataType: usrdata[] = [];
      const html = responce.data;
      const $ = cheerio.load(html);
      const website_usr_field: Cheerio = $('input[type=email]');
      website_usr_field.each((i, elem) => {
        const website_usr_field_type: string = $(elem).find('input[type]').text();
        let datatype: usrdata = [website_usr_field_type];
      })
      const website_usr_html_type = dataType[0];
      if (dataType[0] == 'text') {
        const website_usr_field: Cheerio = $('input[type=text]');
      }
      /*
      TODO:
      1) Fix potential bug that is limiting websites to be scraped even if they have the same types for both username and password.
      2) Fix if statement with mentor
      */
      const website_pwd_field: Cheerio = $('input[type=password]');
      console.log(website_usr_field);
      console.log(website_pwd_field);
      return website_usr_field && website_pwd_field;
    }).catch(console.error);
}

Scraper('https://www.codechef.com/', false);
