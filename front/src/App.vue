<template>
  <v-app>
    <v-app-bar
      app
      color="dark"
      dark
    >
      <clock />

      <v-spacer></v-spacer>
      <div class="menu">
        <router-link to="/">관제페이지</router-link>
      </div>
      <div class="menu">
        <p><router-link to="about">이전페이지</router-link></p>
      </div>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Clock from './components/Clock.vue';

export default {
  name: 'App',

  components: {
    Clock
  },
};
</script>

<style>
  .menu {width: 100px;}
</style>