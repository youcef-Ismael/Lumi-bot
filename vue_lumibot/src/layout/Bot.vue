//Bot.vue
<template>
<div>
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

  <div class="row justify-content-md-center">
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">Trading Bot</div>
        <div class="card-header">Fill with your API from your Binance account!</div>
        <div class="card-body">
           
          <form @submit.prevent="SignUp">
            <div class="form-group">
              <label for="api_key">api_key</label>
              <input v-model="api_key" type="text" class="form-control" placeholder="api_key..">
            </div>
            <div class="form-group">
              <label for="api_secret">api_secret</label>
              <input v-model="api_secret" type="password" class="form-control" placeholder="api_secret..">
            </div>
          <!--  <div class="form-group">
              <label for="tel_number">Telephone Number</label>
              <input v-model="tel_number" type="text" class="form-control" placeholder="Telephone..">
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input v-model="email" type="email" class="form-control" placeholder="Email..">
            </div> -->
            <button type="submit" class="btn btn-primary">RUN</button>
          </form>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>  
//import axios from 'axios'

export default {
    data(){
      return {
          api_key: '',
          //last_name: '',
          //first_name: '',
          api_secret: '',
          //tel_number: '',
          //email: '',        
        errors: null
      };
    },
methods: {
    SignUp: function() {
    console.log('sign in clicked')
    let data = {
        api_key: this.api_key,
    //last_name: this.last_name,
    //first_name: this.first_name,
    api_secret: this.api_secret
    //tel_number: this.tel_number,
    //email: this.email
    };
    const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', "x-access-token": "token-value", },
    mode: 'no-cors',
    body: JSON.stringify(data)
  };
    fetch('http://127.0.0.1:8000/bot/', requestOptions)
    .then(function(response) {
        if (response.ok){
this.$router.push({ path: '/layout/:layout' });
console.log(response)
        } else {
console.log(response)
        //resolve(response)
        }
        
      })
}
}
}
  

  
 /* export default {  
    data(){
      return {
          api_key: '',
          last_name: '',
          first_name: '',
          api_secret: '',
          tel_number: '',
          email: '',        
        errors: null
      };
    },
    methods: {
      register: function() { 
          let data = { 
          api_key: this.api_key,
          last_name: this.last_name,
          first_name: this.first_name,
          api_secret: this.api_secret,
          tel_number: this.tel_number,
          email: this.email,
          };
 const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    mode: 'no-cors',
    body: JSON.stringify(data)
  };
  fetch('http://127.0.0.1:8000/bot/register/', requestOptions)
    .then(async response => {
      const data = await response.json();

      // check for error response
      if (!response.ok) {
        // get error message from body or default to response status
        const error = (data && data.message) || response.status;
        return Promise.reject(error);
      }

      this.postId = data.id;
    })
    .catch(error => {
        
      this.errorMessage = error;
      console.error('There was an error!', error);
    });




      this.$store.dispatch('login', this.form)
      .then(response => {
        console.log(response)
  	this.$router.push({name: 'login'})
      }).catch(error => {
        this.errors = error.response.data.errors
      })
    
    
    
    
    } 
    }
  }; */
</script>