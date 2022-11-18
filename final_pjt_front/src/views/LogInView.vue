<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">
      <hr>
      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password">
      <hr>
      <input 
        type="submit" 
        value="logIn"
      />
    </form>
  </div>
</template>

<script>
// import {mapState, mapActions} from "vuex"

export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },

  // computed:{
  //   ...mapState(["isLogin"], "isLoginError")
  // },
  // methods: {
  //   ...mapActions(["login"])
  // }
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>