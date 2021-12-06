<template>
    <div class="layout-container">
        <header class="page-header bg-primary">
            <button class="back-btn" @click="$router.push({ path: '/layout/:layout' })">
                <i class="fa fa-angle-left fa-2x"></i>
            </button>
            <span class="page-title">LumiBot</span>
        </header>
        <div class="page-container">
            <transition name="fade" mode="out-in">
                <keep-alive include="dashboard">
                    <router-view/>
                </keep-alive>
            </transition>
        </div>
    </div>
</template>
<script>
  export default {
    name: 'LayoutPage',
    data() {
      return {
        currentPage: 'dashboard'
      }
    },
    watch: {
      '$route': {
        deep: true,
        handler: function (page) {
          this.currentPage = page.name;
        }
      }
    }
  }
</script>
<style scoped>
a{text-decoration: none; font-size: 20px;font-family: sans-serif;padding: 0 14px 10px 10px}
ul{padding: 0px 10px 14px 14px}
li{list-style: none; display: inline;}
li a{background: #222; color:#7dc40b;}
li a:hover{background: #5a7e06; color:#fff; text-decoration: none;}
.navi{background: #222; height: 50px; margin-top: -10px;}
</style>