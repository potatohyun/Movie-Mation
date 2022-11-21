import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'


Vue.use(Vuex)
const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    token: null,
    userInfo: null,
    // isLogin: false,
    // isLoginError: false
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies){
          state.movies = movies
      },
    // DELETE_COMMENT(comment){
    //   console.log(comment)
    //   comment = comment.filter((comment) => {
    //     return !(comment === comment)
    //   })
    // },
    SAVE_TOKEN(state, token) {
      state.token = token
      },
    // loginSuccess(state, payload){
    //   state.isLogin = true
    //   state.isLoginError = false
    //   state.userInfo = payload
    // },
    // loginError(state) {
    //   state.isLogin = false
    //   state.isLoginError = false
    //   state.userInfo = null
    // },
    loginout(state) {
      state.isLogin = false
      state.isLoginError = false
      state.userInfo = null
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url:`${API_URL}/main/movies/`,
      })
      .then(res=>
          context.commit('GET_MOVIES', res.data)
        )
      .catch(err=>console.log(err))
    },
    // deleteComment(context, comment){
    //   context.commit('DELETE_COMMENT', comment)
    // },
    signUp(context, payload) {
      // console.log(API_URL)
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
          alert("회원가입이 성공적으로 이뤄졌습니다.")
          router.push({ name: "LogInView" })
        })
        .catch(err =>console.log(err))
    },
    
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
          alert("환영합니다!")
          router.push({ name: "MovieView" })
        })
        .catch(() => {
          alert("이메일과 비밀번호를 확인하세요.")
        });
    },
    // login(dispatch, loginObj) {
    //   // login --> 토큰 반환
    //   axios
    //     .post(`${API_URL}/accounts/login/`,loginObj)
    //   // loginObj = {email,password}를 받아온다.
    //     .then(res => {
    //   // 접근 성공시, 토큰 값이 반환된다. (실제로는 토큰과 함께 유저 id를 받아온다.)
    //   // 토큰을 헤더 정보에 포함시켜서 유저 정보를 요청
    //     let token = res.data.token
    //   //토큰을 로컬 스토리지에 저장
    //     localStorage.setItem("access_token", token); //로컬 스토리지에 토큰 저장
    //     this.dispatch("getMemberInfo")
    //     router.push({ name: "MovieView" })
    //     console.log(res)
    //   })
    //   .catch(() => {
    //     alert("이메일과 비밀번호를 확인하세요.")
    //   });
    // },
    // logout({ commit }) {
    //   commit("logout");
    //   router.push({ name: "MovieView" })
    // },
    // signup(dispatch, loginObj) {
    //   // login --> 토큰 반환
    //   axios
    //     .post(`${API_URL}/accounts/signup/`,loginObj)
    //   // loginObj = {email,password}
    //     .then(res => {
    //       alert("회원가입이 성공적으로 이뤄졌습니다.")
    //       router.push({ name: "LogInView" })
    //       console.log(res)
    //     })
    //     .catch(() => {
    //       alert("이메일과 비밀번호를 확인하세요.")
    //     });
    // },
    // getMemberInfo({ commit }) {
    //   //로컬 스토리지에 저장된 토큰을 저장한다.
    //   let token = localStorage.getItem("access_token")
    //   let config = {
    //     headers: {
    //     "access-token": token
    //     }
    //   }
    //   //토큰 -> 멤버 정보 반환
    //   //새로고침 --> 토큰만 갖고 멤버 정보 요청가능
    //   axios
    //     .get(`${API_URL}/accounts/user/`, config)
    //     .then(response => {
    //       let userInfo = {
    //         pk: response.data.data.pk,
    //         username: response.data.data.username,
    //       }
    //       commit("loginSuccess", userInfo);
    //     })
    //     .catch(() => {
    //       alert("이메일과 비밀번호를 확인하세요.");
    //     });
    // }
  },
  modules: {
  }
})
