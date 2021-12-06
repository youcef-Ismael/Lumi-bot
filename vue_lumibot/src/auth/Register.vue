//Register  .vue
<template>

  <div class="row justify-content-md-center">
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">Register</div>
        <div class="card-body">
           
          <form @submit.prevent="SignUp">
            <div class="form-group">
              <label for="api_key">api_key</label>
              <input v-model="api_key" type="text" class="form-control" placeholder="api_key..">
            </div>
            <div class="form-group">
              <label for="last_name">Last Name</label>
              <input v-model="last_name" type="text" class="form-control" placeholder="Last Name..">
            </div>
            <div class="form-group">
              <label for="first_name">First Name</label>
              <input v-model="first_name" type="text" class="form-control" placeholder="First Name..">
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
            <button type="submit" class="btn btn-primary">Register</button>
          </form>
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
          last_name: '',
          first_name: '',
          api_secret: '',
          //tel_number: '',
          //email: '',        
        errors: null
      };
    },
methods: {
    SignUp: function() {
    console.log('sign up clicked')
    let data = {
        api_key: this.api_key,
    last_name: this.last_name,
    first_name: this.first_name,
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
    fetch('http://127.0.0.1:8000/bot/register/', requestOptions)
    .then(function(response) {
        if (response.status == 'Success'){
          console.log(response)
this.$router.push({ path: '/' });

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