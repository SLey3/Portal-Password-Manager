const homeDir = require("os").homedir()
const PATHTOTS = homeDir + "\\AppData\\Local\\Programs\\Portal Password Manager\\src\\appResources\\resources\\web\\lib\\js-package\\Scraper.ts";
console.log(PATHTOTS);
const TypescriptParser = require("typescript-parser");
const parser = new TypescriptParser.TypescriptParser();

function main() {
  const parsed = await parser.parseFile(PATHTOTS, PATHTOTS)
}
