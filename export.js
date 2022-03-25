const path = require("path");
const { execSync } = require("child_process");
// get root folder of global node modules
const root = execSync("npm root -g").toString().trim();

const puppeteer = require(`${root}/puppeteer`);

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await page.goto(`file:${path.join(__dirname, "poster.html")}`);
  await page.waitForTimeout(5000);
  await page.pdf({
    path: "poster.pdf",
    printBackground: true,
    width: "1920px",
    height: "1080px",
  });
  await page.screenshot({ path: "poster.png" });
  await browser.close();
})();
