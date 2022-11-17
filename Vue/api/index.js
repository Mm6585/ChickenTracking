// implement your own methods in here, if your data is coming from A rest API

import * as AOA from './aoa'
import * as Chart from './chart';








export default {
  // chart data
  getMonthVisit: Chart.monthVisitData,
  getCampaign: Chart.campaignData,
  getLocation: Chart.locationData,


  //AOA data
  getAOA : AOA.getAOA,

};