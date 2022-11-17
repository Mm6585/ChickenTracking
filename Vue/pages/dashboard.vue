<template>
  <div id="pageDashboard">
    <v-container grid-list-xl fluid>
      <v-layout row wrap>
        <v-flex lg6 sm6 xs12>
          <mini-statistic
            v-bind:text="parseInt(data[getDate]['aoa']).toString()"
            title="활동량"
            sub-title="Activitye"
            color="indigo"
          >
          </mini-statistic>
        </v-flex>
        <v-flex lg6 sm6 xs12>
          <mini-statistic
            v-bind:text="(Object.keys(data[getDate]).length - 1).toString()"
            title="개체수"
            sub-title="individual"
            color="red"
          >
          </mini-statistic>
        </v-flex> 

        <!-- mini statistic  end -->
        <v-flex lg12 sm12 xs12>
          <v-widget title="월별 통게" content-bg="white">
            <v-btn icon slot="widget-header-action">
              <v-icon class="text--secondary">refresh</v-icon>
            </v-btn>
            <div slot="widget-content">
              <e-chart
                
                :path-option="[
                  ['dataset.source',siteTrafficData ],
                  ['color', [color.lightBlue.base, color.green.lighten1]],
                  ['legend.show', true],
                  ['xAxis.axisLabel.show', true],
                  ['yAxis.axisLabel.show', true],
                  ['grid.left', '2%'],
                  ['grid.bottom', '5%'],
                  ['grid.right', '3%'],
                  ['series[0].type', 'bar'],
                  ['series[0].areaStyle', {}],
                  ['series[0].smooth', true],
                  ['series[1].smooth', true],
                  ['series[1].type', 'bar'],
                  ['series[1].areaStyle', {}],
                ]"
                ref="canvans1"
                height="400px"
                width="85%"
              >
              </e-chart>
            </div>
          </v-widget>
        </v-flex>    
      </v-layout>
    </v-container>
  </div>
</template>






<script>
  import API from '@/api';
  import EChart from '@/components/chart/echart';
  import MiniStatistic from '@/components/widgets/statistic/MiniStatistic';
  import VWidget from '@/components/VWidget';
  import Material from 'vuetify/es5/util/colors';
  import VCircle from '@/components/circle/VCircle';
  import CircleStatistic from '@/components/widgets/statistic/CircleStatistic';
  import StuTableStatistic from '@/components/widgets/statistic/StuTableStatistic'
  import data from '@/static/data/data.json'
  import html2canvas from 'html2canvas'

  

  export default {
    layout: 'dashboard',
    components: {
      VWidget,
      MiniStatistic,
      VCircle,
      EChart,
      CircleStatistic,
      StuTableStatistic,
    },
    mounted(){
      this.getRes()
      
    }, 
    data: () => ({
      data : data,
      aoa : '',
      date : '',
      objNum : '',
      shortDay : [],
      monthVisitData : '',
      color: Material,
      selectedTab: '',
      result : false,
    }),
    methods : {
      
      
      sendMessage() {
        const title = 'title';
        const body  = 'body';
        const options = { title };
        const notif = new Notification(title, options);
      },
      btnClickHandler() {
        this.result =  Notification.requestPermission()
        this.sendMessage()
      },
      showaoa() {
        console.log(this.getDate())
      },
      getRes() {
        for(let i = 0; i < 100; i++){
              setTimeout(function() {
                getObjInfo()
              }, 5000 * (i + 1))
            
        //get Date
        function leftPad(value) {
        if (value >= 10) {
          return value;
        }
          return `0${value}`;
        }
        const today  = new Date()
        const year = today.getFullYear();
        const month = leftPad(today.getMonth() + 1).toString();
        const day = leftPad(today.getDate()).toString();
        const date = year+month+day
    
        
        
        ///get objInfo    
        const axios = require("axios")    
        function getObjInfo() {


        
        axios
          .get('https://127.0.0.1:3002')
          .then(res => {
          
       });

       
      }
    }
      },
      getDate() {
        function leftPad(value) {
        if (value >= 10) {
          return value;
        }
          return `0${value}`;
        }
        const today  = new Date()
        const year = today.getFullYear();
        const month = leftPad(today.getMonth() + 1).toString();
        const day = leftPad(today.getDate()).toString();
        this.date = year+month+day
        console.log(this.date)

      }
    },
    computed: {
      async aoaData() {
        return this.shortDay;
      },
      getDate() {
        function leftPad(value) {
        if (value >= 10) {
          return value;
        }
          return `0${value}`;
        }
        const today  = new Date()
        const year = today.getFullYear();
        const month = leftPad(today.getMonth() + 1).toString();
        const day = leftPad(today.getDate()).toString();
        const date = year+month+day
        return date
      },
      posts () {
        return API.getPost(3);
      },
      siteTrafficData () {
        const shortMonth = Object.keys(data)
        const monthVisitData = shortMonth.map(m => {
          return {
            'month': m,
            '활동량': data[m]['aoa'],
            '개체': Object.keys(data[m]).length - 1,
          };
        });
        return monthVisitData
      },
      locationData () {
        return API.getLocation;
      },
      
    },

  };
</script>
