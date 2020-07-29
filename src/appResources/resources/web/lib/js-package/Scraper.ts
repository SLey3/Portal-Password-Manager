Object.defineProperty(exports, "__esModule", { value: true });
import * as cheerio from 'cheerio';
import axios from 'axios'


function Scraper(url: string, login_page?: string){
  if (login_page) {
    var link: string = url + '/' + login_page;
  }
  else {
    var link: string = url;
  }
  const AxiosInstance = axios.create();
  AxiosInstance.get(link)
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
