import Vue from 'vue'
import Router from 'vue-router'
import homepageRouter from './homepage'
import BalancedRouter from './balanced_binary_tree'
import HuffmanEncodeRouter from './hffman/encode'
import HuffmanDecodeRouter from './hffman/decode'
import HuffmanDictionary from './hffman/dictionary'
import MessageBoardRouter from  './message_board'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/homepage' //重定向到主页
    },
    homepageRouter,
    BalancedRouter,
    HuffmanEncodeRouter,
    HuffmanDecodeRouter,
    HuffmanDictionary,
    MessageBoardRouter,
  ]
})
