<template>
<div>
 <div class="layout-container">
        <header class="page-header bg-primary">
            <span class="page-title">LumiBot</span>
        </header>
        <div class="page-container" style="margin-top: -20px;">
            <transition name="fade" mode="out-in">
                <keep-alive include="dashboard">
                    <router-view/>
                </keep-alive>
            </transition>
        </div>
    </div>
    <div class="content-box">
        <div class="menu-bar">
            <v-select id="base" :options="currencyList[quote]['pairs']" :clearable="false" v-model="baseCurrency"
                      placeholder="Select Token"></v-select>
            <span class="slash">/</span>
            <v-select id="quote" :options="quoteOptions" :searchable="false" :clearable="false" v-model="quote"
                      @input="resetBase" style="width: 100px"></v-select>
            <button class="add-btn" @click="addCoinPair"><i class="fa fa-plus fa-lg" aria-hidden="true"></i></button>
        <nav class="navi">
<ul>
<li><a href="/layout/:layout">DASHBOARD</a></li>
<li><a href="#">Trading Bot</a></li>
<!-- <li><a href="#">PROFILE</a></li> -->
<li><a href="/">LOGOUT</a></li>
</ul>
</nav>
        </div>
        <CryptoBoard></CryptoBoard>
        <button class="clear-btn" @click="clear">Clear All</button>
    </div>
	</div>
</template>
<script>
    import vSelect from 'vue-select'
    import coins from '@/assets/group.json'
    import CryptoBoard from '@/views/CryptoBoard.vue'
    import {isEmpty} from '../util/Utility'
    import {subscribeSymbol} from '../services/binance'
    import {mapState} from 'vuex'

    export default {
        name: 'dashboard',
        data() {
            return {
                currencyList: coins,
                quote: 'BNB',
                baseCurrency: {}
            }
        },
        mounted() {
            if (this.currencies) {
                this.currencies.forEach(currency => {
                    subscribeSymbol(currency.symbol);
                });
            }
        },
        computed: {
            ...mapState(['currencies']),
            quoteOptions() {
                return Object.keys(coins)
            }
        },
        components: {
            vSelect,
            CryptoBoard
        },
        methods: {
            resetBase() {
                this.baseCurrency = {}
            },
            clear() {
                localStorage.clear();
                location.reload();
            },
            addCoinPair() {
                if (!isEmpty(this.baseCurrency)) {
                    const symbol = `${this.baseCurrency.value}${this.quote}`;
                    subscribeSymbol(symbol);
                    this.$store.commit('ADD_COIN_PAIR', {
                        "symbol": symbol,
                        "base": this.baseCurrency.value,
                        "quote": this.quote,
                        "name": this.baseCurrency.name,
                        "cid": this.baseCurrency.cid
                    })
                }
            }
        }
    }
</script>
<style scoped>
a{text-decoration: none; font-size: 20px;font-family: sans-serif;padding: 14px 14px 10px 10px}
ul{padding: 24px 10px 14px 14px}
li{list-style: none; display: inline;}

</style>