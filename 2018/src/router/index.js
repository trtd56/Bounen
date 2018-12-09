import Vue from 'vue'
import Router from 'vue-router'

// ElementUI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/ja'

// My Page
import TopPage from '@/components/TopPage'
import ShowScore from '@/components/ShowScore'
import Q1Page from '@/components/Q1Page'
import Q2Page from '@/components/Q2Page'
import Q3Page from '@/components/Q3Page'
import Q4Page from '@/components/Q4Page'
import Q5Page from '@/components/Q5Page'
import Q6Page from '@/components/Q6Page'

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
      path: '/ShowScore',
      name: 'ShowScore',
      component: ShowScore
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
    },
    {
      path: '/Q3Page/:username',
      name: 'Q3Page',
      component: Q3Page
    },
    {
      path: '/Q4Page/:username',
      name: 'Q4Page',
      component: Q4Page
    },
    {
      path: '/Q5Page/:username',
      name: 'Q5Page',
      component: Q5Page
    },
    {
      path: '/Q6Page/:username',
      name: 'Q6Page',
      component: Q6Page
    }
  ]
})
