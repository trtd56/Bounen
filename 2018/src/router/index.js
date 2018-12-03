import Vue from 'vue'
import Router from 'vue-router'

// ElementUI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/ja'

// My Page
import TopPage from '@/components/TopPage'
import Q1Page from '@/components/Q1Page'
import Q2Page from '@/components/Q2Page'

Vue.use(ElementUI, {locale})
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'TopPage',
      component: TopPage
    },
    {
      path: '/Q1Page/:username',
      name: 'Q1Page',
      component: Q1Page
    },
    {
      path: '/Q2Page/:username',
      name: 'Q2Page',
      component: Q2Page
    }
  ]
})
