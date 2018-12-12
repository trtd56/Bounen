import Vue from 'vue'
import Router from 'vue-router'

// ElementUI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/ja'

// My Page
import TopPage from '@/components/TopPage'
import ShowScore from '@/components/ShowScore'
import QPage from '@/components/QPage'

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
      path: '/:QPage/:username',
      name: 'QPage',
      component: QPage,
      props: (route) => ({ username: route.params.username, ...problem_name(route.params.QPage) })
    }
  ]
})

function problem_name(QPage){
    let prob = {}
    switch (QPage){
        case 'Q1Page':
            prob.problem_name = "問題1: ボール投げ";
            prob.next_page = 'Q2Page'
            break;
        case 'Q2Page':
            prob.problem_name = "問題2: 射的";
            prob.next_page = 'Q3Page'
            break;
        case 'Q3Page':
            prob.problem_name = "問題3: 釣り";
            prob.next_page = 'Q4Page'
            break;
        case 'Q4Page':
            prob.problem_name = "問題4: せせらぎバトル(パワー)";
            prob.next_page = 'Q5Page'
            break;
        case 'Q5Page':
            prob.problem_name = "問題5: せせらぎバトル(バランス)";
            prob.next_page = 'Q6Page'
            break;
        case 'Q6Page':
            prob.problem_name = "問題6: せせらぎバトル(スピード)";
            prob.next_page = 'TopPage'
            break;
    }
    return prob;
}
