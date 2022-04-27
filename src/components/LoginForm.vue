<template>
    <h2 class="pg-header" id="loginheader">Login to your account</h2>
    <div class="card text-left" style="width: 25rem;" id="logincard">
        <div class="card-body">
            <form id= "LoginForm" >
                <div class="col-auto">
                    <div class="form-group">
                        <label for="username">Username</label>
                        <input name="username" v-model="username" placeholder=" " class="form-control register-form">
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input name="password" v-model="password" placeholder=" " type="password" class="form-control register-form">
                    </div>
                </div>

                <br>

                <div class="col-12">
                    <button id="loginbtn" type="submit" name="submit" class="btn btn-primary" @click.prevent="login">Login</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import store from '@/main.js';
 export default {
    data() {
        return {
            csrf_token: '',
            username: '',
            password: ''     
        }
    },
    
    methods: {
        login(){
            
            let loginForm = document.getElementById('LoginForm');
            let formdata = new FormData(loginForm);

            fetch("/api/auth/login", {
                method: 'POST', 
                body: formdata,
                headers: {'X-CSRFToken': this.csrf_token}
            })

            .then(function (response) {
                console.log(response)
                return response.json();
            })

            .then(function (data) {
                // display a success message
                if(data.token != ''){
                    localStorage.setItem('token', data.token );
                    localStorage.setItem('id', data.id);
                    store.commit('checkiftrue', true);
                    store.commit('checkid', data.id );
                }
                
                else{
                    localStorage.setItem('token', null );
                    localStorage.setItem('id', null );
                    store.commit('checkiftrue', false);
                }

                localStorage.setItem('auth', data.auth );
                console.log("shows check :", store.state.check, store.state.uid)
                console.log("token in local storage",localStorage.getItem('id'))
                console.log(data.token, data.id,localStorage.getItem('auth') );

                return(data);
            })

            .catch(function (error) {
                console.log(error);
            });

            this.$router.push('/explore');

        },

        getCsrfToken(){
            console.log("logged state",this.$store.state.auth)
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        },
    }  
}
</script>

<style>

    #logincard{
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 4%;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }

    #loginheader{
        font-size: 2em;
        font-weight: bold;
        text-align: center;
        margin-top:6% ;
        
    }

    #loginbtn{
        background-color: #0fb881;
        border: 1px solid transparent;
        width: 100%;
    }

    label{
        font-weight: bold;
        font-size: 0.8em;
    }
</style>