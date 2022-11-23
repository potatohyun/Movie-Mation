<template>
    <div>
      <br>
      <h1>{{username}}님 안녕하세요?</h1>
      <br>
      <button @click="logOut">로그아웃</button>
      <br>
      <br>
      <b-container class= "center-block" style="width: 300px;padding:15px;">
      <b-col>
        <b-form @submit.prevent="changePassword">
          <b-form-group id="new_password1" label="새로운 비밀번호:" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="new_password1"
              type="password"
              placeholder="비밀번호를 입력하세요"
              required
            ></b-form-input>
          </b-form-group>
          <br>
          <b-form-group id="new_password2" label="비밀번호 재확인:" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="new_password2"
              type="password"
              placeholder="비밀번호를 다시 입력하세요"
              required
            ></b-form-input>
          </b-form-group>
          <br>
          <b-button type="submit" variant="primary">비밀번호수정</b-button>
        </b-form>
      </b-col>
    </b-container>
    </div>
  </template>
  
  <script>
  // import { mapActions} from "vuex";
  const API_URL = "http://127.0.0.1:8000"
  import axios from 'axios'

  export default {
    name: 'UserStatusView',
    data(){
      return{
        username : null,
        new_password1: null,
        new_password2: null,
      }
    },
    created(){
      this.getUsername()
    },
    // 싸피에서 알려준 방법
    
    methods: {
      getToken: function (){
        const key = this.$store.state.token

        const config = {
          headers:{
              Authorization: `Token ${ key }`
          }
        }
      return config
      },
      logOut() {
        console.log('Rb')
        this.$store.dispatch('logOut')
      },
      getUsername(){
        const config = this.getToken()
        axios.get(`${API_URL}/accounts/user/`, config)
        .then((res) => {
          console.log(res.data)
          this.username = res.data.username
        }
      )},
      changePassword(){
        const new_password1 = this.new_password1
        const new_password2 = this.new_password2

        const payload = {
          new_password1: new_password1,
          new_password2: new_password2
        }
        this.$store.dispatch('changePassword', payload)
      }  
    }
  }
  </script>