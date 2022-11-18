<template>
  <div>
    <h1>계정 생성</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">
      <hr>
      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1">
      <hr>
      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      <hr>
      <input 
        type="submit"
        value="Signup"
      >
    </form>
  </div>
</template>

<script>
// import { mapActions} from "vuex";

export default {
  name: 'SignUpView',
  // data(){
  //   return{
  //     username: null,
  //     password1: null,
  //     password2: null,
  //   }
  // },
  // methods:{
  //   ...mapActions(["signup"])
  // }

  // 싸피에서 알려준 방법
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        // username,
        // password1,
        // password2,
        username: username,
        password1: password1,
        password2: password2,
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>