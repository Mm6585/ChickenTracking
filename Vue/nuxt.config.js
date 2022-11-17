const pkg = require('./package')
const VuetifyLoaderPlugin = require('vuetify-loader/lib/plugin')


module.exports = {
  mode: 'spa',
  env: {
    result : process.env.result_01
  },
  /*
  ** Headers of the page
  */
  head: {
    title: 'ChickTrack',
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {
        hid: 'description', name: 'description', content: '한밭대학교 캡스톤 출결관리 시스템입니다 \n' +
          '    contact : 20172598@edu.hanbat.ac.kr.'
      }
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'},
      {
        rel: 'stylesheet',
        href:
          'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons'
      }
    ],
    script: [
      {src: 'https://cdnjs.cloudflare.com/ajax/libs/echarts/4.0.4/echarts-en.min.js'}
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: {color: '#3adced'},

  /*
  ** Global CSS
  */
  css: [
    '~/assets/style/theme.styl',
    '~/assets/style/app.styl',
    'font-awesome/css/font-awesome.css',
    'roboto-fontface/css/roboto/roboto-fontface.css'
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '@/plugins/vuetify',
    '@/plugins/vee-validate',
    '@/plugins/sw',
    // '@/plugins/firebase'
  ],

  /*ap
  ** Nuxt.js modules
  */
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/pwa'
  ],
      
  pwa: {
    meta: {
      nativeUI: true, // app-like UI
    },
    manifest: {
      name: '양계장관리시스템', // represents the name of the web application
      short_name: '양계장관리시스템', // represents the name of the web application if there is not enough space to display
      description: '아무고토 몰라요팀 AI 양계장 시스템입니다',
      background_color: '#152f73', // a placeholder background color for the application page
      theme_color: '#152f73', // the default theme color for the application
      display: 'fullscreen', // determines the developers’ preferred display mode for the website
      orientation: 'portrait', // the default orientation for all the website's top-level browsing
      icons: [ // icon image path: @/static/icon.png
        {
          src: "favicon.ico", // favicon
          sizes: "64x64 32x32 24x24 16x16",
          type: "image/x-icon"
        },
        {
          src: "images/icon.png", // 192
          sizes: "192x192",
          type: "image/png"
        },
        {
          src: "images/icon.png", // 512
          sizes: "512x512",
          type: "image/png"
        }
      ],
    },
  },

  /*
  ** Build configuration
  */
  manifest: {
    gcm_sender_id: '103953800507',
    name: 'nuxt_pwa',
    short_name: 'NuxtPwa',
    start_url: '/?utm_source=homescreen',
    display: 'standalone',
    background_color: '#000'
  },
  workbox: {
    offline: false,
    runtimeCaching: [
      {
        urlPattern: "/*",
        handler: "networkFirst",
        method: "GET"
      }
    ]
  },
  build: {
    ssr : true,
    transpile: ['vuetify/lib'],
    plugins: [new VuetifyLoaderPlugin()],
    loaders: {
      stylus: {
        import: ["~assets/style/variables.styl"]
      }
    },

    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
    }
  }
}