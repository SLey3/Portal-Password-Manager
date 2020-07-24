import { cheerio }  from 'cheerio';
import axios from 'axios';

function Scraper(url: string, content: string) {
  const Url = url;
  const AxiosInstance = axios.create();
  AxiosInstance.get(Url)
    .then(responce => {
      const html = responce.data;
      const $ = cheerio.load(html);
    })
}
