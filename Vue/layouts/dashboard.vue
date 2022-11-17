<template>
  <div id="appRoot">
    <template>
      <v-app id="inspire" class="app">
        <app-drawer class="app--drawer"></app-drawer>
        <app-toolbar class="app--toolbar"></app-toolbar>
        <v-content>
          <!-- Page Header -->
          <page-header></page-header>
          <div class="page-wrapper">
            <nuxt/>
          </div>
        </v-content>
        <app-fab></app-fab>
        
      </v-app>
    </template>


    <v-snackbar
      :timeout="3000"
      bottom
      right
      :color="snackbar.color"
      v-model="snackbar.show"
    >
      {{ snackbar.text }}
      <v-btn dark flat @click.native="snackbar.show = false" icon>
        <v-icon>close</v-icon>
      </v-btn>
    </v-snackbar>
  </div>
</template>

<script>
  import AppDrawer from '@/components/AppDrawer'
  import AppToolbar from '@/components/AppToolbar'
  import AppFab from '@/components/AppFab'
  import PageHeader from '@/components/PageHeader'
  
  export default {
    components: {
      AppDrawer,
      AppToolbar,
      AppFab,
      PageHeader,
    },
    data: () => ({
      expanded: true,
      rightDrawer: false,
      snackbar: {
        show: false,
        text: '',
        color: '',
      }
    }),

  }
</script>

<style lang="stylus" scoped>
  .page-wrapper
    min-height: calc(100vh - 64px - 50px - 81px);
    margin-bottom 50px;

  .app--footer
    position absolute;
    bottom 0;
    width 100%;

</style>
