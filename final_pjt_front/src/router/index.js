import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import MovieDetailView from '@/views/MovieDetailView'
import CommentCreateView from '@/views/CommentCreateView'
import LogInView from '@/views/LogInView'
import SignUpView from '@/views/SignUpView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/create',
    name: 'CommentCreateView',
    component: CommentCreateView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
