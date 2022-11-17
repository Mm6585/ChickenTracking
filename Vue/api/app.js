import * as puppeteer from "puppeteer"

const browser = puppeteer.launch({
  headless : false,
  args: ["--window-size=1920,1080"],
})






export default{
  // getStudentStatus : getHeaders('http://127.0.0.1:3001').then(res => {JSON.stringify(res.data)})
}

// module.exports = app;
