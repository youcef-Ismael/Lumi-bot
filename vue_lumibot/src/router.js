import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

const router = new Router({
  base: process.env.BASE_URL,
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'LoginPage',
      component: () => import('./auth/Login.vue')
    },
	{
      path: '/layout/:layout',
      name: 'dashboard',
      component: () => import('./views/Dashboard.vue')
    },
    {
      path: '/view/:symbol',
      name: 'infoview',
      component: () => import('./views/InfoView.vue'),
      props: true
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('./auth/Register.vue'),
    },
    {
      path: '/bot',
      name: 'bot',
      component: () => import('./layout/Bot.vue'),
    },
    {
      path: '/layout/:layout',
      name: 'dashboard',
      component: () => import('./layout/LayoutPage.vue'),
      props: true
    }
  ]
})
router.beforeEach((to, from, next) => {
  next()
})
export default router;