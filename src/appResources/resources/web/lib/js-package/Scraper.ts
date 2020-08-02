import * as cheerio from 'cheerio';
import axios from 'axios'


function Scraper(url: string, header_str: string, login_page?: string) {
  if (login_page) {
    var link: string = url + '/' + login_page;
  }
  else {
    var link: string = url;
  }
  const user_agent = header_str;
  const AxiosInstance = axios.create();
  AxiosInstance.get(link, { headers: { 'User-Agent': user_agent } })
    .then(responce => {
      const html = responce.data;
      const $ = cheerio.load(html);
      const website_usr_field: Cheerio = $('input[type=email]');
      //if ()
      /*
      TODO:
      1) Create if statement for assigning login type variable for values.
      */
      const website_pwd_field: Cheerio = $('input[type=password]');
      console.log(website_usr_field);
      console.log(website_pwd_field);
      return website_usr_field && website_pwd_field;
    }).catch(console.error);
}

Scraper('stackoverflow.com', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36', 'users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
