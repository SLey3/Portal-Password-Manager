//Imports
import * as cheerio from 'cheerio';
import axios, { AxiosAdapter } from 'axios'

//Scraper function source code
async function Scraper(url: string, header_str: string, login_page?: string) {
  /*
  TODO:
  1) Create if statement for assigning login type variable for values.
  2) Fix const config  Axios Overload
  */
  if (login_page) {
    var link: string = url + '/' + login_page;
  }
  else {
    var link: string = url;
  }
  const user_agent = header_str;
   console.log(user_agent);
   const config = {
    method: 'get',
    url: link,
    headers: { 'User-Agent': user_agent }
  }
  const res = await axios(config);
  const html = null;
  const $ = cheerio.load(html);
  const website_usr_field: Cheerio = $('input[type=email]');
  //if ()
  const website_pwd_field: Cheerio = $('input[type=password]');
  console.log(website_usr_field);
  console.log(website_pwd_field);
  return website_usr_field && website_pwd_field;
}

Scraper('stackoverflow.com', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36', 'users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
