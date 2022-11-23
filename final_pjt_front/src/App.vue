<template>
  <div id="app">
    <img class= "logo" 
      src="./assets/moviemation_Agency_FB.png" 
      alt="logo"
      @click="goMovieHome"
    >
    <b-navbar class="navbar navbar-expand-sm bg-dark navbar-dark" sticky="true">
      <div class="container-fluid">
        <div class="collapse navbar-collapse justify-content-center" id="collapsibleNavbar">
          <ul class="navbar-nav" v-if="this.$store.state.token">
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'MovieView' }">
                  Home
                </router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'RecommendView' }">
                  Recommend
                </router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'UserStatusView'}">
                  user
                </router-link>
              </a>
            </li>
          </ul>
          <ul class="navbar-nav" v-if="!this.$store.state.token">
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'MovieView' }">
                  Home
                </router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'LogInView' }">
                  Login
                </router-link>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link :to="{ name:'SignUpView' }">
                  signup
                </router-link>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </b-navbar>
    <router-view/>
  </div>
</template>

<script>
export default {
  methods:{
    goMovieHome(){
      this.$router.push({ name:'MovieView' })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #b9333a;
}

nav a.router-link-exact-active {
  color: #7543af;
}

.logo {
  width: 50vw;
  padding: 30px;
}
</style>
