<template>
    <div>
      <h1>유저정보</h1>
        <button @click="logOut">로그아웃</button>
    </div>
  </template>
  
  <script>
  // import { mapActions} from "vuex";
  
  export default {
    name: 'UserStatusView',
  
    // 싸피에서 알려준 방법
    
    methods: {
      logOut() {
        console.log('Rb')
        this.$store.dispatch('logOut')
      }
    }
  }
  </script>