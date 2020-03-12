import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../views/index/index.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect:'/index'
  },
  {
    path: '/index',
    name: 'Index',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component:Index
  },
  {
    path:'/message',
    name:'Message',
    component:() => import(/* webpackChunkName: "about" */ '../views/message/index.vue')
  },
  {
    path:'/announce',
    name:'Announce',
    component:() => import(/* webpackChunkName: "about" */ '../views/announce/index.vue')
  },
  {
    path:'/download',
    name:'Download',
    component:() => import(/* webpackChunkName: "about" */ '../views/download/index.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
