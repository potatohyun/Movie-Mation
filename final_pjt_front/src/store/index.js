import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'


Vue.use(Vuex)
const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    token: null,
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
    SAVE_TOKEN(state, token) {
      state.token = token
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
        })
        .catch(err =>console.log(err))
    },
    logIn(context, payload) {
      
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
  },
  modules: {
  }
})
