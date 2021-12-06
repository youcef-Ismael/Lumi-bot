import Vue from 'vue'
import Vuex from 'vuex'
import defaultPair from '@/assets/defaultpair.json'
import axios from 'axios'
import setHeaderToken from 'axios'
import removeHeaderToken from 'axios'

Vue.use(Vuex);

export default new Vuex.Store({
  strict: true,
  state: {
    user: null,
    isLoggedIn: false, 
    currencies: localStorage.getItem('vue-crypto-currencies-new')? JSON.parse(localStorage.getItem('vue-crypto-currencies-new')) : defaultPair,
    tickers: {},
    chartData: []
  },
  getters: {
    isLoggedIn (state){
      return state.isLoggedIn
    },
    user (state) {
      return state.user
    },
    getSymbolById: state => (symbol) => {
      return state.currencies.find(s => s.symbol === symbol);
    },
    getTickerById: state => (symbol) => {
      return state.tickers[symbol]
    }
  },
  mutations: {
    set_user (state, data) {
      state.user = data
      state.isLoggedIn = true
    }, 
    reset_user (state) {
      state.user = null
      state.isLoggedIn = false
    },
    SET_DEFAULT: (state) => {
      state.currencies = defaultPair
    },
    UPDATE_TICKER: (state, payload) => {
      const tick = state.tickers[payload.symbol]
      payload.pchg = tick ? (payload.price > tick.price? 1 : -1 ) : 1
      Vue.set(state.tickers, payload.symbol, payload)
    },
    ADD_COIN_PAIR: (state, payload) => {
      if(!state.tickers[payload.symbol]) {
        state.currencies.push(payload);
        localStorage.setItem('vue-crypto-currencies-new', JSON.stringify(state.currencies))
      }
      Vue.set(state.tickers, payload.symbol, { pchg: 1 })

    },
    REMOVE_COIN_PAIR: (state, symbol) => {
      Vue.delete(state.tickers, symbol)
      state.currencies.splice(state.currencies.findIndex(s => s.symbol === symbol), 1);
      localStorage.setItem('vue-crypto-currencies-new', JSON.stringify(state.currencies))
    }
  },
  actions: {
    login({ dispatch, commit }, data) {
      return new Promise((resolve, reject) => { 
        axios.post('login', data)
         .then(response => {
           const token = response.data.token  
           localStorage.setItem('token', token) 
           setHeaderToken(token) 
           dispatch('get_user')
           resolve(response)
         })
         .catch(err => {
           commit('reset_user')  
           localStorage.removeItem('token')
           reject(err)
        })
      })
    },
    async get_user({commit}){ 
      if(!localStorage.getItem('token')){
        return
      }
      try{ 
        let response = await axios.get('user')
          commit('set_user', response.data.data)
      } catch (error){
          commit('reset_user') 
          removeHeaderToken()
          localStorage.removeItem('token')
          return error
      } 
    }
  } 
})
